class Song:
    """A class to have a song blueprint of a song"""

    def __init__(self, name, artist, duration=0):
        """
        :param name: Initializes the title
        :param artist: (Str) Name of the artist
        :param duration: duration of the song
        """
        self.name = name
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
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.name)
        if position is None:
            self.tracks.append(song_found)
        else:
            self.tracks.insert(position, song_found)


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


def find_object(field, iterable):
    for item in iterable:
        if item.name == field:
            return item


def load_data():
    artist_list = []
    with open('albums.txt', 'r') as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{} : {} : {} : {}".format(artist_field, album_field, year_field, song_field))
            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
    return artist_list


if __name__ == '__main__':
    artists = load_data()
    print("Number of various artists {} ".format(len(artists)))
