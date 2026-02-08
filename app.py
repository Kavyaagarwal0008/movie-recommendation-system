from flask import Flask, render_template, request
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

app = Flask(__name__)

# ✅ Load movies
movies = pd.read_csv("movies.csv")
movies["title"] = movies["title"].fillna("")
movies["genres"] = movies["genres"].fillna("")

# ✅ Build TF-IDF ONE TIME (on server start)
tfidf = TfidfVectorizer(stop_words="english", max_features=8000)
tfidf_matrix = tfidf.fit_transform(movies["genres"])

# ✅ mapping title -> index (fast)
title_to_index = pd.Series(movies.index, index=movies["title"]).drop_duplicates()

def recommend(movie_title, top_n=5):
    if movie_title not in title_to_index:
        return []

    idx = title_to_index[movie_title]

    # ✅ compute similarity only for that movie row (fast & low memory)
    cosine_sim = linear_kernel(tfidf_matrix[idx], tfidf_matrix).flatten()

    # get top results excluding itself
    sim_scores = cosine_sim.argsort()[-(top_n + 1):][::-1]
    sim_scores = [i for i in sim_scores if i != idx][:top_n]

    return movies["title"].iloc[sim_scores].tolist()

@app.route("/", methods=["GET", "POST"])
def index():
    recs = []
    selected_movie = movies["title"].iloc[0] if len(movies) else ""

    if request.method == "POST":
        selected_movie = request.form.get("movie", selected_movie)
        recs = recommend(selected_movie)

    return render_template(
        "index.html",
        movie_list=movies["title"].values,
        recommendations=recs,
        selected_movie=selected_movie
    )

if __name__ == "__main__":
    app.run()
