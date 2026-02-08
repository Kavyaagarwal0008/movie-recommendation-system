# 🚗 Movie Recommendtion System

A complete **Machine Learning + Flask Web Application** that recommends movies to users based on content similarity using **TF-IDF Vectorization and Cosine Similarity**.

This system analyzes movie genres and suggests **5 similar movies** to the one selected by the user.

---

## 🔗 Live Demo

👉 **Live Application:** https://movie-recommendation-system-y3u3.onrender.com

---

## 📌 Features
* Recommend movies based on content similarity
* Searchable movie input (no long dropdown)
* Clean and modern UI with HTML & CSS
* Flask backend with ML model
* Automatic model generation during deployment
* Fully deployable on Render

---

## 🛠️ Tech Stack

### Programming & Libraries

* Python
* Flask
* Pandas
* Scikit-learn
* Pickle

### Frontend

* HTML5
* CSS3

### Deployment & Tools

* Git & GitHub
* Render (Cloud Deployment)

---

## 📂 Project Structure

```
movie-recommendation-system/
│
├── app.py                # Flask application
├── train_model.py        # Model training script
├── requirements.txt      # Dependencies
├── Procfile              # Render deployment config
├── movies.csv            # Dataset
├── .gitignore           
├── templates/
│   └── index.html        # Main UI
│
├── static/
│   └── style.css         # Styling
│
└── README.md
```

---

## ⚙️ How It Works

1. Dataset of movies with genres is loaded
2. Genres are converted into TF-IDF vectors
3. Cosine similarity is calculated between movies
4. User selects a movie
5. System recommends 5 most similar movies

---

## ▶️ Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Kavyaagarwal0008/movie-recommendation-system.git
cd movie-recommendations system
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```
### 4️⃣ Generate model files
```bash
python train_model.py
```
### 5️⃣ Run the application

```bash
python app.py
```

Visit: **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

## 📊 Machine Learning Models Used

* TF-IDF Vectorization
* Cosine Similarity
* Content-Based Filtering

---

## 🎯 Applications

* OTT platforms (Netflix, Prime, Hotstar)
* Movie streaming services
* Personalized recommendation engines

---

## 👩‍💻 Author

**Kavya Agarwal**
B.Tech CSE-AIML Student | Machine Learning Enthusiast

🔗 GitHub: [https://github.com/Kavyaagarwal0008](https://github.com/Kavyaagarwal0008)

---

⭐ If you like this project, don’t forget to **star the repository**!
