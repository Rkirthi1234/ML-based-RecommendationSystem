import streamlit as st
import pickle
import pandas as pd
import requests

# fetching movie poster function
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=9ddbde1dfd26fe1a81974fc9bc138fe7&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))  # rb = read binary
movies = pd.DataFrame(movies_dict) 
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title(' Movie Recommendation System')
selected_movie_name = st.selectbox(
    'Which movie u want to search?',
    movies['title'].values
)

# same commands is being used which u used in the jupyter-Notebook
def recommend_func(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id  
        recommended_movies.append(movies['title'][i[0]])
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


if st.button('Recommend'):
    # st.write('Selected movie name: ', selected_movie_name)
    recommendations_five_movies, posters = recommend_func(selected_movie_name)

    st.write("      ")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(posters[0])
        st.text(recommendations_five_movies[0])

    with col2:
        st.image(posters[1])
        st.text(recommendations_five_movies[1])

    with col3:    
        st.image(posters[2])
        st.text(recommendations_five_movies[2])

    with col4:
        st.image(posters[3])
        st.text(recommendations_five_movies[3])

    with col5:
        st.image(posters[4])
        st.text(recommendations_five_movies[4])