import webbrowser

class Movie():
    def __init__(self,movie_title,movie_storyline,movie_poster_url,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_url = movie_poster_url
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
