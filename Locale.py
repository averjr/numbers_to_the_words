from abc import ABC, abstractmethod


class Locale(ABC):
    def __init__(self, ranked_whole, cents):
        pass

    @abstractmethod
    def get(self):
        pass
