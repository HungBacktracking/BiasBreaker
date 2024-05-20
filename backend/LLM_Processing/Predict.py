from LLM_Models.model import Predictor
import time

predictor = Predictor()

def insert_predict(dataset):
    for article in dataset:
        text = article['content']

        prediction = ""
        try:
            prediction = predictor.predict_from_article(text)
        except:
            print("Error while predicting")

        article['prediction'] = prediction
        time.sleep(35)

