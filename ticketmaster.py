import requests
from ticketmaster_config import api_key, artist


def get_events(artist):

    """
    'Main' of the program, returns a dictionary with the following structure: 
    [{'event_date' : date, 'event_time' : time, 'venue_name': venue_name, 'event_location' : location,  'link' : link_to_buy tickets}, ect... ]
    """
    response = request_events(artist)
    json_data = get_json_from_response(response)
    if check_for_events(json_data):
        event_list = get_event_list_from_json_data(json_data)
        print(event_list)
        return event_list
    else:
        print('Sorry, there are no events currently scheduled for this artist in the USA')
        return None


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

needed_event_data = get_events(artist)