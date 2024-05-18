from model.model import Predictor

def insert_predict(dataset):
    for article in dataset:
        text = article['content']
        predictor = Predictor()
        prediction = predictor.predict_from_article(text)
        article['prediction'] = prediction

