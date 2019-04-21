from album import Album
from user import User

album_one = Album("Kid A", "Radiohead", "Alternative", True)
album_two = Album("Baby on Baby", "DaBaby", "Hip-Hop/Rap", True)
album_three = Album("album_1", "San Holo", "Futurebass", True)
album_four = Album("Vega", "il:lo", "Electronic", False)

username = input("What is your user name? ")
new_user = User(username)

new_user.albums.append(album_one)
new_user.albums.append(album_two)
new_user.albums.append(album_three)
new_user.albums.append(album_four)

new_user.save_to_csv()

new_user = User.load_from_csv("roz0n_user.txt")
print(new_user.name)
print(new_user.albums)