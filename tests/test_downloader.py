# standard library
from unittest import TestCase
import asyncio

# Third party dependencies

# project libraries
from adl.main import BaseDownloader

loop = asyncio.get_event_loop()


class TestBaseDownloaderClass(TestCase):
    """This test file will test the methods provided by the Base Downloader
    class"""

    def setUp(self):
        url = "https://www.youtube.com/watch?v=y2TmhIw-HX0"
        self.adl = BaseDownloader(url)

    def test_make_request_method(self):
        """Tests the make request method"""
        make_request = self.adl.make_request()
        response = loop.run_until_complete(make_request)
        self.assertEqual(response.status, 200)

    def test_process_response_method(self):
        make_request = loop.run_until_complete(self.adl.make_request())
        self.assertEqual(make_request, 10)
