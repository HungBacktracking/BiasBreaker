import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId
import config

uri = "mongodb+srv://{}:{}@cluster0.izgloib.mongodb.net".format(config.USER, config.PASSWORD)
db = MongoClient(uri)['BiasBreakerDatabase']
        
class Recommender(object):
    def __init__(self):
        # Load the articles from the database
        self.articles = self._load_articles()
        self.df = pd.DataFrame(self.articles)
        # Keep the article id, category, title, content, and keywords
        self.df = self.df[['_id', 'category', 'title', 'content', 'keywords']] 
        self._create_vectorizer()
        self._compute_similarity()
    
    def _load_articles(self):
        articles = []
        for article in db['articles'].find():
            articles.append(article)
        return articles
    
    def _create_vectorizer(self):
        # Create a TfidfVectorizer
        self.vectorizer = TfidfVectorizer(stop_words='english')
        # Fit and transform the data
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['content'])
        
    def _compute_similarity(self):
        # Compute the cosine similarity matrix
        self.cosine_sim = np.dot(self.tfidf_matrix, self.tfidf_matrix.T).toarray()
        # Normalize the cosine similarity matrix
        norm = np.linalg.norm(self.tfidf_matrix.toarray(), axis=1)
        self.cosine_sim = self.cosine_sim / norm[:, None]
        # Save the cosine similarity matrix to a dataframe
        self.cosine_sim_df = pd.DataFrame(self.cosine_sim, index=self.df['_id'], columns=self.df['_id'])

    def get_recommendations_from_item(self, item_id, k=20):
        """
        Get the top n recommendations for the given item_id
        
        Args:
            item_id (str): The item id to get the recommendations
            top_n (int): The number of recommendations to return
        
        Returns:
            list: The list of recommended items
        """
        # Get the item's index
        item_idx = self.df[self.df['_id']==item_id].index[0]
        # Get the similarity scores
        sim_scores = list(enumerate(self.cosine_sim[item_idx]))
        # Sort the items based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        # Get the top n recommendations
        top_n_recs = sim_scores[1:k+1]
        # Get the item ids
        item_ids = [self.df.iloc[i[0]]['_id'] for i in top_n_recs]
        return item_ids
    
    def get_recommendations_for_user(self, user_id, k=20):
        # Get the user's information in the database
        user = db['users'].find_one({'_id': user_id})
        # Get the user's viewed articles
        viewed_articles = user['viewed_articles']
        if len(viewed_articles) == 0:
            # If the user has not viewed any articles, return the random recommendations matched with the user's favorite category
            categories = user['favorite_categories']
            recs = self.df[self.df['category'].isin(categories)].sample(k)
            return recs['_id'].tolist()
        else:
            # Get the recommendations based on the user's last viewed article
            last_viewed_article = viewed_articles[-1]
            return self.get_recommendations_from_item(last_viewed_article, k)
        
# Test the recommender
test_article_id = ObjectId('664b5e8dafb7d3388d076445')
rec = Recommender()
print(rec.get_recommendations_from_item(test_article_id))