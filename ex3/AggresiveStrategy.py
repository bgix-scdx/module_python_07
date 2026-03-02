from ex3.GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.main import color


class AggressiveStrategy(GameStrategy):
    def __init__(self) -> None:
        self.turns = 0
        self.Mana = 5
        self.target = None
        self.battlefield = []

    def execute_turn(self, hand: list, battlefield: list) -> any:
        color(f"\nTurn {self.turns} is starting !\n", (255, 0, 255), bold=True)
        self.turns += 1
        mana = self.Mana + (self.turns * 5)
        max_cost = 0
        for i in hand:
            if i.get_card_info().get("cost") > max_cost:
                max_cost = i.get_card_info().get("cost")
        for cost in range(max_cost):
            for i in hand:
                if i.get_card_info().get("cost") == cost:
                    i.play({"available_mana": mana})
                    hand.remove(i)
                    battlefield.append(i)
                    mana -= i.get_card_info().get("cost")
                    if self.target is None and isinstance(i, CreatureCard):
                        self.target = i
        log = []
        for i in set(battlefield):
            if self.target is None:
                return hand, battlefield, log
            if isinstance(i, CreatureCard) and self.target is not i:
                i.attack_target(self.target)
            elif isinstance(i, SpellCard):
                i.activate_ability(self.target, 5)
            elif isinstance(i, ArtifactCard):
                self.mama = i.activate_ability(5)
            log.append(f"    {i.name} -> {self.target.name}")
            if self.target is not None and self.target.health <= 0:
                self.battlefield = battlefield
                self.battlefield.remove(self.target)
                self.prioritize_targets()
        return hand, battlefield, log

    def get_strategy_name(self) -> None:
        return "Aggressive"

    def prioritize_targets(self) -> None:
        self.target = None
        for i in self.battlefield:
            if isinstance(i, CreatureCard) and self.target is not i:
                self.target = i
                return
