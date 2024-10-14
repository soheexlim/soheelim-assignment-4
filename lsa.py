import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity

class LSA:
    def __init__(self, n_components=100):
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.svd = TruncatedSVD(n_components=n_components)
        self.documents = fetch_20newsgroups(subset='all')['data']
        self.doc_matrix = self.vectorizer.fit_transform(self.documents)
        self.reduced_matrix = self.svd.fit_transform(self.doc_matrix)

    def query(self, user_query):
        query_vector = self.vectorizer.transform([user_query])
        query_reduced = self.svd.transform(query_vector)
        similarities = cosine_similarity(query_reduced, self.reduced_matrix).flatten()
        top_indices = similarities.argsort()[-5:][::-1]
        return [(self.documents[i], similarities[i]) for i in top_indices]
