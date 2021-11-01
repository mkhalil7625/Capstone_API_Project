from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length
class BookmarkForm(FlaskForm):
    artist_name = StringField('Name', DataRequired())
    image_url = StringField('Image_url', DataRequired())
    song1 =StringField('Song1', DataRequired())
    song2 =StringField('Song2', DataRequired()) 
    song3 =StringField('Song3', DataRequired()) 
    song4 =StringField('Song4', DataRequired()) 
    song5 =StringField('Song5', DataRequired()) 
    spotify_link =StringField('Spotify_page_url', DataRequired()) 
    events =StringField('Svents', DataRequired()) 
    submit = SubmitField('Save Source')