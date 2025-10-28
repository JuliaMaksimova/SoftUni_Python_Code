# class Book:
#     def __init__(self, name, author, pages):
#         self.name = name
#         self.author = author
#         self.pages = pages
#
# book = Book("Harry Potter", "J.K.R.", 3000)
#
# print(book.name)
# print(book.author)
# print(book.pages)


# ----------------

# class Car:
#     def __init__(self, name, model, engine):
#         self.name = name
#         self.model = model
#         self.engine = engine
#
#     def get_info(self):
#         return f"This is {self.name} {self.model} with engine {self.engine}."
#
# car = Car("Toyota", "Corola", "1.88L")
#
# print(car.get_info())

# ----------------

# class Music:
#     def __init__(self, title, artist, lyrics):
#         self.title = title
#         self.artist = artist
#         self.lyrics = lyrics
#
#     def print_info(self):
#         return f'This is "{self.title}" from "{self.artist}"'
#
#     def play(self):
#         return self.lyrics
#
# song = Music("Title", "Artist", "Lyrics")
#
# print(song.print_info())
# print(song.play())

# ----------------

class Shop:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)

shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])

print(shop.get_items_count())



