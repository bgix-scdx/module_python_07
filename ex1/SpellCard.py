from ex1 import Card, color


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 ability: callable = None) -> None:
        super().__init__(name, cost, rarity)
        self.effect = ability

    def play(self, game_stats: dict) -> int:
        cost = self.get_card_info().get("cost")
        color("")
        if self.is_playable(game_stats.get("available_mana")):
            color(f" 📖  {self.name} has been set up  "
                  f"for {cost} mana",
                  (255, 255, 0))
            color(f" 📜 Revealing stats: {self.get_card_info()}",
                  (0, 255, 255))
            self.played = True
            return game_stats.get("available_mana") - cost
        else:
            color(f" 📕  You can not summon '{self.name}' yet. "
                  f"({game_stats.get("available_mana")} / {cost})",
                  (0, 0, 255))
            return game_stats.get("available_mana")

    def activate_ability(self, target, value):
        color(f" 📜 {self.name}'s ink biggins to glow !",
              (255, 255, 0))
        if self.effect is None:
            color(" ✨ But it failed.",
                  (255, 255, 0))
        else:
            self.effect(target, value)
            self.effect = None
