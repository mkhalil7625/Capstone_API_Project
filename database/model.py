# from peewee import *
# from database_config import database_path


# db = SqliteDatabase(database_path)


# class Bookmarks(Model):
#     artist_name = CharField()
#     image_url = CharField()
#     # song1 = CharField()
#     # song2 = CharField()
#     # song3 = CharField()
#     # song4 = CharField()
#     # song5 = CharField()
#     spotify_link = CharField()
#     # events = CharField()

#     class Meta:
#         database = db

#     def __str__(self):
#         return f'{self.artist_name}, {self.image_url},  {self.spotify_link}'


# class Cache(Model):
#     artist_name = CharField()
#     image_url = CharField()
#     song1 = CharField()
#     song2 = CharField()
#     song3 = CharField()
#     song4 = CharField()
#     song5 = CharField()
#     spotify_link = CharField()
#     events = CharField()
#     time_cached = IntegerField()

#     class Meta:
#         database = db

#     def __str__(self):
#         return f'{self.artist_name}, {self.image_url}, {self.song1}, {self.song2}, {self.song3}, {self.song4}, {self.song5}, {self.spotify_link}, {self.events}'