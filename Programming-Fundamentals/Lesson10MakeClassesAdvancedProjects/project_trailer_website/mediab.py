import webbrowser


class Movie():
    # parent class
    def __init__(self, movie_title, movie_storyline,
                 poster_image_url, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube
    # opens trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    # shows title and story

    def show_info(self):
        print("Title-"+self.title)
        print("Story-"+self.storyline)


class Series(Movie):
    # child class
    def __init__(self, movie_title, movie_storyline, poster_image_url,
                 trailer_youtube, season, episode):
        Movie.__init__(self, movie_title, movie_storyline,
                       poster_image_url, trailer_youtube)
        self.season = season
        self.episode = episode

    # This appears in the shell so you know what movies appear.
    def show_info(self):
        print("Title-"+self.title)
        print("Story-"+self.storyline)
        print("Season-"+self.season)
        print("Episode-"+self.episode)


class Series(Movie):
    # child class
    def __init__(self, movie_title, movie_storyline, poster_image_url,
                 trailer_youtube, season, episode):
        Movie.__init__(self, movie_title, movie_storyline,
                       poster_image_url, trailer_youtube)
        self.season = season
        self.episode = episode
    # shows info for series

    def show_info(self):
        print("Title-"+self.title)
        print("Story-"+self.storyline)
        print("Season-"+self.season)
        print("Episode-"+self.episode)
