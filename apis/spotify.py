"""
Program to work with Spotify API
Please use your own spotify CLIENT_ID and CLIENT_SECRET keys
A call is made to API using artist/band name provided by user
With data received, we can extract artist id and make a new call to another API endpoint
to get artist albums, songs, profile urls, etc.
Program will list 5 most popular songs from each of 3 famous albums from artist found
"""
import requests
import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

def get_artist_music(artist):
    # Auth keys
    AUTH_URL = 'https://accounts.spotify.com/api/token'
    CLIENT_ID = getenv('SPOTIFY_CLIENT_ID_KEY')
    CLIENT_SECRET = getenv('SPOTIFY_CLIENT_SECRET_KEY')

    auth_response = connect_to_API(AUTH_URL, CLIENT_ID, CLIENT_SECRET)

    # convert response data to JSON format
    auth_response_data = auth_response.json()

    # save the access token
    access_token = auth_response_data['access_token']

    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }

    # base URL of all Spotify API endpoints
    BASE_URL = 'https://api.spotify.com/v1/'

    # get input from user
    # artist_name = get_input()


    """ make an API call using user's given artist name
    base url is used along with some parameters required by the API such as the type how many results needed
    or what type of search is being requested (artist, album, id, playlist, etc.)
    """
    artist_data = find_artist(BASE_URL, headers, artist)

    artist_url = get_artist_url(artist_data)

    genres = artist_data['artists']['items'][0]['genres']
    print(f'Artist genres: {genres}')

    artist_id = artist_data['artists']['items'][0]['id']
    # print(f'Artist id: {artist_id}')
    # print()

    # get all songs from artist
    songs_data = get_tracks(BASE_URL, headers, artist_id)

    # get top 5 artist tracks
    top_tracks = get_top_tracks(songs_data)

    # Create list of top tracks, and spotify link.
    spotify_data = {}
    spotify_data['artist_name'] = artist
    spotify_data['genres'] = genres
    spotify_data['spotify_page_url'] = artist_url
    spotify_data['top_five_songs'] = top_tracks
    return spotify_data


def connect_to_API(AUTH_URL, CLIENT_ID, CLIENT_SECRET):
    # make call to connect to API
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })

    return auth_response


# def get_input():
#     artist_name = input('Enter artist name: ')
#     return artist_name


def find_artist(BASE_URL, headers, artist_name):
    artist = requests.get(BASE_URL + 'search?',
                          headers=headers,
                          params={'query': artist_name, 'offset': 0, 'limit': 1, 'type': 'artist'})
    artist_data = artist.json()
    return artist_data


def get_artist_url(artist_data):
    # print(artist_data['artists']['items'][0]['external_urls']['spotify'])
    return artist_data['artists']['items'][0]['external_urls']['spotify']


def get_tracks(BASE_URL, headers, artist_id):
    songs_request = requests.get(BASE_URL + 'artists/' + artist_id + '/top-tracks?country=US',
                                 headers=headers,)
    songs_data = songs_request.json()
    return songs_data
    # print(songs_data)


def get_top_tracks(songs_data):
    top_songs_list = []
    top_tracks = songs_data['tracks']

    # get 5 most popular songs
    for track in top_tracks[:5]:
        # print(track['name'])
        top_songs_list.append(track['name'])
    
    # print(top_songs_list)
    return top_songs_list


# res=get_artist_music('Lady Gaga')
# print(res['artist_name'])