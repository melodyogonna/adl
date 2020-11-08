# standard library
from unittest import TestCase

# Third party dependencies

# project libraries
from main import BaseDownloader


class TestBaseDownloaderClass(TestCase):
    """This test file will test the methods provided by the Base Downloader
    class"""

    def test_class(self):
        url = "https://www.youtube.com/watch?v=y2TmhIw-HX0"
        self.assertEqual(1 + 1, 2)
