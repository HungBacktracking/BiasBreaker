from model.model import KeywordExtractor
import time

def insert_keywords(dataset):
    for article in dataset:
        text = article['content']
        kw_extractor = KeywordExtractor()
        keywords = kw_extractor.extract_keywords(text)
        for keyword in keywords:
            if keyword not in article['keywords']:
                article['keywords'].append(keyword)
        article['keywords'] = keywords
        time.sleep(15)