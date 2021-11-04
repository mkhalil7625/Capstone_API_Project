from peewee import *
import sqlite3
from database_config import database_path
from models import Bookmarks, Cache
import json
from pprint import pprint


# example_imgur_dictionary =  {'image_url': 'https://www.google.com'}

# example_spotify_dictionary = {'artist_name':'Lady RaRa', 'genres' : ['dance', 'pop'], 'spotify_page_url': 'https://open.spotify.com/artist/1HY2Jd0NmPuamShAr6KMms', 'top_five_songs': ['Shallow','Bad Romance', 'Always Remember Us This Way', 'Rain On Me (with Ariana Grande)', 'Poker Face']}

# example_ticketmaster_dictionary = {}
# example_ticketmaster_dictionary['events'] = [
#     {'event_date': '2021-10-21', 'event_time': '20:00:00', 'venue_name': 'Park Theater', 'event_location': 'Las Vegas, Nevada', 'link_for_tickets': 'https://www.ticketmaster.com/lady-gaga-jazz-piano-las-vegas-nevada-10-21-2021/event/2E005B12A9EE414F'},
#     {'event_date': '2021-10-23', 'event_time': '20:00:00', 'venue_name': 'Park Theater', 'event_location': 'Las Vegas, Nevada', 'link_for_tickets': 'https://www.ticketmaster.com/lady-gaga-jazz-piano-las-vegas-nevada-10-23-2021/event/2E005B12A9F14151'}, 
#     {'event_date': '2021-10-31', 'event_time': '20:00:00', 'venue_name': 'Park Theater', 'event_location': 'Las Vegas, Nevada', 'link_for_tickets': 'https://www.ticketmaster.com/lady-gaga-jazz-piano-las-vegas-nevada-10-31-2021/event/2E005B12A9FC4184'},
#     {'event_date': '2021-10-30', 'event_time': '20:00:00', 'venue_name': 'Park Theater', 'event_location': 'Las Vegas, Nevada', 'link_for_tickets': 'https://www.ticketmaster.com/lady-gaga-jazz-piano-las-vegas-nevada-10-30-2021/event/2E005B12A9FA4160'},
#     {'event_date': '2021-10-28', 'event_time': '20:00:00', 'venue_name': 'Park Theater', 'event_location': 'Las Vegas, Nevada', 'link_for_tickets': 'https://www.ticketmaster.com/lady-gaga-jazz-piano-las-vegas-nevada-10-28-2021/event/2E005B12A9F6415E'},
#     {'event_date': '2021-10-24', 'event_time': '20:00:00', 'venue_name': 'Park Theater', 'event_location': 'Las Vegas, Nevada', 'link_for_tickets': 'https://www.ticketmaster.com/lady-gaga-jazz-piano-las-vegas-nevada-10-24-2021/event/2E005B12A9F34153'},
#     {'event_date': '2021-11-12', 'event_time': '21:00:00', 'venue_name': 'Teragram Ballroom', 'event_location': 'Los Angeles, California', 'link_for_tickets': 'https://www.ticketmaster.com/candi-pops-lady-gaga-ball-los-angeles-california-11-12-2021/event/09005B52B555561C'},
#     {'event_date': '2021-11-27', 'event_time': '21:00:00', 'venue_name': 'Live at 1175', 'event_location': 'Kansasville, Wisconsin', 'link_for_tickets': 'https://www.ticketweb.com/event/little-monsters-lady-gaga-tribute-live-at-1175-tickets/11432855'},
#     {'event_date': '2021-10-23', 'event_time': '21:00:00', 'venue_name': 'Warehouse on Watts | W.O.W. ', 'event_location': 'Philadelphia, Pennsylvania', 'link_for_tickets': 'https://www.ticketweb.com/event/darius-alexander-dj-xtina-warehouse-on-watts-wow-tickets/11431875'}]

