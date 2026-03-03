from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard
from ex0.main import color


if __name__ == "__main__":
    card1 = TournamentCard("Sussy Baka", 5, "Baka")
    card2 = TournamentCard("Paul", 1, "Supas")
    TournamentPlatform.register_card(card1)
    TournamentPlatform.register_card(card2)
    TournamentPlatform.create_match(card1.id, card2.id)
    TournamentPlatform.get_leaderboard()
    TournamentPlatform.generate_tournament_report()
    color("\nEnd of Tournament", (255, 0, 255), bold=True)
