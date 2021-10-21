from peewee import *
from database_config import database_path
from model import Bookmarks, Cache
import json


"""WARNING This program DROPS ALL EXISTING TABLES in the database and repopulates the bookmarks and cache table with default data"""

# Example event list
example_list = [
    {'event_date': '2021-10-21', 'event_time': '20:00:00', 'venue_name': 'Park Theater', 'event_location': 'Las Vegas, Nevada', 'link_for_tickets': 'https://www.ticketmaster.com/lady-gaga-jazz-piano-las-vegas-nevada-10-21-2021/event/2E005B12A9EE414F'},
    {'event_date': '2021-10-23', 'event_time': '20:00:00', 'venue_name': 'Park Theater', 'event_location': 'Las Vegas, Nevada', 'link_for_tickets': 'https://www.ticketmaster.com/lady-gaga-jazz-piano-las-vegas-nevada-10-23-2021/event/2E005B12A9F14151'}, 
    {'event_date': '2021-10-31', 'event_time': '20:00:00', 'venue_name': 'Park Theater', 'event_location': 'Las Vegas, Nevada', 'link_for_tickets': 'https://www.ticketmaster.com/lady-gaga-jazz-piano-las-vegas-nevada-10-31-2021/event/2E005B12A9FC4184'},
    {'event_date': '2021-10-30', 'event_time': '20:00:00', 'venue_name': 'Park Theater', 'event_location': 'Las Vegas, Nevada', 'link_for_tickets': 'https://www.ticketmaster.com/lady-gaga-jazz-piano-las-vegas-nevada-10-30-2021/event/2E005B12A9FA4160'},
    {'event_date': '2021-10-28', 'event_time': '20:00:00', 'venue_name': 'Park Theater', 'event_location': 'Las Vegas, Nevada', 'link_for_tickets': 'https://www.ticketmaster.com/lady-gaga-jazz-piano-las-vegas-nevada-10-28-2021/event/2E005B12A9F6415E'},
    {'event_date': '2021-10-24', 'event_time': '20:00:00', 'venue_name': 'Park Theater', 'event_location': 'Las Vegas, Nevada', 'link_for_tickets': 'https://www.ticketmaster.com/lady-gaga-jazz-piano-las-vegas-nevada-10-24-2021/event/2E005B12A9F34153'},
    {'event_date': '2021-11-12', 'event_time': '21:00:00', 'venue_name': 'Teragram Ballroom', 'event_location': 'Los Angeles, California', 'link_for_tickets': 'https://www.ticketmaster.com/candi-pops-lady-gaga-ball-los-angeles-california-11-12-2021/event/09005B52B555561C'},
    {'event_date': '2021-11-27', 'event_time': '21:00:00', 'venue_name': 'Live at 1175', 'event_location': 'Kansasville, Wisconsin', 'link_for_tickets': 'https://www.ticketweb.com/event/little-monsters-lady-gaga-tribute-live-at-1175-tickets/11432855'},
    {'event_date': '2021-10-23', 'event_time': '21:00:00', 'venue_name': 'Warehouse on Watts | W.O.W. ', 'event_location': 'Philadelphia, Pennsylvania', 'link_for_tickets': 'https://www.ticketweb.com/event/darius-alexander-dj-xtina-warehouse-on-watts-wow-tickets/11431875'}]

event_dictionary = {}

event_dictionary['events'] = example_list # Create new dictionary to store event list under the key 'events'


db = SqliteDatabase(database_path) # Get the path and connect
db.connect()


Bookmarks.drop_table() # Drop tables if they are there
Cache.drop_table()


def populate_test_data(event_dictionary):
    db.create_tables([Bookmarks, Cache])
    #Create an entry in the bookmarks table
    Bookmarks.create(
    artist_name = 'Lady Gaga',
    image_url = 'https://www.google.com',
    song1 = 'Shallow',
    song2 = 'Bad Romance',
    song3 = 'Always Remember Us This Way',
    song4 = 'Rain On Me (with Ariana Grande)',
    song5 = 'Poker Face',
    spotify_link = 'https://open.spotify.com/artist/1HY2Jd0NmPuamShAr6KMms',
    events = json.dumps(event_dictionary))

    #Create entry in the cache table
    Cache.create(
    artist_name = 'Lady Gaga',
    image_url = 'https://www.google.com',
    song1 = 'Shallow',
    song2 = 'Bad Romance',
    song3 = 'Always Remember Us This Way',
    song4 = 'Rain On Me (with Ariana Grande)',
    song5 = 'Poker Face',
    spotify_link = 'https://open.spotify.com/artist/1HY2Jd0NmPuamShAr6KMms',
    events = json.dumps(event_dictionary))


populate_test_data(event_dictionary)