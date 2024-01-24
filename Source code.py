class MovieRecommendationSystem:
    def __init__(self):
        # Example movie data: {movie_id: [title, genre]}
        self.movies = {
            1: ["Movie1", "Action"],
            2: ["Movie2", "Comedy"],
            3: ["Movie3", "Drama"],
            # Add more movies as needed
        }
        # Example user ratings data: {user_id: {movie_id: rating}}
        self.user_ratings = {
            101: {1: 4, 2: 3, 3: 5},
            102: {1: 5, 2: 2, 3: 4},
            # Add more user ratings as needed
        }

    def recommend_movies(self, user_id, num_recommendations=3):
        # Get movies not yet rated by the user
        unrated_movies = [movie_id for movie_id in self.movies if movie_id not in self.user_ratings.get(user_id, {})]

        # Calculate movie scores based on user ratings
        movie_scores = {movie_id: self.calculate_movie_score(user_id, movie_id) for movie_id in unrated_movies}

        # Sort movies by scores and get top recommendations
        recommended_movies = sorted(movie_scores, key=movie_scores.get, reverse=True)[:num_recommendations]

        return [(movie_id, self.movies[movie_id][0]) for movie_id in recommended_movies]

    def calculate_movie_score(self, user_id, movie_id):
        # Simple collaborative filtering: Calculate the average rating of similar users
        similar_users = [other_user_id for other_user_id in self.user_ratings if movie_id in self.user_ratings[other_user_id]]
        if not similar_users:
            return 0  # No similar users

        total_score = sum(self.user_ratings[other_user_id][movie_id] for other_user_id in similar_users)
        average_score = total_score / len(similar_users)
        return average_score

# Example usage:
movie_system = MovieRecommendationSystem()
user_id_to_recommend = 103

recommendations = movie_system.recommend_movies(user_id_to_recommend)
print(f"Recommended movies for User {user_id_to_recommend}: {recommendations}")
