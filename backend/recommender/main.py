import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import NMF
from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId
import config

uri = "mongodb+srv://{}:{}@cluster0.izgloib.mongodb.net".format(config.USER, config.PASSWORD)
db = MongoClient(uri)['BiasBreakerDatabase']

class Recommender(object):
    def __init__(self):
        self.articles = self._load_articles()
        self.df = pd.DataFrame(self.articles)
        self.df = self.df[['_id', 'category', 'title', 'content', 'keywords']] 
        self._create_vectorizer()
        self._compute_similarity()
    
    def _load_articles(self):
        articles = []
        for article in db['articles'].find():
            articles.append(article)
        return articles
    
    def _create_vectorizer(self):
        # Combine content and keywords into a single string for each article
        self.df['combined'] = self.df.apply(lambda row: row['content'] + " " + " ".join(row['keywords']) + " " + row['category'], axis=1)
        
        # Create a TfidfVectorizer
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['combined'])
        
    def _compute_similarity(self):
        # Compute the cosine similarity matrix
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)
        # self.cosine_sim_df = pd.DataFrame(self.cosine_sim, index=self.df['_id'], columns=self.df['_id'])

    def get_recommendations_from_item(self, item_id, k=20):
        """
        Get recommendations based on a given item.

        Args:
            item_id (any): The ID of the item to get recommendations for.
            k (int, optional): The number of recommendations to return. Defaults to 20.

        Returns:
            list: A list of item IDs representing the top recommendations.
        """
        item_idx = self.df[self.df['_id'] == item_id].index[0]
        sim_scores = list(enumerate(self.cosine_sim[item_idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        top_n_recs = sim_scores[1:k+1]
        item_ids = [self.df.iloc[i[0]]['_id'] for i in top_n_recs]
        return item_ids
    
    def get_recommendations_for_user(self, user_id, k=20):
        """
        Get recommendations for a user based on their viewing history and favorite categories.

        Args:
            user_id (str): The ID of the user.
            k (int, optional): The number of recommendations to return. Defaults to 20.

        Returns:
            list: A list of recommended article IDs.
        """
        user = db['users'].find_one({'_id': user_id})
        viewed_articles = user['viewed_articles']
        if len(viewed_articles) == 0:
            categories = user['favorite_categories']
            recs = self.df[self.df['category'].isin(categories)].sample(k)
            return recs['_id'].tolist()
        else:
            last_viewed_article = viewed_articles[-1]
            return self.get_recommendations_from_item(last_viewed_article, k)
        

class HybridRecommender(Recommender):
    def __init__(self):
        super().__init__()
        self.user_item_matrix = self._create_user_item_matrix()
        self.nmf_model = self._fit_nmf_model()
    
    def _create_user_item_matrix(self):
        users = db['users'].find()
        user_ids = []
        article_ids = list(self.df['_id'])
        data = []
        for user in users:
            user_ids.append(user['_id'])
            user_data = [0] * len(article_ids)
            for article_id in user['viewed_articles']:
                article_idx = article_ids.index(article_id)
                user_data[article_idx] += 1  # Increment the count for each view
            data.append(user_data)
        return pd.DataFrame(data, index=user_ids, columns=article_ids)
    
    def _fit_nmf_model(self):
        nmf = NMF(n_components=20, random_state=1)
        nmf.fit(self.user_item_matrix)
        return nmf
    
    def get_collaborative_recommendations(self, user_id, k=10):
        user_index = self.user_item_matrix.index.get_loc(user_id)
        user_vector = self.nmf_model.transform(self.user_item_matrix.iloc[user_index].values.reshape(1, -1))
        user_item_scores = np.dot(user_vector, self.nmf_model.components_)
        top_indices = np.argsort(user_item_scores[0])[::-1][:k]
        top_article_ids = self.user_item_matrix.columns[top_indices]
        return top_article_ids.tolist()
    
    def get_recommendations_for_user(self, user_id, k=20):
        user = db['users'].find_one({'_id': user_id})
        if not user:
            return []
        viewed_articles = user.get('viewed_articles', [])
        if not viewed_articles:
            categories = user.get('favorite_categories', [])
            recs = self.df[self.df['category'].isin(categories)].sample(k)
            return recs['_id'].tolist()
        
        last_viewed_article = viewed_articles[-1]
        content_recs = set(self.get_recommendations_from_item(last_viewed_article, k=k//2))
        collab_recs = set(self.get_collaborative_recommendations(user_id, k=k//2))
        recommendations = list(content_recs.union(collab_recs))[:k]
        return recommendations        
        
# Test the recommender
test_article_id = ObjectId('664b5e8dafb7d3388d076445')
rec = Recommender()
print(rec.get_recommendations_from_item(test_article_id))