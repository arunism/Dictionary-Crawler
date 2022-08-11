from wmtk.base import BaseEngine
from wmtk.config import GOOGLE_CUSTOM_SEARCH_URL, GOOGLE_API_KEY, GOOGLE_SEARCH_ENGINE_ID
from wmtk.base import Request


class Google(BaseEngine):
    def __init__(self, key: str = None, delay: float = None, language: str = None) -> None:
        super(Google, self).__init__(key, delay, language)

    def search(self, query: str = '', category: str = 'search', cx: str = None):
        req = Request(
            url=GOOGLE_CUSTOM_SEARCH_URL,
            params={
                'q': query,
                'key': GOOGLE_API_KEY,
                'cx': GOOGLE_SEARCH_ENGINE_ID
            }
        )
        data = req.parse_text()
        return data
