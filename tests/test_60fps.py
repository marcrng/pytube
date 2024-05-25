import unittest
from pytube import YouTube


class TestCustomStreamQuery(unittest.TestCase):
    def setUp(self):
        self.yt = YouTube('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        self.all_streams = self.yt.streams

    def test_30fps(self):
        # Check if the stream with itag '136' is included
        self.assertTrue(any(stream.itag == 136 for stream in self.all_streams))

    def test_60fps(self):
        # Check if the stream with itag '303' is included
        self.assertTrue(any(stream.itag == 303 for stream in self.all_streams))


if __name__ == '__main__':
    unittest.main()
