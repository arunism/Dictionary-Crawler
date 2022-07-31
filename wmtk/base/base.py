class BaseEngine:
    def __init__(self, key: str) -> None:
        self.key = key

    @staticmethod
    def search(self, query, type='search'):
        return NotImplementedError
