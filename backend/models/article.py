from database import db
from bson import ObjectId

articles = db['articles']
class Article:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    @staticmethod
    def find_one(id):
        article = articles.find_one({'_id': ObjectId(id)})
        return article

