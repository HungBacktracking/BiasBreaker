from .utils import *
from . import world
import os
import requests
import heapq

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.text_splitter import TokenTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain.schema.document import Document
# from langchain.globals import set_debug
# set_debug(True)
import google.generativeai as genai
genai.configure(api_key=world.GOOGLE_API_KEY)

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

    def __init__(self, model_name="gemini-pro"):
        """
        Initializes the TextSummarizer class.

        Args:
            model_name (str, optional): The name of the model to use for text summarization.
                                        Default is 'gemini-pro'.

        Raises:
            AssertionError: If the model_name is not one of the available models or
                            if the option is not one of {'easy', 'normal', 'detailed'}.
        """
        assert model_name in ["gemini-pro"], "Invalid model_name"
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
        result["easy"] = self.summarize(text_file, "easy")
        result["normal"] = self.summarize(text_file, "normal")
        result["detailed"] = self.summarize(text_file, "detailed")
        return result

    def summarize(self, text, option="normal"):
        """
        Summarizes the given text.

        Args:
            text (str): The text to be summarized.
            option (str, optional): The level of detail for the summary.
                                    Options are 'easy', 'normal', 'detailed'. Default is 'Normal'.

        Returns:
            str: The summarized text.
        """
        assert option in ["easy", "normal", "detailed"], "Invalid option"
        # Define the Summarize Chain
        prompt = PromptTemplate.from_template(self.templates[option])
        llm_chain = LLMChain(llm=self.llm, prompt=prompt)
        stuff_chain = StuffDocumentsChain(
            llm_chain=llm_chain, document_variable_name="text"
        )

        # Invoke Chain
        loader = StringLoader(text)
        docs = loader.load()
        response = stuff_chain.invoke(docs)

        return response["output_text"]
    

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
            self.template1 = "Với thông tin về công ty: {company_info} và bài báo: {news_article}, dự đoán các tác động có thể xảy ra nếu chúng liên quan đến một hoặc một số lĩnh vực sau của công ty: Giao hàng, Di chuyển hoặc Dịch vụ Tài chính. DỰ ĐOÁN:"
            self.company_info = WebBaseLoader(company_url).load()
            self.template2 = "Với thông tin về công ty: {company_info} và các từ khóa: {keywords}, cùng với các tiêu đề bài báo liên quan: {titles}, dự đoán các tác động có thể xảy ra nếu chúng liên quan đến một hoặc một số lĩnh vực sau của công ty: Giao hàng, Di chuyển hoặc Dịch vụ Tài chính. DỰ ĐOÁN:"
        
        def predict_from_article(self, news_article):
            """_summary_

            Args:
                news_article (_type_): _description_

            Returns:
                _type_: _description_
            """
            prompt_template = PromptTemplate(
                template=self.template1,
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
        
        def predict_from_keywords(self, keywords, titles):
            """_summary_

            Args:
                keywords (_type_): _description_
                titles (_type_): _description_

            Returns:
                _type_: _description_
            """
            prompt_template = PromptTemplate(
                template=self.template2,
                input_variables=["company_info", "keywords", "titles"],
            )
            
            chain = LLMChain(
                llm=self.llm,
                prompt=prompt_template
            )
            
            kw_loader = StringLoader(keywords)
            kw_docs = kw_loader.load()
            article_loader = StringLoader(titles)
            article_docs = article_loader.load()
            
            prediction = chain.run(
                company_info=self.company_info,
                keywords=kw_docs,
                titles=article_docs,
            )
            
            return prediction
        

class KeywordExtractor(object):
    def __init__(self, count=5):
        """
        Initializes the KeywordExtractor class.

        Args:
            count (int, optional): The number of keywords to extract. Default is 5.
        """
        self.count = count
        self.llm = genai.GenerativeModel("gemini-pro")
        self.prompt_template = "Tìm {count} từ khóa thời sự quan trọng trong đoạn tin tức sau: {text} TỪ KHÓA: 1. <keyword> 2. <keyword> 3. <keyword> ..."
    
    def extract_keywords(self, text):
        """
        Extracts keywords from the given text.

        Args:
            text (str): The text from which keywords need to be extracted.

        Returns:
            list: A list of the top `count` ranked phrases as keywords.
        """
        prompt = self.prompt_template.format(count=self.count, text=text)
        response = self.llm.generate_content(prompt)
        response = response.text.split("\n")
        response = [line.split('. ')[1] for line in response if line]
        return response
        

# text = """
# Hãng chip tỷ USD của Mỹ tăng tốc mở rộng ở Việt Nam
# Marvell - nhà thiết kế chip tỷ USD của Mỹ, tăng tốc mở rộng hoạt động ở Việt Nam để sớm vào top 3 trung tâm lớn nhất tập đoàn.
# Thông tin được TS Lợi Nguyễn, Phó chủ tịch Cấp cao về Cloud Optics của Marvell cho biết ngày 17/5. Theo đó, Marvell vừa mở văn phòng mới tại Đà Nẵng khoảng một tháng, với nhân sự tầm 50 người.
# Họ sẽ lập văn phòng thứ hai ở TP HCM ngay năm nay. Văn phòng mới này, cũng như các trung tâm kỹ thuật khác của Marvell tại Việt Nam sẽ tập trung vào các công nghệ vi mạch mới như kết nối quang, lưu trữ, công nghệ bán dẫn tín hiệu tương tự và tín hiệu hỗn hợp (mixed signal).
# Đây là những công nghệ then chốt trong việc tăng tốc xây dựng cơ sở hạ tầng mới, nhằm đáp ứng nhu cầu về hiệu suất và tốc độ ngày càng gia tăng của các trung tâm dữ liệu đám mây và trí tuệ nhân tạo (AI).
# Thành lập năm 1995, Marvell là một trong số ít các nhà thiết kế chip nổi bật của Mỹ cùng với Nvidia trong thời đại AI lên ngôi. Sản phẩm của 2 gã khổng lồ này mang tính bổ trợ nhau.
# Chip của Nvidia là chip thuần túy với kiến trúc xử lý GPU và chip của Marvell giúp kết nối các GPU với nhau. Năm ngoái, hãng thiết kế chip này đạt doanh thu 5,5 tỷ USD. Khép phiên 17/5, cổ phiếu Marvell đạt trên 73 USD trên sàn Nasdaq, vốn hóa xấp xỉ 141 tỷ USD.
# Marvell đến Việt Nam đã được 10 năm với ban đầu chỉ chục kỹ sư. Họ phát triển mạnh 2 năm nay, khi AI thành cơn sốt. Hiện họ đạt quy mô 400 nhân sự tại Việt Nam, tăng hơn 30% chỉ sau 8 tháng, với 97% là kỹ sư.
# Tiến độ này vượt mục tiêu tăng trưởng 50% trong vòng 3 năm đã được Chủ tịch & CEO Matt Murphy cam kết tại Hội nghị cấp cao Việt Nam - Mỹ về đầu tư và đổi mới sáng tạo được tổ chức vào tháng 9/2023.
# "Trong 3 năm tới, chúng tôi kỳ vọng sẽ tăng trưởng khoảng 20% một năm về quy mô nhân sự, hướng tới cột mốc 500 kỹ sư trong tương lai không xa", TS Lê Quang Đạm, Tổng giám đốc Marvell Việt Nam cho biết thêm.
# Với quy mô này, Việt Nam sẽ là trung tâm hoạt động lớn thứ 3, chỉ sau trụ sở chính tại Mỹ và Ấn Độ. Hiện tập đoàn có 6.800 nhân sự toàn cầu. Ngay năm nay, ông Đạm định tuyển thêm khoảng 60 kỹ sư và cấp 30 suất học bổng. Công ty tập trung tuyển 2 nhóm kỹ sư, với thuận lợi và thách thức riêng.
# Các kỹ sư mới ra trường có nền tảng kiến thức kỹ thuật cơ bản tốt nên chỉ cần đào tạo khoảng 6-9-12 tháng là có thể làm việc. Tuy nhiên, phần lớn chưa mạnh về giao tiếp tiếng Anh, khả năng làm việc nhóm, trình bày và quản lý dự án.
# Trong khi đó, kỹ sư 5-15 năm kinh nghiệm, quản lý được dự án, đảm nhiệm khâu kiến trúc trong ngành vi mạch bán dẫn rất khan hiếm. "Đây là khó khăn chung ở Việt Nam vì công nghiệp bán dẫn vi mạch còn khá non trẻ", ông Đạm nhận xét.
# Để giải quyết, ông cho rằng cần thời gian hợp tác với các trường - viện để xây dựng nguồn cung cấp nhân lực. Khi so sánh trong Đông Nam Á, nhân lực ở Việt Nam mạnh về kiến thức cơ bản chắc. Tuy nhiên, quy mô các trường đại học còn nhỏ, và chất lượng hạn chế so với các trường khu vực và thế giới.
# Trong ngành vi mạch bán dẫn Việt Nam, 80% nhân sự tập trung tại TP HCM, 12% ở Đà Nẵng và còn lại ở Hà Nội. Để chiêu mộ, ngoài mở văn phòng tại các nơi này, Marvell đầu tư vào cơ hội tiếp cận công nghệ mới, môi trường làm việc và lương thưởng, phúc lợi. Họ tặng cổ phiếu cho 100% nhân viên chính thức, với số lượng tùy cấp bậc và thành tích.
# Ngoại trừ công đoạn đầu tiên là kiến trúc hệ thống, kỹ sư Marvell Việt Nam tham gia vào hầu hết công đoạn như thiết kế, kiểm tra thiết kế, giai đoạn GDSII (chuyển đổi từ định dạng thiết kế sang sản xuất).
# Họ tham gia vào những công nghệ mới nhất, từ 28 nano, 14 nano, 7 nano, 5 nano, thậm chí tập đoàn đang xem xét làm những dự án 3 và 2 nano. Ông Bùi Quang Ngọc, Phó chủ tịch Bộ phận Kết nối dữ liệu Marvell Việt Nam cho biết đội ngũ Việt Nam đóng góp trực tiếp vào nhiều sản phẩm tiên tiến nhất của tập đoàn.
# "Tôi ví dụ Nova là sản phẩm hiện đại nhất và đầu tiên trên thế giới cung cấp kết nối tốc độ cao 1.6 terabyte/giây. Nova 2 có 8 cổng, mỗi cổng có thể truyền dẫn ở tốc độ 200 gygabyte/giây - tốc độ cao nhất và đầu tiên trên thế giới hiện tại", ông nói.
# Đối với khách hàng nội địa, Vinfast đang sử dụng con chip "Ethernet on car" - kết nối các thiết bị trong xe hơi, các bộ phận cảm ứng, các bộ phận điều khiển CPU trong xe hơi của Marvell.
# "Có 17 trên 20 công ty sản xuất xe hàng đầu thế giới đã sử dụng chip của Marvell. Ngoài ra, một số doanh nghiệp lớn tại Việt Nam đang làm việc với chúng tôi để hướng tới việc sử dụng chip", ông Đạm tiết lộ.
# Marvell hoạt động dưới mô hình fabless (công ty thiết kế và bán chip nhưng phần sản xuất được đặt gia công bởi nhà máy đối tác) và không có dự định mở nhà máy sản xuất. Họ tập trung vào việc thiết kế chip, còn sản xuất sẽ do một bên thứ ba ở Đài Loan hoặc Mỹ đảm nhiệm. Việc kiểm định cũng do một bên thứ ba phụ trách.
# Đặt nhiều tham vọng ở Việt Nam nhưng hãng không tiết lộ số tiền cụ thể định rót thêm. "Quy mô tùy thuộc vào tình hình các dự án và tuyển dụng. Một trong những yếu tố lớn cho vốn đầu tư của công ty là số lượng nhân lực", ông Đạm nói.
# """
# keyword_extractor = KeywordExtractor()
# print(keyword_extractor.extract_keywords(text))