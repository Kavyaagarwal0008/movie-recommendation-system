from flask import Flask, render_template, request
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# ✅ Load dataset (make sure movies.csv exists in your repo)
movies = pd.read_csv("movies.csv")

# ✅ Ensure required columns exist
# If your dataset uses different column names, adjust here
# Example: "title" and "genres" must exist
movies["title"] = movies["title"].fillna("")
movies["genres"] = movies["genres"].fillna("")

def recommend(movie_title, movies_df):
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(movies_df["genres"])

    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Find index of selected movie
    idx_list = movies_df.index[movies_df["title"] == movie_title].tolist()
    if not idx_list:
        return []
    idx = idx_list[0]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]

    movie_indices = [i[0] for i in sim_scores]
    return movies_df["title"].iloc[movie_indices].tolist()

@app.route("/", methods=["GET", "POST"])
def index():
    recs = []
    selected_movie = movies["title"].iloc[0] if len(movies) > 0 else ""

    if request.method == "POST":
        selected_movie = request.form.get("movie")
        recs = recommend(selected_movie, movies)

    return render_template(
        "index.html",
        movie_list=movies["title"].values,
        recommendations=recs,
        selected_movie=selected_movie
    )

if __name__ == "__main__":
    app.run()
