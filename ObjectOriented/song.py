# Notice class Album and Artist have circular references


class Song:
    """A class to have a song blueprint of a song"""

    def __init__(self, title, artist, duration=0):
        """
        :param title: Initializes the title
        :param artist: Initializes with the artist name(optional)
        :param duration: duration of the song
        """
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """Methods:
     add_song: used to add a new song to the album's track.
     """
    def __init__(self, name, year, artist=None):
        """
        :param name: name of the album
        :param year: year it was released
        :param artist: who is the artist
        """
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """
        Add a song to the list of tracks
        :param song: A song to add
        :param position: it is optional
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """
    Basic artist class.
    Attributes:
        name (string): name of the artist.
        albums (list): list o0f albums.
    Methods:
        add_album: use to add a album to the list of albums artist have
    """
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """
        This method adds the album to the list of albums an artist have
        :param album: album object to be added.
        :return: None
        """
        self.albums.append(album)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []
    with open('albums.txt', 'r') as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{} : {} : {} : {}".format(artist_field, album_field, year_field, song_field))

            # check is the artist is None
            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.name != album_field:
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)

            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)
        # Remember read will not allow the last line data to be entered in the list
        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)
    return artist_list


if __name__ == '__main__':
    artists = load_data()
    print("Number of various artists {} ".format(len(artists)))
