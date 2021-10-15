"""
This is some test code for the ticketmaster api
"""

import requests

base_url = 'https://app.ticketmaster.com'
base_path = '/discovery/v2/events.json?'
key = '&apikey='
artist = ''

url_string = base_url + base_path + 'keyword=' + artist + key

result = requests.get(url_string)

number_of_pages = result.json()['page']['totalPages']
number_of_elements = result.json()['page']['totalElements']
number_of_events = 0
next_page_path = result.json()['_links']['next']

print(number_of_elements)
print(number_of_pages)
print(next_page_path)

def get_json_data(url): # Returns Json data from a request
    result = requests.get(url)
    return result.json()

def get_events(artist):
    base_url = 'https://app.ticketmaster.com'
    base_path = '/discovery/v2/events.json?'
    key = '&apikey='
    events = []
    new_url = base_url + base_path + 'keyword=' + artist + key

    first_page = get_json_data(new_url)
    for i in first_page['_embeded']['events']:
        events.append(i)

    next_page_path = first_page['_links']['next']['href']

    if next_page_path:
        get_json_data


