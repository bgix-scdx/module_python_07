from ex4.TournamentCard import TournamentCard
from random import randint
from ex0.main import color
saves = []


class TournamentPlatform:
    def register_card(card: TournamentCard) -> None:
        id = f"{card.name}_{randint(0, 999)}"
        color(f"Registering {id}", (255, 0, 0),
              bold=True)
        card.id = id
        color(f"Skill Rating: {card.elo}", (255, 205, 155))
        color(f"Winrate {(card.wins / (card.loses + 1)) * 100}%",
              (255, 205, 155))
        saves.append([card])

    def create_match(card1_id: str, card2_id: str) -> str:
        coinflip = randint(0, 1)
        for i in saves:
            if i[0].id == card1_id:
                card1_id = i[0]
            elif i[0].id == card2_id:
                card2_id = i[0]
        winer = card1_id if coinflip == 0 else card2_id
        loser = card2_id if coinflip == 0 else card1_id
        color(f"Match: {card1_id.id} vs {card2_id.id}", (255, 155, 205),
              bold=True)
        color(f"Winner: {winer.id}", (0, 155, 255))
        color(f"Loser: {loser.id}", (255, 155, 0))
        winer.update_wins(1)
        loser.update_loses(1)
        return winer

    def get_leaderboard() -> None:
        for i in saves:
            data = i[0]
            print(data.name)

    def generate_tournament_report() -> None:
        pass
