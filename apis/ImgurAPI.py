from typing import cast
import requests
from os import getenv
from dotenv import load_dotenv
def getpicture(artist):

  load_dotenv()
  key = getenv('IMGUR_KEY')

  url = "https://api.imgur.com/3/gallery/search/top/year/1?"
  query = {'q': artist, 'q_type' : 'jpg'}


  payload={}
  files={}
  header = {
  'Authorization': 'Client-ID key'
}

  data = requests.request("GET", url, params=query, headers=header, data=payload, files=files).json()
  imagedatalist = data['data']
  firstimage = imagedatalist[0]
  url = firstimage['images'][0]['link']
  return url
