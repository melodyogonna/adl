from aiohttp import ClientSession


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

    async def _make_request(self):
        async with ClientSession() as request:
            async with request.get(self.link) as response:
                return response

    def _set_headers(self):
        pass

    @property
    async def make_request(self):
        return await self._make_request()
