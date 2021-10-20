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


def main():
    # Auth keys
    AUTH_URL = 'https://accounts.spotify.com/api/token'
    CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
    CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

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
    artist_name = get_input()


    """ make an API call using user's given artist name
    base url is used along with some parameters required by the API such as the type how many results needed
    or what type of search is being requested (artist, album, id, playlist, etc.)
    """
    artist_data = find_artist(BASE_URL, headers, artist_name)

    genres = artist_data['artists']['items'][0]['genres']
    print(f'Artist genres: {genres}')

    artist_id = artist_data['artists']['items'][0]['id']
    # print(f'Artist id: {artist_id}')
    # print()

    # get all songs from artist
    songs_data = get_tracks(BASE_URL, headers, artist_id)

    # get top 5 artist tracks
    top_tracks = get_top_tracks(songs_data)
    return top_tracks


def connect_to_API(AUTH_URL, CLIENT_ID, CLIENT_SECRET):
    # make call to connect to API
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })

    return auth_response


def get_input():
    artist_name = input('Enter artist name: ')
    return artist_name


def find_artist(BASE_URL, headers, artist_name):
    artist = requests.get(BASE_URL + 'search?',
                          headers=headers,
                          params={'query': artist_name, 'offset': 0, 'limit': 1, 'type': 'artist'})
    artist_data = artist.json()
    return artist_data


def get_tracks(BASE_URL, headers, artist_id):
    songs_request = requests.get(BASE_URL + 'artists/' + artist_id + '/top-tracks?country=US',
                                 headers=headers,)
    songs_data = songs_request.json()
    return songs_data
    # print(songs_data)


def get_top_tracks(songs_data):
    top_tracks = songs_data['tracks']

    # # get 5 most popular songs
    # for track in top_tracks[:limit]:
    #     print(track['name'])
    return top_tracks


main()
