"""
This program is a system for movie recommendations.
"""

def get_movies():
    """
    This function gets a list of movies from the user.
    :return: list of movies
    """
    movies = []
    movie = input('Enter a movie title: ')
    while not movie == 'end':
        movies.append(movie)
        movie = input('Enter a movie title: ')
    return movies

def get_ratings(movies):
    """
    This function gets a rating for each movie in a movie list from the user.
    :param movies: list of movies
    :return: dictionary of movies with ratings
    """
    ratings = {}
    print('Rate each movie:')
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

if __name__ == '__main__':
    main()