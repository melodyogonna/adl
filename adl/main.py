from aiohttp import ClientSession, ClientResponse


class BaseDownloader:
    """Base Downloader class"""

    def __init__(self, link: str) -> None:
        self.client = ClientSession
        self.link = link
        self._set_headers()

    def download(self, download_provider: str) -> None:
        format = download_provider

    def _set_download_provider(self):
        pass

    async def _process_response(self, response: ClientResponse) -> ClientResponse:
        print("dkdkd")
        with open("response.html", "wb") as rf:
            while True:
                chunked_response = await response.content.read(10)
                print(chunked_response)
                if not chunked_response:
                    break
                rf.write(chunked_response)
        print(await response.text())
        return response

    async def _make_request(self) -> ClientResponse:
        async with self.client(headers=self.headers) as request:
            async with request.get(self.link) as response:
                await self._process_response(response)
                return response

    def _set_headers(self):
        self.headers = {"User-Agent": "Mozilla/5.0", "accept-language": "en-US,en"}

    async def make_request(self):
        return await self._make_request()
