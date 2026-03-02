from ex0.main import color


class GameEngine:
    def __init__(self, rounds) -> None:
        color("Starting Game Engine...", (255, 205, 155), bold=True)
        self.turns = rounds
        self.passedturns = 0

    def configure_engine(self, factory, strategy) -> None:
        color("Turn is starting:",
              (255, 0, 255))
        self.hand = factory.create_themed_deck(12)
        self.battlefield = []
        self.strategy = strategy
        color("Game engine configured !", (255, 205, 155), bold=True)

    def simulate_turn(self) -> None:
        self.strategy.execute_turn(self.hand, self.battlefield)
        self.passedturns += 1

    def get_engine_status(self) -> None:
        color("\nCurrent Game Status:", (255, 0, 255), bold=True)
        color(f"Hand: {[card.name for card in self.hand]}", (0, 255, 255))
        color(f"\nTurns: {self.passedturns}",
              (255, 255, 0))
