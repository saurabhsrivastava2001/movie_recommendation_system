import streamlit as st
from utils import (
    load_model, recommend, get_trending_movies, get_new_releases, get_movies_by_genre, get_mood_based_movies
)

# Set page title and layout
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")

# Load model
movies, similarity = load_model()

st.title("🎬 Movie Recommender System")
st.markdown("##### Discover your next favorite movie!")

# --- UI State Variables (To Ensure Only One Section is Visible) ---
sections = ["recommend", "trending", "genre", "mood", "new_releases"]
for section in sections:
    if section not in st.session_state:
        st.session_state[section] = False

def reset_sections(except_section):
    """Resets all sections except the one currently clicked."""
    for section in sections:
        st.session_state[section] = (section == except_section)

# --- MOVIE RECOMMENDER SYSTEM (Main Feature) ---
if movies is None or similarity is None:
    st.error("⚠️ Error loading the recommendation model. Please check the backend.")
else:
    st.markdown("### 🔍 Find Your Next Favorite Movie")
    movie_list = movies['title'].values
    selected_movie = st.selectbox("🎥 Select a movie:", movie_list)

    if st.button("🔄 Show Recommendations"):
        reset_sections("recommend")
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie, movies, similarity)
        if recommended_movie_names:
            st.markdown("#### 🎯 Recommended Movies")
            cols = st.columns(5)
            for i, (name, poster) in enumerate(zip(recommended_movie_names, recommended_movie_posters)):
                with cols[i]:
                    st.image(poster, caption=name, use_container_width=True)
        else:
            st.warning("❌ No recommendations found. Try another movie.")

st.markdown("---")

# ---- BUTTONS FOR ADDITIONAL FEATURES ----
col1, col2, col3, col4 = st.columns(4)

# --- TRENDING MOVIES ---
with col1:
    if st.button("🔥 Show Trending Movies"):
        reset_sections("trending")

if st.session_state.trending:
    trending_movies = get_trending_movies()
    st.markdown("### 🔥 Trending Movies")
    if trending_movies:
        cols = st.columns(5)
        for i, (name, poster) in enumerate(trending_movies):
            with cols[i]:
                st.image(poster, caption=name, use_container_width=True)
    else:
        st.warning("No trending movies available.")

# --- GENRE-BASED MOVIES ---
with col2:
    if st.button("🎭 Show Genre-Based Movies"):
        reset_sections("genre")

if st.session_state.genre:
    genres = {"Action": "28", "Comedy": "35", "Drama": "18", "Thriller": "53", "Romance": "10749"}
    selected_genre = st.selectbox("🎭 Select Genre:", list(genres.keys()))
    genre_movies = get_movies_by_genre(genres[selected_genre])
    
    st.markdown(f"### 🎭 {selected_genre} Movies")
    if genre_movies:
        cols = st.columns(5)
        for i, (name, poster) in enumerate(genre_movies):
            with cols[i]:
                st.image(poster, caption=name, use_container_width=True)
    else:
        st.warning("No movies found for this genre.")

# --- MOOD-BASED MOVIES ---
with col3:
    if st.button("😊 Show Mood-Based Movies"):
        reset_sections("mood")

if st.session_state.mood:
    mood = st.selectbox("😊 Select Mood:", ["Happy", "Sad", "Thriller", "Action", "Romantic"])
    mood_movies = get_mood_based_movies(mood)

    st.markdown(f"### 😊 {mood} Movies")
    if mood_movies:
        cols = st.columns(5)
        for i, (name, poster) in enumerate(mood_movies):
            with cols[i]:
                st.image(poster, caption=name, use_container_width=True)
    else:
        st.warning("No mood-based movies found.")

# --- NEW RELEASES ---
with col4:
    if st.button("🆕 Show New Releases"):
        reset_sections("new_releases")

if st.session_state.new_releases:
    new_movies = get_new_releases()
    st.markdown("### 🆕 New Releases")
    if new_movies:
        cols = st.columns(5)
        for i, (name, poster, date) in enumerate(new_movies):
            with cols[i]:
                st.image(poster, caption=f"{name}\n📅 Released: {date}", use_container_width=True)
    else:
        st.warning("No new releases available.")
