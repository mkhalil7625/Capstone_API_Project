from flask import Flask,request, render_template, redirect
# todo import database
from apis import ticketmaster
from database import bookmark

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/get-artist')
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


# @app.route('/display-all-bookmarks')
#     #List of all

# @app.route('/error')
#     #Error handling