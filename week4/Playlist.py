class Playlist:
    def __init__(self, name, repeat = False, shuffle = False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.list_songs = []

    def add_song(self, song):
        self.list_songs.append(song)

    def remove_song(self, song):
        self.list_songs.remove(song)
