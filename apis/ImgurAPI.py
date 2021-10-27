from typing import cast
import requests
from imagurapiconfig import header
def getpicture(artist):

  url = "https://api.imgur.com/3/gallery/search/top/year/1?"
  query = {'q': artist, 'q_type' : 'jpg'}


  payload={}
  files={}

  data = requests.request("GET", url, params=query, headers=header, data=payload, files=files).json()
  imagedatalist = data['data']
  firstimage = imagedatalist[0]
  url = firstimage['images'][0]['link']
  return url
  