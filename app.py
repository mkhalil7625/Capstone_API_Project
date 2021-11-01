from flask import Flask,request, render_template, redirect
import bookmark
from apis import ticketmaster,spotify, ImgurAPI
import os
import json


app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/get-artist', methods=['GET'])
def get_artist_info():
    artist_name = request.args.get('search')
    artist_spotify_info = spotify.get_artist_music(artist_name)
    artist_events = ticketmaster.get_events(artist_spotify_info['artist_name'])
    artist_url = ImgurAPI.getpicture(artist_spotify_info['artist_name'])

    return render_template('artist.html',events=artist_events, artist_info=artist_spotify_info, artist_image=artist_url)

@app.route('/save-artist')
def save_artist():
    # Ask database to save artist
    # bookmark.bookmark_data(artist_data)

    print(request.data.get('artist_name'))
    return redirect('/display-all-bookmarks')


@app.route('/display-all-bookmarks', methods=['GET'])
def display_all_bookmarks():
    bookmarks = bookmark.get_all_bookmark()
    # parsed_bookmarks=JSON.parse
    return render_template('bookmarks.html',bookmarks=bookmarks)

# @app.route('/error')
#     #Error handling

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)