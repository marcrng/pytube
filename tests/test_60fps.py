import unittest
from pytube import YouTube
from pytube.innertube import InnerTube
import pprint


def is_otf_stream(stream):
    return stream.is_otf


class TestCustomStreamQuery(unittest.TestCase):
    def setUp(self):
        self.yt = YouTube('https://www.youtube.com/watch?v=nb_TnOMZ-kU')
        self.all_streams = self.yt.streams
        self.pp = pprint.PrettyPrinter(indent=4)
        self.it = InnerTube(client='WEB')
        self.id = 'nb_TnOMZ-kU'

    def test_vid_info(self):
        self.pp.pprint(self.yt.vid_info)

    def test_print_all_streams(self):
        # Print all available streams
        for stream in self.all_streams:
            print(stream)

    def test_print_innertube_raw(self):

        # Define the endpoint, query parameters, and data
        endpoint = 'https://www.youtube.com/youtubei/v1/player'
        query = {
            'videoId': 'nb_TnOMZ-kU',  # Replace with your video's ID
        }
        query.update(self.it.base_params)
        data = self.it.base_data

        # Use the _call_api method to make the request
        response = self.it._call_api(endpoint, query, data)

        # Print the response
        self.pp.pprint(response)

    def test_30fps(self):
        # Check if the stream with itag '136' is included
        self.assertTrue(any(stream.itag == 136 for stream in self.all_streams))

    def test_60fps(self):
        # Check if the stream with itag '303' is included
        self.assertTrue(any(stream.itag == 308 for stream in self.all_streams))

    def test_it_60fps(self):
        # Define the endpoint, query parameters, and data
        endpoint = 'https://www.youtube.com/youtubei/v1/player'
        query = {
            'videoId': 'nb_TnOMZ-kU',  # Replace with your video's ID
        }
        query.update(self.it.base_params)
        data = self.it.base_data

        # Use the _call_api method to make the request
        response = self.it._call_api(endpoint, query, data)

        self.assertTrue("'itag': 308" in str(response))

    def test_it_player_response(self):
        response = self.it.player(self.id)
        self.pp.pprint(response)

    def test_download(self):
        stream = self.yt.streams.get_by_itag(308)
        stream.download()


if __name__ == '__main__':
    unittest.main()
