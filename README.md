🎬 Movie Recommendation System

A complete Machine Learning + Flask Web Application that recommends movies to users based on content similarity using TF-IDF Vectorization and Cosine Similarity.

This system analyzes movie genres and suggests 5 similar movies to the one selected by the user.

🔗 Live Demo

👉 (Add your Render link here after deployment)

📌 Features

Recommend movies based on content similarity

Searchable movie input (no long dropdown)

Clean and modern UI with HTML & CSS

Flask backend with ML model

Automatic model generation during deployment

Fully deployable on Render

🛠️ Tech Stack
Programming & Libraries

Python

Flask

Pandas

Scikit-learn

Pickle

Frontend

HTML5

CSS3

Deployment & Tools

Git & GitHub

Render (Cloud Deployment)

📂 Project Structure
movie-recommendation-system/
│
├── app.py                # Flask application
├── train_model.py        # Model training script
├── movies.csv            # Dataset
├── requirements.txt      # Dependencies
├── Procfile              # Render config
├── .gitignore
│
├── templates/
│   └── index.html        # UI
│
├── static/
│   └── style.css         # Styling


.pkl files are not pushed to GitHub. They are generated automatically during deployment.

⚙️ How It Works

Dataset of movies with genres is loaded

Genres are converted into TF-IDF vectors

Cosine similarity is calculated between movies

User selects a movie

System recommends 5 most similar movies

▶️ Run Locally
1️⃣ Clone repository
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system

2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Generate model files
python train_model.py

5️⃣ Run Flask app
python app.py


Open: http://127.0.0.1:5000

🚀 Deployment on Render

Build Command

pip install -r requirements.txt && python train_model.py


Start Command

gunicorn app:app

📊 Machine Learning Technique Used

TF-IDF Vectorization

Cosine Similarity

Content-Based Filtering

🎯 Applications

OTT platforms (Netflix, Prime, Hotstar)

Movie streaming services

Personalized recommendation engines

💡 Viva / Interview Explanation (Short)

“This system uses TF-IDF vectorization and cosine similarity to recommend movies based on genre similarity, implemented with Flask and deployed on Render.”

👩‍💻 Author

Kavya Agarwal
B.Tech CSE-AIML Student | Machine Learning Enthusiast

🔗 GitHub: https://github.com/Kavyaagarwal0008
