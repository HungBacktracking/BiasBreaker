from utils import *
import world 
import os
import requests

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.text_splitter import TokenTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain.schema.document import Document
# from langchain.globals import set_debug
# set_debug(True)

from rake_nltk import Rake

# from rich.markdown import Markdown
# from rich.console import Console
# console = Console()

import warnings
from langchain_core._api.deprecation import LangChainDeprecationWarning
warnings.filterwarnings("ignore", category=LangChainDeprecationWarning)

os.environ["GOOGLE_API_KEY"] = world.GOOGLE_API_KEY

class StringLoader(object):
    def __init__(self, text):
        self.text = text
        
    def _get_text_chunks(self, text):
        text_splitter = TokenTextSplitter(chunk_size=500, chunk_overlap=100)
        docs = [Document(page_content=x) for x in text_splitter.split_text(text)]
        return docs

    def load(self):
        return self._get_text_chunks(self.text)

class TextSummarizer(object):
    
    def __init__(self, model_name='gemini-pro'):
        """
        Initializes the TextSummarizer class.

        Args:
            model_name (str, optional): The name of the model to use for text summarization. 
                                        Default is 'gemini-pro'.

        Raises:
            AssertionError: If the model_name is not one of the available models or 
                            if the option is not one of {'easy', 'normal', 'detailed'}.
        """
        assert model_name in ['gemini-pro'], "Invalid model_name"
        # Initialize model
        self.llm = ChatGoogleGenerativeAI(model=model_name)
        # Define templates for summarization
        self.templates = {
            'easy': "Viết một bản tóm tắt ngắn gọn về nội dung sau đây: {text} TÓM TẮT NGẮN GỌN:",
            'normal': "Viết một bản tóm tắt về nội dung sau đây: {text} TÓM TẮT:",
            'detailed': "Viết một bản tóm tắt chi tiết về nội dung sau đây: {text} TÓM TẮT CHI TIẾT:"
        }
        
    def get_result(self, text_file):
        """
        Get the result of the text summarization.

        Args:
            text_file (str): The path to the text file to be summarized.

        Returns:
            dict: The result of the text summarization.
        """
        result = {}
        result['easy'] = self.summarize(text_file, 'easy')
        result['normal'] = self.summarize(text_file, 'normal')
        result['detailed'] = self.summarize(text_file, 'detailed')
        return result
        
    def summarize(self, text, option='normal'):
        """
        Summarizes the given text.

        Args:
            text (str): The text to be summarized.
            option (str, optional): The level of detail for the summary. 
                                    Options are 'easy', 'normal', 'detailed'. Default is 'Normal'.

        Returns:
            str: The summarized text.
        """
        assert option in ['easy', 'normal', 'detailed'], "Invalid option"
        # Define the Summarize Chain
        prompt = PromptTemplate.from_template(self.templates[option])
        llm_chain = LLMChain(llm=self.llm, prompt=prompt)
        stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="text")

        # Invoke Chain
        loader = StringLoader(text)
        docs = loader.load()
        response = stuff_chain.invoke(docs)

        return response["output_text"]

# text = 'The COVID-19 pandemic has had a profound impact on the global economy, with many businesses forced to close their doors and millions of people losing their jobs. In response to the crisis, governments around the world have implemented various measures to support businesses and workers, including stimulus packages, tax breaks, and unemployment benefits. However, the economic fallout from the pandemic is far from over, and many experts warn that the worst is yet to come. In this article, we will explore the economic impact of the COVID-19 pandemic and discuss what the future may hold for the global economy.'
# text_summarizer = TextSummarizer()
# console.print(Markdown('### CONCISE SUMMARY\n' + text_summarizer.summarize(text, 'easy') + '\n'))
# console.print(Markdown('### SUMMARY\n' + text_summarizer.summarize(text, 'normal') + '\n'))
# console.print(Markdown('### DETAILED SUMMARY\n' + text_summarizer.summarize(text, 'detailed')))

class Predictor(object):
        
        def __init__(self, model_name='gemini-pro', company_url='https://www.grab.com/vn/en/'):
            """
            Initializes the Predictor class.
    
            Args:
                model_name (str, optional): The name of the model to use for prediction. 
                                            Default is 'gemini-pro'.
                company_url (str, optional): The URL of the company website.
    
            Raises:
                AssertionError: If the model_name is not one of the available models.
            """
            assert model_name in ['gemini-pro'], "Invalid model_name"
            # Initialize model
            self.llm = ChatGoogleGenerativeAI(model=model_name)
            # Define template for prediction
            self.template = "Với thông tin về công ty: {company_info} và bài báo: {news_article}, dự đoán các tác động có thể xảy ra nếu chúng liên quan đến một hoặc một số lĩnh vực sau của công ty: Giao hàng, Di chuyển hoặc Dịch vụ Tài chính. DỰ ĐOÁN:"
            self.company_info = WebBaseLoader(company_url).load()
        
        def predict(self, news_article):
            prompt_template = PromptTemplate(
                template=self.template,
                input_variables=["company_info", "news_article"],
            )
            
            chain = LLMChain(
                llm=self.llm,
                prompt=prompt_template
            )
            
            loader = StringLoader(news_article)
            docs = loader.load()
            
            prediction = chain.run(
                company_info=self.company_info,
                news_article=docs,
            )
            
            return prediction
        
# predictor = Predictor()
# news_article = 'The COVID-19 pandemic has had a profound impact on the global economy, with many businesses forced to close their doors and millions of people losing their jobs. In response to the crisis, governments around the world have implemented various measures to support businesses and workers, including stimulus packages, tax breaks, and unemployment benefits. However, the economic fallout from the pandemic is far from over, and many experts warn that the worst is yet to come. In this article, we will explore the economic impact of the COVID-19 pandemic and discuss what the future may hold for the global economy.'
# console.print(Markdown('### PREDICTION\n' + predictor.predict(news_article)))

def keyword_extractor(text, count=5):
    """Extracts keywords from the given text.

    Args:
        text (str): The text from which keywords need to be extracted.
        count (int, optional): The number of keywords to extract. Defaults to 5.

    Returns:
        list: A list of the top `count` ranked phrases as keywords.
    """
    r = Rake()
    r.extract_keywords_from_text(text)
    return r.get_ranked_phrases()[:count]

print(keyword_extractor('''spaCy is an open-source software library for advanced natural language processing,
written in the programming languages Python and Cython. The library is published under the MIT license
and its main developers are Matthew Honnibal and Ines Montani, the founders of the software company Explosion.'''))