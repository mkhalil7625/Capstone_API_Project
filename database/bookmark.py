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