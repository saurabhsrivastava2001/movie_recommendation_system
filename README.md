# check the deployed model please click here
## [movie recommendation system by saurabh Srivastava]([https://streamlit.io/](https://huggingface.co/spaces/saurabhSriv2001/movie_recommendation_system_with_more_features ))

# 🎮 Movie Recommender System  

A powerful **Movie Recommender System** built with **Streamlit**, **TMDb API**, and **Machine Learning**.  
Find the best movie recommendations based on your preferences, trending movies, genres, moods, and latest releases!  

---

## 🚀 Features  

### 🔹 Main Features  
- **🎥 Movie-Based Recommendations**: Get personalized recommendations based on your selected movie.  
- **🔥 Trending Movies** *(Dynamic Section)*: View the latest trending movies from **TMDb API**.  
- **🎭 Genre-Based Recommendations** *(Dynamic Section)*: Find movies based on selected genres.  
- **😊 Mood-Based Recommendations** *(Dynamic Section)*: Get movie suggestions based on your mood (Happy, Sad, Exciting, etc.).  
- **🔟 New Releases** *(Dynamic Section)*: Stay updated with the **latest movie releases**, including release dates.  

### 🔹 Optimized UI & Performance  
- **Button-Triggered Sections**: Secondary features only load when clicked (keeping UI clean).  
- **Optimized API Calls**: Handles errors gracefully, preventing crashes due to API failures.  
- **Fast & Responsive**: Lightweight and easy to use.  

---

## 🛠 Tech Stack  

- **Frontend**: [Streamlit](https://streamlit.io/)  
- **Backend**: Python, Pandas, Pickle  
- **Machine Learning**: Cosine Similarity for recommendations  
- **APIs**: [TMDb API](https://www.themoviedb.org/documentation/api) for movie data & posters  

---

## 💽 Installation & Setup  

### 🔹 1. Clone the Repository  
```sh
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
```

### 🔹 2. Create a Virtual Environment  
```sh
# For Windows
python -m venv env
env\Scripts\activate

# For Mac/Linux
python3 -m venv env
source env/bin/activate
```

### 🔹 3. Install Dependencies  
```sh
pip install -r requirements.txt
```

---

## 💽 Handling Large Model Files (`.pkl`)  

Since the **model files are too large**, they are **not directly included in GitHub**. You must **download them manually or automate the process**.

### **Option 1: Download Model from Google Drive (Recommended)**
1. **Manually download the model files** from Google Drive:  
   - 💽 [movie_list.pkl](YOUR_GOOGLE_DRIVE_LINK_1)  
   - 💽 [similarity.pkl](YOUR_GOOGLE_DRIVE_LINK_2)  
2. **Place them inside the `model/` directory** in your project folder.  

OR  

### **Option 2: Automatically Download Model Files**  
Modify `utils.py` to **automatically download** the model before running the project:

```python
import gdown
import os
import pickle

def download_model():
    """Downloads the model files from Google Drive if not present."""
    files = {
        "movie_list.pkl": "YOUR_GOOGLE_DRIVE_FILE_ID_1",
        "similarity.pkl": "YOUR_GOOGLE_DRIVE_FILE_ID_2",
    }

    if not os.path.exists("model"):
        os.makedirs("model")

    for file, file_id in files.items():
        if not os.path.exists(f"model/{file}"):
            print(f"Downloading {file}...")
            gdown.download(f"https://drive.google.com/uc?id={file_id}", f"model/{file}", quiet=False)

def load_model():
    """Loads the recommendation model after downloading it if necessary."""
    download_model()
    movies = pickle.load(open("model/movie_list.pkl", "rb"))
    similarity = pickle.load(open("model/similarity.pkl", "rb"))
    return movies, similarity
```
🔹 **Replace** `"YOUR_GOOGLE_DRIVE_FILE_ID_1"` and `"YOUR_GOOGLE_DRIVE_FILE_ID_2"` with the actual file IDs from Google Drive.

---

## 🔥 Running the Application  
```sh
streamlit run app.py
```

The app will run locally at **[http://localhost:8501](http://localhost:8501)**  

---

## 🎥 Usage Guide  

1️⃣ **Select a movie** from the dropdown and click **"Show Recommendations"**  
2️⃣ Click **buttons** to explore:
   - 🔥 **Trending Movies**  
   - 🎭 **Genre-Based Movies**  
   - 😊 **Mood-Based Movies**  
   - 🔟 **New Releases**  
3️⃣ **Enjoy the best movie suggestions tailored for you!**  

---

## 🔐 API & Dataset Details  

- Uses **The Movie Database (TMDb) API** to fetch movie posters and details.  
- **Movie dataset** is preprocessed and stored in `model/movie_list.pkl` and `model/similarity.pkl`.  
- Machine Learning model is based on **Cosine Similarity** for finding similar movies.  

---

## 🖼 Screenshots  

_Add screenshots of your app interface here._  

Example:  
![Movie Recommender Screenshot](https://via.placeholder.com/800x400.png?text=Add+Your+Screenshot+Here)  

---

## 🔮 Future Enhancements  

✔ **User-Based Collaborative Filtering** (Personalized recommendations based on user behavior)  
✔ **User Authentication** (Save favorite movies & history)  
✔ **Movie Ratings & Reviews** (Users can rate movies)  
✔ **Multi-Language Support**  

---

## 🤝 Contributing  

Want to improve this project? Contributions are welcome!  

1. **Fork the repository**  
2. **Create a new branch** (`feature-branch`)  
3. **Commit your changes**  
4. **Push to GitHub & open a PR**  

---

## 📝 License  

This project is licensed under the **MIT License**.  

---

## 📩 Contact & Support  

For any issues or suggestions, feel free to contact:  
📧 **your-email@example.com**  
💻 **GitHub**: [Your GitHub Profile](https://github.com/your-username)  

---
🎮 **Enjoy your personalized movie recommendations!** 🍿  
