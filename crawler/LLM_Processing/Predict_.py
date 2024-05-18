from model.model import Predictor
import time

def insert_predict(dataset):
    for article in dataset:
        text = article['content']
        predictor = Predictor()
        prediction = predictor.predict_from_article(text)
        article['prediction'] = prediction
        time.sleep(20)

