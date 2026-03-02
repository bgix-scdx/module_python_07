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
        cost = self.get_card_info().get("cost")
        color("")
        if self.is_playable(game_stats.get("available_mana")):
            color(f" 🔥 {self.name} was summmon on the battle field !"
                  f"for {cost} mana",
                  (255, 0, 0))
            color(f" 📜 Revealing stats: {self.get_card_info()}",
                  (0, 255, 255))
            self.played = True
            return game_stats.get("available_mana") - cost
        else:
            color(f" 🫗  You can not summon '{self.name}' yet. "
                  f"({game_stats.get("available_mana")} / {cost})",
                  (0, 0, 255))
            return game_stats.get("available_mana")

    def get_card_info(self) -> dict:
        return {"name": self.name,
                "cost": self.__cost,
                "rarity": self.__rarity}

    def is_playable(self, available_mana: int) -> bool:
        try:
            return (True if available_mana >= self.__cost else False)
        except TypeError:
            return (False)
