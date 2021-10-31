from unittest import TestCase
from model import Bookmarks
from peewee import *

import bookmark
from bookmark import DuplicateError, ArtistNotInDatabase

class TestDB(TestCase):


    def setup(self):
        db = SqliteDatabase('test_db.sqlite') # Get the path and connect to db
        db.connect()
        Bookmarks.drop_table()
        db.create_tables([Bookmarks])

    
    def test_add_new_bookmark(self):
        bookmark.bookmark_data('artist_name', 'image_url', 'song1', 'song2', 'song3', 'song4', 'song5', 'spotify_page_url', 'events')
        expected = {'artist_name' : 'artist_name',
        'image_url' : 'image_url',
        'song1' : 'song1',
        'song2' : 'song2',
        'song3' : 'song3',
        'song4' : 'song4',
        'song5' : 'song5',
        'spotify_link' : 'spotify_page_url',
        'events' : 'events'}
        self.compare_db_to_expected(expected)


    def compare_db_to_expected(self, expected):

        db = SqliteDatabase('test_db.sqlite') # Get the path and connect to db
        db.connect()
        all_data = Bookmarks.select(Bookmarks)

        self.assertEqual(len(expected.keys()), len(all_data))

        for row in all_data:
            self.assertIn(row[0], expected.keys())
            self.assertEqual(expected[row[0]], row[1])