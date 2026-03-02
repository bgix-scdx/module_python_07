from ex2.EliteCard import EliteCard
from ex0.CreatureCard import CreatureCard

if __name__ == "__main__":
    card = EliteCard("Shark", 1, "Mythical", 5)
    enemy = CreatureCard("Dummy", 1, "None", 1, 50)
    card.play({"available_mana": 50})
    card.cast_spell("Blub blub", [enemy])
    card.channel_mana(69)
    card.channel_mana("Blub")
    print()
    card.get_magic_stats()
    print()
    card.attack(enemy)
    card.defend(5)
    print()
    card.get_combat_stats()
