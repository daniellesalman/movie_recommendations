"""
This program is a system for movie recommendations.
"""

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

def main():
    # Print list of movies:
    movies = get_movies()
    print(movies)

    # Add rating to each movie:
    movie_ratings = get_ratings(movies)

    # Print average, max, and min ratings:
    print(f'Average rating: \033[93m{sum(movie_ratings.values()) / len(movie_ratings)}\033[0m')
    print(f'Max rating: \033[92m{max(movie_ratings.values())}\033[0m')
    print(f'Min rating: \033[91m{min(movie_ratings.values())}\033[0m')

    # Add genre to each movie:
    movie_genres = get_genres(movie_ratings)

    # Get list of favorite genres from user:
    user_fav_genres = get_user_favs()

    # Recommend movies based on favorite genres from user and ratings:
    recommended_movies = recommend_movies(movie_genres, user_fav_genres)
    print(f'Recommended movies: {list(recommended_movies.keys())}')

if __name__ == '__main__':
    main()