from peewee import *
from database_config import database_path
from model import Bookmarks, Cache
import json

def combine_dictionaries(imgur_dictionary, spotify_dictuonary, ticketmaster_dictionary):
    new_dictionary = {}
    new_dictionary['imgur'] = imgur_dictionary
    new_dictionary['spotify'] = spotify_dictuonary
    new_dictionary['ticketmaster'] = ticketmaster_dictionary
    return new_dictionary

def bookmark_data(artist_data):
    db = SqliteDatabase(database_path) # Get the path and connect to db
    db.connect()
    db.create_tables([Bookmarks])
    new_bookmark = Bookmarks.create(
    artist_name = artist_data['spotify']['artist_name'],
    image_url = artist_data['imgur']['image_url'],
    song1 = artist_data['spotify']['top_five_songs'][0],
    song2 = artist_data['spotify']['top_five_songs'][1],
    song3 = artist_data['spotify']['top_five_songs'][2],
    song4 = artist_data['spotify']['top_five_songs'][3],
    song5 = artist_data['spotify']['top_five_songs'][4],
    spotify_link = artist_data['spotify']['spotify_page_url'],
    events = json.dumps(artist_data['ticketmaster']['events'])
    )
    new_bookmark.save()