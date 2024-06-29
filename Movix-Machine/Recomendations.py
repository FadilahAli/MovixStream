import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import requests

# Load ratings from database
rating = pd.read_sql_query("SELECT * FROM ratings", conn)

# Load movie metadata from API
movie_api_url = "https://api.themoviedb.org/3/movie/{movie_id}?api_key=3d39d6bfe362592e6aa293f01fbcf9b9"
movie_metadata = {}
for movie_id in rating.movieId.unique():
    response = requests.get(movie_api_url.format(movie_id=movie_id))
    movie_metadata[movie_id] = response.json()

# Create a pivot table
table = pd.pivot_table(rating, index='userId', columns='movieId', values='rating').fillna(0)

# Calculate similarity between users
similarity = []
for r in table.values:
    calc = cosine_similarity(table.values[user].reshape(1,-1), r.reshape(1, -1))[0][0]
    similarity.append(calc)

# Get the most similar user
neirest_user = list_user[similarity.index(max(copy_similarity))]
similar_score = max(copy_similarity)

# Get movie IDs watched by the most similar user
movieId = rating[rating['userId'] == list_user[neirest_user]]['movieId'].tolist()

# Get movie titles and other metadata
movie_titles = [movie_metadata[movie_id]['title'] for movie_id in movieId]

# Print recommendations
print("Since you watched Twelve Monkeys (a.k.a. 12 Monkeys) (1995), you might also like:")
for title in movie_titles:
    print(title)