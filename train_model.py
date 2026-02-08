import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv("movies.csv")

# Combine important features
movies['genres'] = movies['genres'].fillna('')

# TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genres'])

# Cosine similarity
similarity = cosine_similarity(tfidf_matrix)

# Save models
pickle.dump(movies, open("movies.pkl", "wb"))
pickle.dump(similarity, open("similarity.pkl", "wb"))

print("✅ Model training completed")
