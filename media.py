import webbrowser

# Class Movie
class Movie():
    # Class Movie constructor.
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, review_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.review_url = review_url

    # Define functions that opens up movie trailer in the webbrowser.
    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
