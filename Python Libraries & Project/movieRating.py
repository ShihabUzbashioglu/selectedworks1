from imdb import imdb


def get_movie_rating():
    movie_name = input ("enter movie name")
    ia = imdb()
    movies = ia.search_movie(movie_name)


    if movies :
        movie = movies[0]
        ia.update(movie)
        rating = movie.get('rating', 'n/a')
        print (f"the imdb rating of '{movie_name}' is : {rating}")
    else:
        print (f"movie '{movie_name}' not found !")


get_movie_rating()