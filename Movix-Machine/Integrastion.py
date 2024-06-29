from flask import Flask, jsonify
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(app)

# Load ratings from database
rating = pd.read_sql_query("SELECT * FROM rating", conn)

# Load movie metadata from API
movie_api_url = "https://api.themoviedb.org/3/movie/{movie_id}?api_key=3d39d6bfe362592e6aa293f01fbcf9b9"
movie_metadata = {}
for movie_id in rating.movieId.unique():
    response = requests.get(movie_api_url.format(movie_id=movie_id))
    movie_metadata[movie_id] = response.json()

# Compute user-user similarity matrix
user_similarity = cosine_similarity(user_item_matrix)

# Initialize kNN model
knn_model = NearestNeighbors(metric='cosine', algorithm='brute')
knn_model.fit(user_similarity)

@app.route('/recommendations/<int:user_id>', methods=['GET'])
def recommend_movies(user_id):
    # Find top-k similar users
    distances, indices = knn_model.kneighbors(user_similarity[user_id], n_neighbors=10+1)
    # Get the movie ratings of similar users
    similar_user_ratings = user_item_matrix.iloc[indices[0][1:]]

    # Predict ratings for unseen movies
    predicted_ratings = similar_user_ratings.mean(axis=0)

    # Generate top-n recommendations
    recommended_movies = predicted_ratings.nlargest(10).index.tolist()

    return jsonify({'recommended_movies': recommended_movies})

if __name__ == 'app':
    app.run(debug=True)