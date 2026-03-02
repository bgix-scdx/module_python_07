from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggresiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


if __name__ == "__main__":
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine(6)
    engine.configure_engine(factory, strategy)
    engine.get_engine_status()
    for _ in range(engine.turns):
        engine.simulate_turn()
    engine.get_engine_status()
