from ex0.Card import Card
from ex0.main import color


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 dmg: int = 1, health: int = 5) -> None:
        super().__init__(name, cost, rarity)
        self.health = health
        self.damage = dmg
        self.name = name
        self.played = False

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

    def attack_target(self, target: Card) -> None:
        targ_data: CreatureCard = target
        if targ_data.health > 0:
            if targ_data.health - self.damage <= 0:
                color(f" 💥 Fatal Blow ! {targ_data.name} has been "
                      f"down by {self.name} !",
                      (255, 0, 0))
                targ_data.health = 0
            else:
                color(f" 💢 {targ_data.name} has been attacked by"
                      f" {self.name} ! [{targ_data.health - self.damage}]",
                      (255, 155, 155))
                targ_data.health -= self.damage
        else:
            color(f"{targ_data.get("name")} is already down !")
