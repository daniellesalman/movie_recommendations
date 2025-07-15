"""
This program is a system for movie recommendations.
"""
class User:
    def __init__(self, username):
        self.username = username
        self.movies = {}
        self.fav_genres = []

    def add_movies(self, movies):
        self.movies.update(movies)

    def add_fav_genres(self, genres):
        self.fav_genres.extend(genres)


def get_movies():
    """
    This function gets a list of movies from the user.
    :return: list of movies
    """
    movies = []
    movie = input('Enter a movie title (to finish, enter "end"): ')
    while not movie == 'end':
        movies.append(movie)
        movie = input('Enter a movie title (to finish, enter "end"): ')
    return movies

def get_ratings(movies):
    """
    This function gets a rating for each movie in a movie list from the user.
    :param movies: list of movies
    :return: dictionary of movies with ratings
    """
    ratings = {}
    for movie in movies:
        rating = input(f'Enter a movie rating (1-10) for "{movie}": ')
        ratings.update({movie: int(rating)})
    return ratings

def get_genres(ratings):
    """
    This function gets a genre for each movie in a movie list from the user.
    :param ratings: dictionary of movies with ratings
    :return: dictionary of movies with ratings and genres
    """
    for movie in ratings:
        genre = input(f'Enter a genre for "{movie}": ')
        ratings.update({movie: (ratings[movie], genre)})
    return ratings

def get_user_favs():
    """
    This function gets a list of favorite movie genres from the user.
    :return: list of genres
    """
    fav_genres = []
    genre = 'genre'
    while not genre == 'end':
        genre = input('Enter a favorite genre (to finish, enter "end"): ')
        if genre == 'end':
            break
        fav_genres.append(genre)
    return fav_genres

def recommend_movies(movie_genres, fav_genres):
    """
    This function recommends movies based on the user's favorite movie genres.
    :param movie_genres: dictionary of movies with ratings and genres
    :param fav_genres: user's favorite genres
    :return: dictionary of movie recommendations
    """
    recommended = {}
    for fav_genre in fav_genres:
        matching_movies = {movie: (rating, genre) for movie, (rating, genre) in movie_genres.items() if genre == fav_genre}
        if matching_movies:
            highest_rating = max(rating for rating, genre in matching_movies.values())
            for movie in matching_movies:
                if matching_movies[movie][0] == highest_rating:
                    recommended.update({movie: matching_movies[movie]})
    return recommended

def find_similar_users(target_user, all_users):
    """
    This function finds similar users based on the user's favorite movie genres.
    :param target_user: user to find similar users for
    :param all_users: dictionary of all users
    :return: list of similar users
    """
    similarities = []
    for user in all_users.values():
        if not user.username == target_user.username:
            common_movies = set(target_user.movies.keys()) & set(user.movies.keys())
            if common_movies:
                total_diff = 0
                for movie in common_movies:
                    rating1 = target_user.movies[movie][0]
                    rating2 = user.movies[movie][1]
                    total_diff += abs(rating1 - rating2)
                avg_diff = total_diff / len(common_movies)
                similarities.append((avg_diff, user))
    similarities.sort(key=lambda x: x[0])
    return [user for x, user in similarities]

def collaborative_recommendations(target_user, all_users):
    """
    This function finds recommendations from similar users.
    :param target_user: user to find similar movies for
    :param all_users: dictionary of all users
    :return: dictionary of recommendations
    """
    similar_users = find_similar_users(target_user, all_users)
    recommended = {}
    for similar_user in similar_users:
        for movie, (rating, genre) in similar_user.movies.items():
            if movie not in target_user.movies and rating >= 8:
                recommended.update({movie: (rating, genre)})
        if recommended:
            break
    return recommended

# Global users dictionary
users = {}

def main():
    username = input('Enter username: ')
    if username not in users:
        users.update({username: User(username)})
    user = users[username]

    movies = get_movies()
    print(movies)
    movie_ratings = get_ratings(movies)
    movie_data = get_genres(movie_ratings)
    user.add_movies(movie_data)

    # Print average, max, and min ratings:
    ratings = [value[0] for value in user.movies.values()]
    print(f'Average rating: \033[93m{sum(ratings) / len(ratings)}\033[0m')
    print(f'Max rating: \033[92m{max(ratings)}\033[0m')
    print(f'Min rating: \033[91m{min(ratings)}\033[0m')

    # Get list of favorite genres from user:
    user.add_fav_genres(get_user_favs())

    # Recommend movies based on favorite genres from user and ratings:
    recommended_movies = recommend_movies(user.movies, user.fav_genres)
    print('Recommendations based on favorite genres:')
    if recommended_movies:
        for movie, (rating, genre) in recommended_movies.items():
            print(f'{movie} (Rating: {rating}, Genre: {genre})')
    else:
        print('No recommendations.')

    smart_recommendations = collaborative_recommendations(user, users)
    print('Recommendations from similar users:')
    if smart_recommendations:
        for movie, (rating, genre) in smart_recommendations.items():
            print(f'{movie} (Rating: {rating}, Genre: {genre})')
    else:
        print('No recommendations.')

if __name__ == '__main__':
    check = 1
    while check:
        main()
        again = input('Would you like to continue? (y/n): ')
        if again.lower() == 'n':
            check = None