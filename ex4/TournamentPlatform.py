from ex4.TournamentCard import TournamentCard
from random import randint
from ex0.main import color


class TournamentPlatform:
    def register_card(card: TournamentCard) -> None:
        color(f"Registering {card.name}.{randint(0, 999)}", (255, 0, 0),
              bold=True)
        color(f"Skill Rating: {card.elo}", (255, 205, 155))
        color(f"Winrate {(card.wins / card.loses) * 100}", (255, 205, 155))

    def create_match(card_id: str, card2_id: str) -> str:
        pass

    def get_leaderboard() -> None:
        pass

    def generate_tournament_report() -> None:
        pass
