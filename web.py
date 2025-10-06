# import streamlit as st
# import pickle
# import pandas as pd
# import requests

# def fetch_poster(movie_id):
#     """Fetches the movie poster from the TMDB API."""
#     try:
#         response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY&language=en-US')
#         response.raise_for_status()
#         data = response.json()
#         poster_path = data.get('poster_path')
#         if poster_path:
#             return "https://image.tmdb.org/t/p/w500/" + poster_path
#         else:
#             return "https://via.placeholder.com/500x750.png?text=No+Poster"
#     except requests.exceptions.RequestException as e:
#         st.error(f"API request failed: {e}")
#         return "https://via.placeholder.com/500x750.png?text=API+Error"

# def recommend(movie):
#     """Recommends 5 similar movies."""
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
#     recommended_movies = []
#     recommended_movies_posters = []
#     for i in movies_list:
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movies.append(movies.iloc[i[0]].title)
#         recommended_movies_posters.append(fetch_poster(movie_id))
#     return recommended_movies, recommended_movies_posters

# # Load the data and similarity matrix
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
# similarity = pickle.load(open('similarity.pkl', 'rb'))

# # App layout
# st.title('Movie Recommender System')

# selected_movie_name = st.selectbox(
#     'Select a movie you like to get recommendations:',
#     movies['title'].values
# )

# if st.button('Recommend'):
#     st.write("Here are some movies you might like:")
#     names, posters = recommend(selected_movie_name)
    
#     cols = st.columns(5)
#     for i in range(5):
#         with cols[i]:
#             st.text(names[i])
#             st.image(posters[i])

# import streamlit as st
# import pickle
# import pandas as pd
# import requests
# import os
# import json
# from datetime import datetime
# import time

# # Initialize usage tracking
# USAGE_FILE = "app_usage.json"

# def init_usage_tracking():
#     """Initialize the usage tracking file"""
#     if not os.path.exists(USAGE_FILE):
#         base_data = {
#             "total_recommendations": 0,
#             "unique_movies_searched": set(),
#             "sessions": [],
#             "first_used": datetime.now().isoformat(),
#             "last_updated": datetime.now().isoformat()
#         }
#         save_usage_data(base_data)

# def load_usage_data():
#     """Load usage data from file"""
#     try:
#         with open(USAGE_FILE, 'r') as f:
#             data = json.load(f)
#             # Convert set back from list
#             data['unique_movies_searched'] = set(data['unique_movies_searched'])
#             return data
#     except:
#         return None

# def save_usage_data(data):
#     """Save usage data to file"""
#     try:
#         # Convert set to list for JSON serialization
#         data_copy = data.copy()
#         data_copy['unique_movies_searched'] = list(data['unique_movies_searched'])
#         data_copy['last_updated'] = datetime.now().isoformat()
        
#         with open(USAGE_FILE, 'w') as f:
#             json.dump(data_copy, f, indent=2)
#     except Exception as e:
#         print(f"Error saving usage data: {e}")

# def track_recommendation(movie_name):
#     """Track each recommendation request"""
#     init_usage_tracking()
#     data = load_usage_data()
    
#     if data:
#         data['total_recommendations'] += 1
#         data['unique_movies_searched'].add(movie_name)
        
#         # Track this session
#         session_data = {
#             "timestamp": datetime.now().isoformat(),
#             "movie_searched": movie_name,
#             "session_id": str(hash(str(time.time())))
#         }
#         data['sessions'].append(session_data)
        
#         # Keep only last 100 sessions to avoid file getting too big
#         if len(data['sessions']) > 100:
#             data['sessions'] = data['sessions'][-100:]
        
#         save_usage_data(data)

# def show_usage_stats():
#     """Display usage statistics in the app"""
#     data = load_usage_data()
    
#     if data:
#         st.sidebar.markdown("---")
#         st.sidebar.subheader("📊 Local App Analytics")
        
#         col1, col2 = st.sidebar.columns(2)
        
#         with col1:
#             st.metric("Total Recommendations", data['total_recommendations'])
        
#         with col2:
#             st.metric("Movies Searched", len(data['unique_movies_searched']))
        
#         # Show recent activity
#         if data['sessions']:
#             st.sidebar.write("**Recent Searches:**")
#             recent_searches = data['sessions'][-5:]  # Last 5 searches
#             for session in reversed(recent_searches):
#                 time_str = datetime.fromisoformat(session['timestamp']).strftime("%H:%M")
#                 st.sidebar.write(f"• {session['movie_searched']} ({time_str})")

