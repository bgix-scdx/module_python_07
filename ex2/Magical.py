from abc import ABC, abstractmethod


class Magical(ABC):
    def __init__(self):
        self.managiven = 0
        self.casted = 0

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> None:
        ...

    @abstractmethod
    def channel_mana(self, ammount: int) -> None:
        ...

    @abstractmethod
    def get_magic_stats(self) -> str:
        ...
