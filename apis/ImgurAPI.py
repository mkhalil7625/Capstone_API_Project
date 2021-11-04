from typing import cast
import requests
from os import getenv
from dotenv import load_dotenv

def getpicture(artist):
  try:
    load_dotenv()
    key = getenv('IMGUR_CLIENT_ID')

    url = "https://api.imgur.com/3/gallery/search/viral/year/?"
    query = {'q': artist, 'q_type' : 'jpg'}


    payload={}
    files={}
    header = {
      'Authorization': 'Client-ID '+key
    }

    response = requests.request("GET", url, params=query, headers=header, data=payload, files=files)
    print(response)
    response.raise_for_status()
    data = response.json()
    imagedatalist = data['data']
    firstimage = imagedatalist[0]
    url = firstimage['images'][0]['link']

    imgur_data = {} # Create dictionary that will contain data to return
    imgur_data['image_link'] = url

    return imgur_data

  except requests.exceptions.HTTPError as errh: # https://www.nylas.com/blog/use-python-requests-module-rest-apis/#make-robust-api-requests - The resource I used to help make this
    print(errh)
  except requests.exceptions.ConnectionError as errc:
    print(errc)
  except requests.exceptions.Timeout as errt:
    print(errt)
  except requests.exceptions.RequestException as err:
    print(err)

