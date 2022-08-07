class BaseEngine:
    def __init__(self, key: str = None, delay: float = None, language: str = 'en') -> None:
        self.key = key
        self.delay = delay
        self.language = language

    @staticmethod
    def search(self, query: str = '', category: str = 'search'):
        return NotImplementedError


class URL:
    def __init__(
            self,
            template: dict = {}
    ) -> None:
        pass
