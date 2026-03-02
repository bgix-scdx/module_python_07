from abc import ABC, abstractmethod


class Combatable(ABC):
    def __init__(self):
        self.attacks = 0
        self.damage_defended = 0

    @abstractmethod
    def attack(self, target) -> None:
        ...

    @abstractmethod
    def defend(self, incoming_damage: int) -> None:
        ...

    @abstractmethod
    def get_combat_stats(self) -> str:
        ...
