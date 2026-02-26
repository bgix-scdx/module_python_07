def color(message: any, tcol: tuple = (255, 255, 255),
          bcol: tuple = None,
          bold: bool = False, ita: bool = False, under: bool = False,
          finish: str = '\n', f: any = None) -> None:
    if tcol is None:
        tcol = (255, 255, 255)
    style = "1;" if bold else ""
    italic = "3;" if ita else ""
    underline = "4;" if under else ""
    bcolor = f"48;2;{bcol[0]};{bcol[1]};{bcol[2]}" if bcol else ""
    style = style+italic+underline+bcolor
    if (type(message) is dict or type(message) is list):
        for mes in message:
            print(f"\033[{style}38;2;{tcol[0]};{tcol[1]};{tcol[2]}"
                  f"m{mes}\033[0m", end=finish, file=f)
            print("")
    else:
        print(f"\033[{style}38;2;{tcol[0]};{tcol[1]};{tcol[2]}"
              f"m{message}\033[0m",
              end=finish, file=f)


if __name__ == "__main__":
    from ex0.CreatureCard import CreatureCard
    color("=== DataDeck Card Foundation ===",
          (255, 0, 0), bold=True)
    mana = 100
    card = CreatureCard("Bakus mogus", 55, "Legendary", 15, 20)
    enemy = CreatureCard("Sussy", 15, "common", 10, 18)
    mana = card.play({"available_mana": mana})
    mana = card.play({"available_mana": mana})
    color(f" ❔ Double checking playability: {card.is_playable(mana)}",
          (0, 155, 155))
    mana = enemy.play({"available_mana": mana})
    print("")
    enemy.attack_target(card)
    card.attack_target(enemy)
    enemy.attack_target(card)
