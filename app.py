from flask import Flask,request, render_template, redirect, jsonify
# from .database import model
import bookmarks
from apis import ticketmaster,spotify, ImgurAPI
import os
from flask_caching import Cache
import json
from playhouse.shortcuts import model_to_dict

app = Flask(__name__)
# caching setup
cache=Cache(config={'CACHE_TYPE':'SimpleCache'})
cache.init_app(app)


# Many of these routes need to anticpate errors and take some action - for example,
# redirect the user to an error page.  Differentiate between "Artist not found" type errors, 
# where the user can try another search, and application errors like API server down or code 
# error, that you would show a general 'sorry something went wrong' type message.

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/get-artist')
@cache.cached(timeout=5)
def get_artist_info():
    artist_name = request.args.get('search')
    artist_spotify_info = spotify.get_artist_music(artist_name)
    artist_events = ticketmaster.get_events(artist_spotify_info['artist_name'])
    artist_url = ImgurAPI.get_picture(artist_spotify_info['artist_name'])

    return render_template('artist.html',events=artist_events, artist_info=artist_spotify_info, artist_image=artist_url)

@app.route('/save-artist')
def save_artist():
    # Ask database to save artist
    artist_name = request.args.get("artist_name")
    image_link = request.args.get("image_link")
    # genres = request.args.get("genres")
    spotify_page_url = request.args.get("spotify_page_url")
   

    bookmarks.bookmark_data(artist_name,image_link,spotify_page_url)
    # print(request.data.get('artist_name'))
    return redirect('/display-all-bookmarks')


@app.route('/display-all-bookmarks')
def display_all_bookmarks():
    all_bookmarks =  bookmarks.get_all_bookmarks()
    # parsed_bookmarks=JSON.parse

    return render_template('bookmarks.html', bookmarks=all_bookmarks)
# @app.route('/error')
#     #Error handling

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)