from ex1 import Card, color


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 duration: int = None, ability: callable = None) -> None:
        super().__init__(name, cost, rarity)
        self.duration = duration
        self.lifespan = 0
        self.active = ability

    def play(self, game_stats: dict) -> int:
        cost = self.get_card_info().get("cost")
        color("")
        if self.is_playable(game_stats.get("available_mana")):
            color(f" 🪬  {self.name} was summmon on the battle field "
                  f" for {cost} mana",
                  (255, 0, 255))
            color(f" 📜 Revealing stats: {self.get_card_info()}",
                  (0, 255, 255))
            self.played = True
            return game_stats.get("available_mana") - cost
        else:
            color(f" 🔮  You can not summon '{self.name}' yet. "
                  f"({game_stats.get("available_mana")} / {cost})",
                  (0, 0, 255))
            return game_stats.get("available_mana")

    def activate_ability(self, args) -> None:
        color(f" 🔮 {self.name}'s effect biggins !",
              (255, 0, 255))
        if self.active is None or self.duration < self.lifespan:
            color(" 🥀 But it expired.",
                  (255, 0, 255))
        else:
            self.lifespan += 1
            self.active(args)
