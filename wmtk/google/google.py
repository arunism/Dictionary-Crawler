import requests
from wmtk.base import BaseEngine
from wmtk.config import GOOGLE_CUSTOM_SEARCH_URL, GOOGLE_API_KEY, GOOGLE_SEARCH_ENGINE_ID


class Google(BaseEngine):
    def __init__(self, key: str = None, delay: float = None, language: str = None) -> None:
        super(Google, self).__init__(key, delay, language)

    def search(self, query: str = '', category: str = 'search', cx: str = None):
        data = requests.get(
            url=GOOGLE_CUSTOM_SEARCH_URL,
            params={
                'key': GOOGLE_API_KEY,
                'cx': GOOGLE_SEARCH_ENGINE_ID,
                'q': query
            }
        ).json()
        return data
