# ML-based-Recommendation_System
This project is a Streamlit-based Movie Recommendation System that suggests 5 similar movies for a selected title, along with their posters, using content-based filtering and The Movie Database (TMDB API) for fetching movie posters.

# Features
Search for a movie title from a pre-loaded dataset.

Get 5 movie recommendations based on similarity.

Display of movie posters for better user experience.

Interactive UI built with Streamlit.

# Tech Stack
Python 3

Streamlit (UI Framework)

Pandas (Data handling)

Pickle (Pre-saved model/data loading)

Requests (API calls to TMDB)

TMDB API (Fetching movie posters)

# How to Run

- Clone the Repository:
  
  git clone <your-repo-url>

  cd movie-recommendation

- Install Dependencies
  
  Make sure you have Python 3.9+ installed, then run:
  
  pip install streamlit pandas requests

- Add Required Files
  Ensure you have the following files in the same directory:

  movie_dict.pkl

  similarity.pkl
  
  These contain the movie data and precomputed similarity matrix.

- Run the App
  
  streamlit run app.py

The app will open in your default browser.

# API Key Setup
This app uses the TMDB API. The API key is already in app.py, but for security in production:
- Create a free account on TMDB.
- Generate an API key.
- Store it in an environment variable:
  
  export TMDB_API_KEY='your_api_key'
- Replace the API key usage in app.py with:
  
  import os
  api_key = os.getenv("TMDB_API_KEY")


# Project output:
https://github.com/Rkirthi1234/ML-based-Recommendation_System/blob/main/demo.mp4

# Future Enhancements
Add search by genre, actor, or director.

Include collaborative filtering for personalized recommendations.

Deploy on Streamlit Cloud or Heroku for public access.
