

from typing import cast
import requests
from os import getenv
from dotenv import load_dotenv

def get_picture(artist):
  try:
    load_dotenv()
    key = getenv('IMGUR_CLIENT_ID')

    url = 'https://api.imgur.com/3/gallery/search/viral/year/?'
    query = {'q': artist, 'q_type': 'jpg'}

    header = {
      'Authorization': 'Client-ID '+key
    }

    response = requests.get(url, params=query, headers=header)
    response.raise_for_status()
    data = response.json()
    image_data_list = data['data']
    first_image = image_data_list[0]  # what if there are no images? 
    url = first_image['images'][0]['link']

    imgur_data = {} # Create dictionary that will contain data to return
    imgur_data['image_link'] = url  # why a dictionary with one key-value pair? Why not just return the url?

    return imgur_data

  # notes on this error handling pattern at GitHub
  except requests.exceptions.HTTPError as errh: # https://www.nylas.com/blog/use-python-requests-module-rest-apis/#make-robust-api-requests - The resource I used to help make this
    print(errh)
  except requests.exceptions.ConnectionError as errc:
    print(errc)
  except requests.exceptions.Timeout as errt:
    print(errt)
  except requests.exceptions.RequestException as err:
    print(err)

