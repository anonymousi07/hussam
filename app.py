import streamlit as st
import pandas as pd
import pickle
import requests


# Load similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))


# Fetch poster from TMDB
def fetch_poster(movie_id):
    api_key = "d21d321557ddab64329ebac3d5de4214"  # Replace with your TMDB API key
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:  # Check for successful response
        data = response.json()
        poster_path = data.get('poster_path')  # Safely get the poster_path
        if poster_path:
            return f"http://image.tmdb.org/t/p/w500/{poster_path}"  # TMDB image URL
    return "https://via.placeholder.com/500x750?text=No+Poster+Available"  # Fallback image


# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].id  # Get the movie ID
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


# Load movie data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Streamlit UI
st.title('Movie Recommender System')

# Movie selection dropdown
selected_movie_name = st.selectbox(
    'Select a movie:',
    movies['title'].values
)

# Recommendation button
if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    # Display recommendations in columns
    cols = st.columns(5)  # Adjust column count for better layout
    for col, name, poster in zip(cols, names, posters):
        with col:
            st.text(name)
            st.image(poster)  # Display poster
