from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

def recommend(movie):
    idx = movies[movies["title"] == movie].index[0]
    distances = similarity[idx]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [movies.iloc[i[0]].title for i in movie_list]

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
