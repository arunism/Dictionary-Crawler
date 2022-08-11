import requests
from builtins import str
from typing import Dict


class BaseEngine:
    def __init__(self, key: str = None, delay: float = None, language: str = 'en') -> None:
        self.key = key
        self.delay = delay
        self.language = language

    @staticmethod
    def search(self, query: str = '', category: str = 'search'):
        return NotImplementedError


class Request:
    def __init__(self, url: str, params: Dict[str, str] = {}) -> None:
        self.url = url
        self.params = params

    def parse_text(self) -> Dict:
        data = requests.get(self.url, self.params).json()
        return data
