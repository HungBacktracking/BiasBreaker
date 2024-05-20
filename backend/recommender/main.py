import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from ..database.database import db

class BaseRecommender():
    def get_recommendations_from_item(self, item_id, k=10):
        """
        Get the top n recommendations for the given item_id
        
        Args:
            item_id (str): The item id to get the recommendations
            top_n (int): The number of recommendations to return
        
        Returns:
            list: The list of recommended items
        """
        # Get the item's index
        item_idx = self.df[self.df['id']==item_id].index[0]
        # Get the similarity scores
        sim_scores = list(enumerate(self.cosine_sim[item_idx]))
        # Sort the items based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        # Get the top n recommendations
        top_n_recs = sim_scores[1:k+1]
        # Get the item ids
        item_ids = [self.df.iloc[i[0]]['id'] for i in top_n_recs]
        return item_ids

class Recommender(BaseRecommender):
    def __init__(self):
        # Load the articles from the database
        self.articles = self._load_articles()
        self.df = pd.DataFrame(self.articles)
        # Keep the article id, category, title, content, and keywords
        self.df = self.df[['id', 'category', 'title', 'content', 'keywords']] 
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
        self.cosine_sim_df = pd.DataFrame(self.cosine_sim, index=self.df['id'], columns=self.df['id'])