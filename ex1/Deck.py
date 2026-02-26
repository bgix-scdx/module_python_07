from ex0.Card import Card
from ex0.main import color
from random import shuffle, choice


class Deck:
    def __init__(self, name: str) -> None:
        color(f" 🕹️  {name} has joined the game.",
              (155, 255, 155))
        self.name = name
        self.added = 0
        self.removed = 0
        self.shuffles = 0
        self.drawings = 0
        self.cards = {}

    def add_card(self, card: Card) -> None:
        color(f" 🆕  Adding {card.name} to {self.name}'s deck.",
              (155, 255, 155))
        self.added += 1
        self.cards.update({card.name: card})

    def remove_card(self, card_name) -> None:
        if self.cards.get(card_name):
            color(f" ➖  Removing {card_name} from {self.name}'s deck.",
                  (155, 255, 155))
            self.cards.pop(card_name)
            self.removed += 1
        else:
            color(" ⛔  You already dont have this card !",
                  (155, 255, 155))

    def shuffle(self) -> None:
        shuff = list(self.cards.items())
        shuffle(shuff)
        self.cards = dict(shuff)
        self.shuffles += 1
        color(f" 🎲  {self.name}'s deck was shuffled.",
              (155, 255, 155))
        color(f"     > {list(self.cards.keys())}",
              (155, 255, 155), bold=True)

    def draw_card(self) -> Card:
        name = choice(list(self.cards))
        self.drawings += 1
        color(f" 🎲  {self.name} has draw a new card !",
              (155, 255, 155))
        return self.cards.get(name)

    def get_deck_stats(self) -> None:
        color(f"\n 📊  Showing {self.name}'s stats: "
              f"\n     Card added: {self.added}"
              f"\n     Card removed: {self.removed}"
              f"\n     Current cards: {len(self.cards)}"
              f"\n     They draw {self.drawings} times from their dack"
              f"\n     Their deck was shuffled {self.shuffles} times.",
              (155, 255, 155))
