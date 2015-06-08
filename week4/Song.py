class Song:

    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        parts = [int(part.strip()) for part in length.split(":")]

        if len(parts) == 3:
            self.hours = parts[0]
            self.minutes = parts[1]
            self.seconds = parts[2]
        elif len(parts) == 2:
            self.minutes = parts[0]
            self.seconds = parts[1]
        else:
            raise ValueError("Length not proper format: {}".format(length))




    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title, self.album, self.length)

    def __eq__(self, other):
        title_eq = self.title == other.title
        artist_eq = self.artist == other.artist
        album_eq = self.album == other.album
        length_eq = self.length == other.length

        return title_eq and artist_eq and album_eq and length_eq

    def __hash__(self):
        return hash(str(self))

    def get_hours(self):
        return self.hours

    def get_minutes(self):
        return self.hours*60 + self.minutes

    def get_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


    def length_print(self, seconds=False, minutes=False, hours=False):

        if not seconds and not minutes and not hours:
            return self.length

        if hours:
            return self.get_hours()

        if minutes:
            return self.get_minutes()

        if seconds:
            return self.get_seconds()



song = Song("gagsa", "gas", "gafaa", "1:30:63")
print(song.length_print())
