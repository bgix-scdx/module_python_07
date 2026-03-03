from ex4.TournamentCard import TournamentCard
from random import randint
from ex0.main import color
saves = []
played = 0


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
        global played
        played += 1
        return winer

    def get_leaderboard() -> None:
        mini = None
        selected = None
        clonelist = saves.copy()
        color("\nDisplaying Leaderboard...", (255, 205, 155), bold=True)
        while len(clonelist) > 0:
            for i in clonelist:
                i = i[0]
                if (mini is None or i.elo > mini):
                    selected = i
                    mini = i.elo
            color(f"{selected.name}'s score: {selected.elo}", (255, 205, 0))
            clonelist.remove([selected])
            selected = None
            mini = None

    def generate_tournament_report() -> None:
        color(f"\nTotal Card: {len(saves)}", (255, 0, 205))
        color(f"Total played: {played}", (255, 0, 205))
        rating = sum(i[0].elo for i in saves) / len(saves)
        color(f"Total Rating: {rating}", (255, 0, 205))
        color("Status: Active", (255, 0, 205))
