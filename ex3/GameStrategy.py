from abc import ABC, abstractmethod


class GameStrategy(ABC):
    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> any:
        ...

    @abstractmethod
    def get_strategy_name(self) -> None:
        ...

    @abstractmethod
    def prioritize_targets(self) -> None:
        ...
