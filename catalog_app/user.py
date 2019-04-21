from album import Album


class User:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def __repr__(self):
        return "<User: {}>".format(self.name)

    def get_purchased_albums(self):
        return list(filter(lambda album: album.purchased, self.albums))

    def get_unpurchased_albums(self):
        return list(filter(lambda album: not album.purchased, self.albums))

    def add_album(self, title, artist, genre, purchased):
        self.albums.append(Album(title, artist, genre, purchased))

    def delete_album(self, title):
        self.albums = list(filter(self.albums(lambda album: album.title != title, self.albums)))

    def save_to_csv(self):
        with open("{}_user.txt".format(self.name), "w") as file:
            file.write("{}\n".format(self.name))

            for album in self.albums:
                file.write("{},{},{},{}\n".format(album.title, album.artist, album.genre, str(album.purchased)))

    @classmethod
    def load_from_csv(cls, filename):
        with open(filename, "r") as file:
            contents = file.readlines()

            user_name = contents[0]
            user_albums = []

            for album in contents[1:]:
                album_data = album.split(",")
                user_albums.append(Album(album_data[0], album_data[1], album_data[2], album_data[3] == True))

            user = cls(user_name)
            user.albums = user_albums

            return user