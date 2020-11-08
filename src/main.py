class BaseDownloader:
    """Base Downloader class"""

    def __init__(self, link: str) -> None:
        self.link = link

    def download(self, download_provider: str) -> None:
        format = download_provider

    def _set_download_provider(self):
        pass

    def _process_response(self):
        pass
