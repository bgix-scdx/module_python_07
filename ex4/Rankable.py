from abc import ABC, abstractmethod


class Rankable(ABC):
    def __init__(self) -> None:
        self.elo = 0
        self.wins = 0
        self.loses = 0

    @abstractmethod
    def calculate_rating(self) -> None:
        ...

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        ...

    @abstractmethod
    def update_loses(self, loses: int) -> None:
        ...

    def get_rank_info(self) -> None:
        ...
