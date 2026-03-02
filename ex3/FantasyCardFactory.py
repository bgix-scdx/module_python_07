from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.main import damage as damageSpell
from ex0.main import color
from random import randint, seed


def add_elexir(val: int) -> None:
    color(f" 🌠 The elexir bestow {val} mana to everyone.",
          (255, 155, 255))
    return val


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.Cards = dict()
        self.Cards["creature"] = []
        self.Cards["spell"] = []
        self.Cards["artifact"] = []

    def create_creature(self, name_or_power:
                        str | int | None = None) -> CreatureCard:
        names = ["Dragon", "Giant", "Troll", "Bad Dragon", "Chicken",
                 "Evil Garden Gnome", "Fish", "Shark", "Trade Bro", "Equinox"]
        if name_or_power is None:
            color("A name or a stat is required to create a creature card.",
                  color=(255, 0, 0))
            return None
        elif isinstance(name_or_power, str):
            cost = randint(1, 20)
            damage = randint(1, 10)
            health = randint(1, 10)
            total = (damage + health) - cost
            rarity = "commun" if total <= 5 else "rare"
            rarity = rarity if total <= 10 else "epic"
            rarity = rarity if total <= 15 else "legendary"
            creature = CreatureCard(name_or_power, cost,
                                    rarity, damage, health)
            self.Cards["creature"].append(creature)
            return creature
        elif isinstance(name_or_power, int):
            seed(name_or_power)
            cost = randint(1, 20)
            damage = randint(1, 10)
            health = randint(1, 10)
            total = (damage + health) - cost
            rarity = "commun" if total <= 5 else "rare"
            rarity = rarity if total <= 10 else "epic"
            rarity = rarity if total <= 15 else "legendary"
            creature = CreatureCard(names[name_or_power % len(names)],
                                    cost, rarity, damage, health)
            return creature

    def create_spell(self, name_or_power:
                     str | int | None = None) -> SpellCard:
        names = ["Fireball", "Lazer Bean", "Antiheal", "Sharknado",
                 "Choclate Rain", "Raining Tacos", "Random Bullshit Go !"]
        if name_or_power is None:
            color("A name or a stat is required to create a spell card.",
                  color=(255, 0, 0))
            return None
        elif isinstance(name_or_power, str):
            cost = randint(1, 10)
            damage = randint(1, 10)
            total = damage - cost
            rarity = "commun" if total <= 3 else "rare"
            rarity = rarity if total <= 6 else "epic"
            rarity = rarity if total <= 8 else "legendary"
            creature = SpellCard(name_or_power, cost,
                                 rarity, damageSpell)
            self.Cards["spell"].append(creature)
            return creature
        elif isinstance(name_or_power, int):
            seed(name_or_power)
            cost = randint(1, 10)
            damage = randint(1, 10)
            total = damage - cost
            rarity = "commun" if total <= 3 else "rare"
            rarity = rarity if total <= 6 else "epic"
            rarity = rarity if total <= 8 else "legendary"
            creature = SpellCard(names[name_or_power % len(names)],
                                 cost, rarity, damageSpell)
            return creature

    def create_artifact(self, name_or_power:
                        str | int | None = None) -> ArtifactCard:
        names = ["Monkey Paw", "Donnut",
                 "KFC Chicken Bucket (sweet and sour sauce)", "Mana Dunk"]
        if name_or_power is None:
            color("A name or a stat is required to create a spell card.",
                  color=(255, 0, 0))
            return None
        elif isinstance(name_or_power, str):
            cost = randint(1, 10)
            damage = randint(1, 10)
            total = damage - cost
            rarity = "commun" if total <= 3 else "rare"
            rarity = rarity if total <= 6 else "epic"
            rarity = rarity if total <= 8 else "legendary"
            creature = ArtifactCard(name_or_power, cost,
                                    rarity, add_elexir)
            self.Cards["artifact"].append(creature)
            return creature
        elif isinstance(name_or_power, int):
            seed(name_or_power)
            cost = randint(1, 10)
            damage = randint(1, 10)
            total = damage - cost
            rarity = "commun" if total <= 3 else "rare"
            rarity = rarity if total <= 6 else "epic"
            rarity = rarity if total <= 8 else "legendary"
            creature = ArtifactCard(names[name_or_power % len(names)],
                                    cost, rarity, add_elexir)
            return creature

    def create_themed_deck(self, size: int) -> list:
        deck = []
        for i in range(size):
            card_type = randint(0, 2)
            if card_type == 0:
                deck.append(self.create_creature(randint(0, 100)))
            elif card_type == 1:
                deck.append(self.create_spell(randint(0, 100)))
            else:
                deck.append(self.create_artifact(randint(0, 100)))
        return deck

    def get_supported_types(self) -> list:
        return ["creature", "spell", "artifact", "themed_deck"]
