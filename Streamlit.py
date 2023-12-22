import streamlit as st
import pickle
import pandas as pd


movie_list = pickle.load(open("movie.pkl", 'rb'))
movies = pd.DataFrame(movie_list)
similarity = pickle.load(open("similarity.pkl", 'rb'))


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    movie_similarity = sorted(enumerate(similarity[movie_index]), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie = []
    for i in movie_similarity:
        movies_id = movies.iloc[i[0]].id
        recommended_movie.append(movies.iloc[i[0]].title)
    return recommended_movie


st.title("Movie Recommender system")
selected_movie_name = st.selectbox('HOW DO YOU WANT TO BE RECOMMENDED?', movies['title'].values)
if st.button('Recommend'):
    recommendations= recommend(selected_movie_name)

    for i in recommendations:
        st.subheader(i)


















