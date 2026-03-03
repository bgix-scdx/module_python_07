from ex4.Rankable import Rankable
from ex2.Combatable import Combatable
from ex0.Card import Card
from ex0.main import color


class TournamentCard(Rankable, Combatable, Card):
    def __init__(self, name: str, cost: int, rarity: str):
        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self)
        Rankable.__init__(self)

    def play(self, game_stats):
        return super().play(game_stats)

    def calculate_rating(self) -> None:
        self.elo = (self.wins * 100 - self.loses * 50)
        color(f"{self.name}'s elo has changed: {self.elo} mmr", (255, 0, 0))
        self.get_rank_info()

    def update_wins(self, wins: int) -> None:
        self.wins += 1
        self.calculate_rating()

    def update_loses(self, loses: int) -> None:
        self.loses += 1
        self.calculate_rating()

    def get_rank_info(self) -> None:
        color(f"\n - {self.name}'s Stats", (255, 0, 255), bold=True)
        color(f"Victorys: {self.wins}", (0, 255, 0))
        color(f"Loses: {self.loses}", (255, 0, 0))
        color(f"MMR: {self.elo}", (255, 255, 0))

    def attack(self, target) -> None:
        if isinstance(target, TournamentCard):
            color(f" 🗡️  {self.name} is attacking {target.name} !"
                  f" -{self.damage}",
                  (255, 155, 0))
            self.attacks += 1
        else:
            color(f" 🗡️ {self.name} tryed to attack but missed !",
                  (255, 0, 0))

    def defend(self, incoming_damage: int) -> None:
        if isinstance(incoming_damage, int):
            color(f" 🛡️  {self.name} protected them selves from"
                  f" {incoming_damage} damage !",
                  (255, 155, 0))
            self.attacks += 1
            self.damage_defended += incoming_damage
        else:
            color(f" 🗡️ {self.name} tryed to protect them selves but failed!",
                  (255, 0, 0))

    def get_combat_stats(self) -> str:
        color(" ⚔️  Displaying fight statistics: \n"
              f"    Attacks: {self.attacks}\n"
              f"    Damages Defended: {self.damage_defended}", (255, 155, 0))
