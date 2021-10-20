from flask import Flask,request, render_template, redirect
# todo import database
#import apis

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/get-artist')
def det_artist():
    # todo

