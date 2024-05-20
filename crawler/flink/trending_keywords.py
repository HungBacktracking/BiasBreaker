from pymongo.mongo_client import MongoClient
from datetime import datetime, timedelta
import config

import argparse
import logging
import sys

from pyflink.common import WatermarkStrategy, Encoder, Types, Row
from pyflink.common.serialization import SimpleStringSchema
from pyflink.datastream import StreamExecutionEnvironment, RuntimeExecutionMode
from pyflink.datastream.connectors.file_system import (FileSource, StreamFormat, FileSink, OutputFileConfig, RollingPolicy)
from pyflink.datastream.connectors import FlinkKafkaProducer

# MongoDB connection URI
uri = f"mongodb+srv://{config.USER}:{config.PASSWORD}@cluster0.izgloib.mongodb.net"

def fetch_articles(start_date, end_date):
    with MongoClient(uri) as client:
        db = client['BiasBreakerDatabase']
        collection = db['articles']
        query = {'datetime': {'$gte': start_date, '$lte': end_date}}
        articles = collection.find(query)
        return list(articles)  # Convert cursor to list

def prepare_data(articles):
    data = []
    for article in articles:
        for keyword in article['keywords']:
            data.append(Row(keyword, 1))
    return data

def keyword_count(date=None, mode='daily', top_n=10, output_path=None):
    """
    Count the number of articles for each keyword in the given date 
    
    Args:
        date (datetime): The date to count the number of articles
        mode (str): The mode to count the number of articles. It can be 'daily', 'weekly', or 'monthly'.
    
    Returns:
    """
    assert mode in ['daily', 'weekly', 'monthly'], "Invalid mode. It must be 'daily', 'weekly', or 'monthly'."
    # Get the start date
    if mode=='daily':
        start_date = date - timedelta(days=1)
    elif mode=='weekly':
        start_date = date - timedelta(days=7)
    elif mode=='monthly':
        start_date = date - timedelta(days=30)
  
    input_data = prepare_data(fetch_articles(start_date, date))

    # Create a StreamExecutionEnvironment
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_runtime_mode(RuntimeExecutionMode.BATCH)
    # Set the parallelism
    env.set_parallelism(1)
    
    # Define the source
    ds = env.from_collection(collection=input_data, type_info=Types.ROW([Types.STRING(), Types.LONG()]))
    
    # Compute keyword count
    ds = ds.key_by(lambda row: row[0]) \
        .reduce(lambda row1, row2: Row(row1[0], row1[1] + row2[1]))
        
    # Collect all data to the driver
    collected = ds.execute_and_collect()
    
    # Sort by frequency and get top N
    sorted_data = sorted(collected, key=lambda row: row[1], reverse=True)[:top_n]
    if output_path is None:
        output_path = f"{mode}_trending_keywords_{date.strftime('%d-%m-%Y')}.txt"
        with open(output_path, 'w') as f:
            for keyword, count in sorted_data:
                f.write(f"{keyword}: {count}\n")
    
    # Define the sink
    ds.print()
    
    # Execute the job
    env.execute("Keyword Count")

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(message)s")
    
    parser = argparse.ArgumentParser(description='Count the number of articles for each keyword in the given date to find top N keywords with the highest number of articles')
    parser.add_argument('--date', type=lambda s: datetime.strptime(s, '%d-%m-%Y'), default=datetime.now(), help='The date to count the number of articles')
    parser.add_argument('--mode', type=str, default='daily', help='The mode to count the number of articles. It can be "daily", "weekly", or "monthly"')
    parser.add_argument('--top_n', type=int, default=10, help='The number of top keywords to show')
    parser.add_argument('--output', type=str, help='The output path to save the result')
    
    args = parser.parse_args()
    
    keyword_count(args.date, args.mode, args.top_n, args.output)
            