# # Your existing functions (keep these the same)
# def fetch_poster(movie_id):
#     API_KEY = os.getenv('TMDB_API_KEY', 'YOUR_API_KEY_HERE')
#     if API_KEY == 'YOUR_API_KEY_HERE':
#         return "https://via.placeholder.com/500x750.png?text=API+Key+Required"
    
#     try:
#         response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US')
#         response.raise_for_status()
#         data = response.json()
#         poster_path = data.get('poster_path')
#         if poster_path:
#             return "https://image.tmdb.org/t/p/w500/" + poster_path
#         else:
#             return "https://via.placeholder.com/500x750.png?text=No+Poster"
#     except:
#         return "https://via.placeholder.com/500x750.png?text=API+Error"

# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
#     recommended_movies = []
#     recommended_movies_posters = []
#     for i in movies_list:
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movies.append(movies.iloc[i[0]].title)
#         recommended_movies_posters.append(fetch_poster(movie_id))
#     return recommended_movies, recommended_movies_posters

# # Load your data
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)


# # Initialize usage tracking
# init_usage_tracking()

# # App layout
# st.title('🎬 Movie Recommender System')

# selected_movie_name = st.selectbox(
#     'Select a movie you like to get recommendations:',
#     movies['title'].values
# )

# if st.button('Recommend'):
#     # Track this recommendation
#     track_recommendation(selected_movie_name)
    
#     st.write("Here are some movies you might like:")
#     names, posters = recommend(selected_movie_name)
    
#     cols = st.columns(5)
#     for i in range(5):
#         with cols[i]:
#             st.text(names[i])
#             st.image(posters[i])

# # Show usage statistics
# show_usage_stats()

# # Add a button to view detailed analytics
# if st.sidebar.button("View Detailed Analytics"):
#     data = load_usage_data()
#     if data:
#         st.sidebar.markdown("---")
#         st.sidebar.subheader("Detailed Statistics")
#         st.sidebar.write(f"First used: {datetime.fromisoformat(data['first_used']).strftime('%Y-%m-%d %H:%M')}")
#         st.sidebar.write(f"Last updated: {datetime.fromisoformat(data['last_updated']).strftime('%Y-%m-%d %H:%M')}")
#         st.sidebar.write(f"Total sessions: {len(data['sessions'])}")

import streamlit as st
import pickle
import pandas as pd
import requests

# Function to fetch movie poster from TMDB API
# NOTE: This key is for demonstration. You should get your own free key from themoviedb.org
def fetch_poster(movie_id):
    try:
        api_key = "8265bd1679663a7ea12ac168da84d2e8"
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
        response = requests.get(url)
        response.raise_for_status()  # Checks for HTTP errors
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/500x750.png?text=No+Poster"
    except requests.exceptions.RequestException:
        return "https://via.placeholder.com/500x750.png?text=API+Error"

# Function to get movie recommendations
def recommend(movie, movies_df, similarity_matrix):
    # Get the index of the selected movie from the dataframe
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    
    # Get the similarity scores for that movie against all other movies
    distances = similarity_matrix[movie_index]
    
    # Sort the movies by similarity score in descending order and get the top 5
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    # Prepare lists to hold the names and posters of recommended movies
    recommended_movies_names = []
    recommended_movies_posters = []
    for i in movies_list:
        # Get movie details by index
        movie_id = movies_df.iloc[i[0]].movie_id
        movie_title = movies_df.iloc[i[0]].title
        
        # Add the movie title and poster to our lists
        recommended_movies_names.append(movie_title)
        recommended_movies_posters.append(fetch_poster(movie_id))
        
    return recommended_movies_names, recommended_movies_posters

# --- Main App Execution ---

# Load the data files
try:
    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    
    # This was the missing line that caused the original error
    similarity = pickle.load(open('similarity.pkl', 'rb'))
except FileNotFoundError:
    st.error("🚨 Error: Make sure 'movie_dict.pkl' and 'similarity.pkl' are in your GitHub repository.")
    st.stop() # Stop the app from running further if files are missing

# App Title
st.title('🎬 Movie Recommender System')

# Movie selection dropdown
selected_movie_name = st.selectbox(
    'Select a movie you like to get recommendations:',
    movies['title'].values
)

# Recommend button
if st.button('Recommend'):
    with st.spinner('Finding recommendations for you...'):
        # Call the recommend function and pass the required data
        names, posters = recommend(selected_movie_name, movies, similarity)
        
        st.write("Here are some movies you might like:")
        
        # Display the 5 recommendations in 5 columns
        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.text(names[i])
                st.image(posters[i])
