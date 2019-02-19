class Song:
    """A class to have a song blueprint of a song"""

    def __init__(self, title, artist, duration=0):
        """

        :param title: Initializes the title
        :param artist: Initializes with the artist name
        :param duration: duration of the song
        """
        self.title = title
        self.artist = artist
        self.duration = duration


help(Song)
print(Song.__doc__)