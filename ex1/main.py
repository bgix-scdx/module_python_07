from ex0 import CreatureCard, color
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck


def damage(target, damage) -> None:
    color(f" ⛈️  Damaging {damage} health of {target.name} !",
          (255, 255, 0))
    try:
        target.health -= damage
    except ValueError:
        color(" 🌧️  But it failed !",
              (255, 255, 0))


def strike(target: CreatureCard, damage) -> None:
    color(f" ⛈️  Striking down {damage} health of {target.name} !",
          (255, 255, 0))
    try:
        target.health -= damage
    except ValueError:
        color(" 🌧️  But it failed !",
              (255, 255, 0))


if __name__ == "__main__":
    mana = 15

    def add_elexir(val: int) -> None:
        color(f" 🌠 The elexir bestow {val} mana to everyone.",
              (255, 155, 255))
        global mana
        mana += val

    deck = Deck("sharkys")
    elexir = ArtifactCard("Elexir", 10, "Common", 0, add_elexir)
    elexir2 = ArtifactCard("Advanced Elexir", 10, "Common", 0, add_elexir)
    spell = SpellCard("Thunderous Strike", 5, "rare", strike)
    goblin = CreatureCard("Goblin", 0, "common", 1, 5)

    deck.add_card(spell)
    deck.add_card(elexir)

    mana = spell.play({"available_mana": mana})
    mana = elexir.play({"available_mana": mana})
    mana = elexir.play({"available_mana": mana})
    elexir.activate_ability(10)
    spell.activate_ability(goblin, 5)
    spell.activate_ability(goblin, 5)

    deck.shuffle()
    deck.shuffle()
    deck.shuffle()
    print()
    color(f"     {deck.draw_card().name}",
          (255, 255, 155))

    mana = elexir2.play({"available_mana": mana})
    deck.remove_card("Thunderous Strike")
    deck.remove_card("Bakus Amogus")
    print()
    elexir.activate_ability(10)
    deck.shuffle()
    deck.get_deck_stats()
