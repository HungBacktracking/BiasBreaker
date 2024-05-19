from model.model import KeywordExtractor
import time

kw_extractor = KeywordExtractor()

def insert_keywords(dataset):
    for article in dataset:
        text = article['content']

        keywords = []
        try:
            keywords = kw_extractor.extract_keywords(text)
        except:
            print("Error while extracting keywords")

        for keyword in keywords:
            if keyword not in article['keywords']:
                article['keywords'].append(keyword)
        time.sleep(15)