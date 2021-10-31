import requests
from os import getenv
from dotenv import load_dotenv

load_dotenv()
api_key=getenv('TICKETMASTER_KEY') # take environment variables from .env.

def get_events(artist):

    """
    'Main' of the program, returns a dictionary with the following structure: 
    [{'event_date' : date, 'event_time' : time, 'venue_name': venue_name, 'event_location' : location,  'link' : link_to_buy tickets}, ect... ]
    """
    try:
        response = request_events(artist)
        response.raise_for_status()
        json_data = get_json_from_response(response)
        if check_for_events(json_data):
            event_list = get_event_list_from_json_data(json_data)
            ticketmaster_data = {}
            ticketmaster_data['events'] = event_list
            return ticketmaster_data
        else:
            print('Sorry, there are no events currently scheduled for this artist in the USA')
            return None
    except requests.exceptions.HTTPError as errh: # https://www.nylas.com/blog/use-python-requests-module-rest-apis/#make-robust-api-requests - The resource I used to help make this
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)


def request_events(artist):

    """
    Requests a response from ticketmaster, using the artist given as a keyword, and an api_key from a configuration file.
    """
    url = f'https://app.ticketmaster.com/discovery/v2/events.json?keyword={artist}&countryCode=US&apikey={api_key}'
    response = requests.get(url)
    return response


def get_json_from_response(result):
    return result.json()


def get_event_list_from_json_data(data):

    """
    Parses through the json data to pull our required data, and append it to a list.
    """
    event_list = []
    raw_event_data = data['_embedded']['events']

    for i in raw_event_data:
        event_dictionary = {}
        event_dictionary['event_date'] = i['dates']['start']['localDate']
        event_dictionary['event_time'] = i['dates']['start']['localTime']
        event_dictionary['venue_name'] = i['_embedded']['venues'][0]['name']
        event_dictionary['event_location'] = i['_embedded']['venues'][0]['city']['name'] + ', ' + i['_embedded']['venues'][0]['state']['name']
        event_dictionary['link_for_tickets'] = i['url']
        event_list.append(event_dictionary)
    return event_list


def check_for_events(data):

    """
    Check to see if there are any events in the response.
    """
    if '_embedded' in data:
        return True
    else:
        return False
