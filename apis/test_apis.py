from unittest import TestCase
from unittest.mock import patch, Mock
import ImgurAPI
import ticketmaster
import spotify

class TestTicketmasterApi(TestCase):

    
    @patch('ticketmaster.request_events')
    def test_get_event_list_from_json_data(self, mock_responses):
        pass