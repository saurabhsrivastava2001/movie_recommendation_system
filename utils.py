import requests
import pickle

API_KEY = "b69da5f4487715930c78152e05e65ecd"

def fetch_poster(movie_id):
    """Fetch movie poster from TMDb API with error handling."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return f"https://image.tmdb.org/t/p/w500/{data['poster_path']}" if "poster_path" in data and data["poster_path"] else "https://via.placeholder.com/500x750.png?text=No+Image"
    except:
        return "https://via.placeholder.com/500x750.png?text=No+Image"

def load_model():
    """Load movie recommendation model."""
    try:
        movies = pickle.load(open("model/movie_list.pkl", "rb"))
        similarity = pickle.load(open("model/similarity.pkl", "rb"))
        return movies, similarity
    except:
        return None, None

def recommend(movie, movies, similarity):
    """Recommend movies based on similarity index."""
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movie_names = []
        recommended_movie_posters = []
        for i in distances[1:6]:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movie_posters.append(fetch_poster(movie_id))
            recommended_movie_names.append(movies.iloc[i[0]].title)
        return recommended_movie_names, recommended_movie_posters
    except:
        return [], []

def get_trending_movies():
    """Fetch trending movies from TMDb API."""
    url = f"https://api.themoviedb.org/3/trending/movie/week?api_key={API_KEY}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return [(movie["title"], fetch_poster(movie["id"])) for movie in data.get("results", [])[:5]]
    except:
        return []

def get_new_releases():
    """Fetch newly released movies from TMDb API."""
    url = f"https://api.themoviedb.org/3/movie/now_playing?api_key={API_KEY}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return [(movie["title"], fetch_poster(movie["id"]), movie.get("release_date", "Unknown")) for movie in data.get("results", [])[:5]]
    except:
        return []

def get_movies_by_genre(genre_id):
    """Fetch movies by genre from TMDb API."""
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&with_genres={genre_id}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return [(movie["title"], fetch_poster(movie["id"])) for movie in data.get("results", [])[:5]]
    except:
        return []

def get_mood_based_movies(mood):
    """Fetch movies based on mood categories."""
    mood_map = {"Happy": "35", "Sad": "18", "Thriller": "53", "Action": "28", "Romantic": "10749"}
    return get_movies_by_genre(mood_map.get(mood, "35"))
