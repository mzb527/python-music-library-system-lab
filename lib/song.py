class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artists_count(artist)
    
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

# Example usage
song1 = Song("Halo", "Beyoncé", "Pop")
song2 = Song("99 Problems", "Jay-Z", "Rap")

print(Song.show_song_info())


