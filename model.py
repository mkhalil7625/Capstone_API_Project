from peewee import *
from database_config import database_path
import json
from flask import g, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict


db = SqliteDatabase(database_path)


class Bookmarks(Model):
    id = IntegerField(primary_key=True)
    artist_name = CharField()
    image_url = CharField()
    song1 = CharField()
    song2 = CharField()
    song3 = CharField()
    song4 = CharField()
    song5 = CharField()
    spotify_link = CharField()
    events = CharField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.artist_name}, {self.image_url}, {self.song1}, {self.song2}, {self.song3}, {self.song4}, {self.song5}, {self.spotify_link}, {self.events}'


class Cache(Model):
    id = IntegerField(primary_key=True)
    artist_name = CharField()
    image_url = CharField()
    song1 = CharField()
    song2 = CharField()
    song3 = CharField()
    song4 = CharField()
    song5 = CharField()
    spotify_link = CharField()
    events = CharField()
    time_cached = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.artist_name}, {self.image_url}, {self.song1}, {self.song2}, {self.song3}, {self.song4}, {self.song5}, {self.spotify_link}, {self.events}'


db.create_tables([Bookmarks,Cache])

def open_close_connection(func):
    """
    Decorator used to open and close connections.
    """
    def decorated_function(*args):
        g.db = db
        g.db.connect()

        response = func(*args)

        g.db.close()
        return response
    return decorated_function


@open_close_connection
def get_saved_bookmarks():
    bookmarks = Bookmarks.select()
    return jsonify([model_to_dict(c) for c in bookmarks])

@open_close_connection
def add_artist():
    with db.atomic():
        c = Bookmarks.create(**request.json)
        return jsonify(model_to_dict(c)), 201

@open_close_connection
def get_by_id(bookmark_id):
    try:
        c = Bookmarks.get_by_id(bookmark_id)
        return json.dumps(model_to_dict(c)), 200
    except DoesNotExist:
        return 'Bookmark Not Found', 404
