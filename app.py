from flask import Flask,request, render_template, redirect
# todo import database
from apis import ticketmaster

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/get-artist')
def get_artist_info():
    artist_name=request.args.get('search')
    artist_events=ticketmaster.get_events(artist_name)
    # artist_url=

    return render_template('artist.html',events=artist_events)

