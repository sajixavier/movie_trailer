import webbrowser


class Movie():
    """ This class will provide details like title, storyline,
    poster image and youtube url of a movie etc """
    def __init__(self, movie_title, movie_storyline,
                 movie_poster_image, movie_youtube_url):
        """ This constructor will accept movie title, story line, poster
and youtube url (trailer)"""
        # Assign values to class variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_youtube_url

    def show_trailer(self):
        """ This function will open the movie trailer in a browser """
        webbrowser.open(self.trailer_youtube_url)
