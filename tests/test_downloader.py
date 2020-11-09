# standard library
from unittest import TestCase
import asyncio

# Third party dependencies

# project libraries
from adl.main import BaseDownloader


class TestBaseDownloaderClass(TestCase):
    """This test file will test the methods provided by the Base Downloader
    class"""

    def setUp(self):
        url = "https://www.youtube.com/watch?v=y2TmhIw-HX0"
        self.adl = BaseDownloader(url)

    def test_make_request_method(self):
        """Tests the make request method"""
        make_request = self.adl.make_request
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(make_request)
        self.assertEqual(response.status, 200)
