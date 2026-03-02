from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex0.main import color


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, damage: int = 1,
                 health: int = 1):
        super().__init__(name, cost, rarity)
        Combatable.__init__(self)
        Magical.__init__(self)
        self.damage = damage
        self.health = health

    def cast_spell(self, spell_name: str, targets: list) -> None:
        color(f" ☄️  {self.name} is casting {spell_name}",
              (0, 255, 255))
        if not isinstance(targets, list):
            color(" 💫 ut no target were found...",
                  (0, 255, 255))
            return
        for i in targets:
            if not isinstance(i, CreatureCard):
                color(f" 💫  Hit a {i}...", (0, 255, 255))
            else:
                color(f" ✴️  Damaged {i.name} !", (0, 255, 255))
            self.casted += 1

    def channel_mana(self, ammount: int) -> None:
        if type(ammount) is int:
            color(f" 🌟 {self.name} is channeling {ammount} mana", (0, 0, 255))
            self.managiven += ammount
            return ammount
        else:
            color(f" 🌟 {self.name} tryed to channel mana but he "
                  "failed", (0, 0, 255))

    def get_magic_stats(self) -> None:
        color(" 🪄  Displaying magic statistics: \n"
              f"    Mana Generated: {self.managiven}\n"
              f"    Spell casted: {self.casted}", (0, 255, 255))

    def attack(self, target) -> None:
        if isinstance(target, CreatureCard):
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

    def play(self, game_stats: dict):
        super().play(game_stats)

    def get_combat_stats(self) -> str:
        color(" ⚔️  Displaying fight statistics: \n"
              f"    Attacks: {self.attacks}\n"
              f"    Damages Defended: {self.damage_defended}", (255, 155, 0))
