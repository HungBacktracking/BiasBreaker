from model.model import TextSummarizer
import time

summarizer = TextSummarizer()


def insert_summaries(dataset):
    for data in dataset:
        content = data["content"]
        
        summary_content = ""
        try:
            summary_content = summarizer.get_result(content)
        except:
            print("Error while summarizing")

        data["summaries"] = summary_content
        time.sleep(35)
