from ex4.Rankable import Rankable
from ex2.Combatable import Combatable
from ex0.Card import Card


class TournamentCard(Rankable, Combatable, Card):
    def __init__(self, name: str, cost: int, rarity: str):
        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self)
        Rankable.__init__(self)

    def play(self, game_stats):
        return super().play(game_stats)

    def calculate_rating(self) -> None:
        self.elo = (self.wins * 4 - self.loses * 2) + 1
        print(self.elo)

    def update_wins(self, wins: int) -> None:
        self.wins += 1
        self.calculate_rating()

    def update_loses(self, loses: int) -> None:
        self.loses += 1
        self.calculate_rating()

    def get_rank_info(self) -> None:
        ...

    def attack(self, target) -> None:
        ...

    def defend(self, incoming_damage: int) -> None:
        ...

    def get_combat_stats(self) -> str:
        ...
