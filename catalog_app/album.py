class Album:
    def __init__(self, title, artist, genre, purchased):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.purchased = purchased

    def __repr__(self):
        return "<Album: {}>".format(self.title)

