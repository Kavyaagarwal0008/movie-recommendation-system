from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

similarity = pickle.load(open("similarity.pkl", "rb"))

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend(movie):
    tfidf = TfidfVectorizer(stop_words='english')

    tfidf_matrix = tfidf.fit_transform(movies['genres'])

    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    idx = movies[movies['title'] == movie].index[0]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]

    movie_indices = [i[0] for i in sim_scores]

    return movies['title'].iloc[movie_indices].values

@app.route("/", methods=["GET", "POST"])
def index():
    recs = []
    selected_movie = None

    if request.method == "POST":
        selected_movie = request.form["movie"]
        recs = recommend(selected_movie)

    return render_template(
        "index.html",
        movie_list=movies["title"].values,
        recommendations=recs,
        selected_movie=selected_movie
    )

if __name__ == "__main__":
    app.run(debug=True)
