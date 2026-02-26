from abc import ABC, abstractmethod
from ex0.main import color


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        try:
            if int(cost) > 0:
                self.name = name
                self.__cost = int(cost)
                self.__rarity = rarity
        except ValueError as err:
            color(f"/!\\ > Card '{name}' could not be created: {err}",
                  (255, 0, 0))
            return
        color(f" - Card '{name}' was created.",
              (0, 255, 0))

    @abstractmethod
    def play(self, game_stats: dict) -> dict:
        ...

    def get_card_info(self) -> dict:
        return {"name": self.name,
                "cost": self.__cost,
                "rarity": self.__rarity}

    def is_playable(self, available_mana: int) -> bool:
        try:
            return (True if available_mana >= self.__cost else False)
        except TypeError:
            return (False)