# def combine_dictionaries(imgur_dictionary, spotify_dictuonary, ticketmaster_dictionary):
#     new_dictionary = {}
#     new_dictionary['imgur'] = imgur_dictionary
#     new_dictionary['spotify'] = spotify_dictuonary
#     new_dictionary['ticketmaster'] = ticketmaster_dictionary
#     return new_dictionary

# def bookmark_data(artist_data):
#     db = SqliteDatabase(database_path) # Get the path and connect to db
#     db.connect()
#     db.create_tables([Bookmarks])

#     artist_name_in_bookmarks = Bookmarks.select().where(Bookmarks.artist_name == artist_data['spotify']['artist_name']) # Check db for duplicate data, do nothing if artist is found
#     if artist_name_in_bookmarks:
#         print('Artist already in bookmark')
#         pass
#     else: # Create a bookmark if the artist is not found
#         new_bookmark = Bookmarks.create(
#         artist_name = artist_data['spotify']['artist_name'],
#         image_url = artist_data['imgur']['image_url'],
#         song1 = artist_data['spotify']['top_five_songs'][0],
#         song2 = artist_data['spotify']['top_five_songs'][1],
#         song3 = artist_data['spotify']['top_five_songs'][2],
#         song4 = artist_data['spotify']['top_five_songs'][3],
#         song5 = artist_data['spotify']['top_five_songs'][4],
#         spotify_link = artist_data['spotify']['spotify_page_url'],
#         events = json.dumps(artist_data['ticketmaster']['events'])
#         )
#         new_bookmark.save()

# new_dictionary = combine_dictionaries(example_imgur_dictionary, example_spotify_dictionary, example_ticketmaster_dictionary)
# pprint(new_dictionary)
# bookmark_data(new_dictionary)

def bookmark_data(artist_name, image_url, spotify_page_url):
    db = SqliteDatabase(database_path) # Get the path and connect to db
    db.connect()
    db.create_tables([Bookmarks])
    artist_name_in_bookmarks = Bookmarks.select().where(Bookmarks.artist_name == artist_name) # Check db for duplicate data, do nothing if artist is found
    if artist_name_in_bookmarks:
        raise DuplicateError('That artist is already in the bookmarks')
    else:
        new_bookmark = Bookmarks.create(
        artist_name = artist_name,
        image_url = image_url,
        # song1 = song1,
        # song2 = song2,
        # song3 = song3,
        # song4 = song4,
        # song5 = song5,
        spotify_link = spotify_page_url,
        # events = events
        )
        new_bookmark.save()
def get_artist_bookmark(artist_name):
    db = SqliteDatabase(database_path) # Get the path and connect to db
    db.connect()
    db.create_tables([Bookmarks])
    artist_bookmark = Bookmarks.select().where(Bookmarks.artist_name == artist_name)
    if artist_bookmark:
        artist_data = {}
        artist_data['artist_name'] = artist_bookmark.artist_name
        artist_data['image_url'] = artist_bookmark.image_url
        artist_data['song1'] = artist_bookmark.song1
        artist_data['song2'] = artist_bookmark.song2
        artist_data['song3'] = artist_bookmark.song3
        artist_data['song4'] = artist_bookmark.song4
        artist_data['song5'] = artist_bookmark.song5
        artist_data['spotify_link'] = artist_bookmark.spotify_link
        # artist_data['events'] = artist_bookmark.events
        return artist_data
    else:
        raise ArtistNotInDatabase('That artist is not in the database')

def get_all_bookmarks():
    # db = SqliteDatabase(database_path) # Get the path and connect to db
    # db.connect()
    # db.create_tables([Bookmarks])
    # query = Bookmarks.select()
    db=database_path
    with sqlite3.connect(db) as conn:
        conn.row_factory=sqlite3.Row
        query=conn.execute(f'SELECT * FROM bookmarks')

        all_bookmarks=query.fetchall()
        return all_bookmarks


class DuplicateError(Exception):
    pass

class ArtistNotInDatabase(Exception):
    pass