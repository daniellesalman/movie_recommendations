"""
This program is a system for movie recommendations.
"""

def main():
    movies = []
    movie = input('Enter a movie title: ')
    while not movie == 'end':
        movies.append(movie)
        movie = input('Enter a movie title: ')

    print(movies)

if __name__ == '__main__':
    main()