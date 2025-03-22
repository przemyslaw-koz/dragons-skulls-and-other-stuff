import time

from colorama import Fore

from game.npc import talk
from game.player import Player
from game.player_actions import get_player_actions, print_basic_actions
from game.welcome import print_welcome
from repository.tiny_db_repo import TinyDBWorldRepository
from utils.terminal import clear_screen


def game_loop(repository):
    player = Player("JANEK I JULEK")
    basic_actions = get_player_actions()

    print(Fore.GREEN + f"\n🌟 Witajcie, {player.name}! 🌟" + Fore.RESET)

    time.sleep(2)

    while True:
        current = repository.get_location(player.location)

        print(
            Fore.CYAN
            + f"\n📍 Jesteście w miejscu znanym jako: {player.location}"
            + Fore.RESET
        )
        print("\n" + Fore.LIGHTYELLOW_EX + current["desc"] + Fore.RESET + "\n")

        print()
        print(Fore.MAGENTA + "✨ Co dalej, dzielni podróżnicy? ✨" + Fore.RESET)
        print(
            Fore.LIGHTWHITE_EX
            + "Wybierzcie kolejną akcję, podając jej numer:"
            + Fore.RESET
        )
        print()
        print_basic_actions()
        print()

        action = input(Fore.CYAN + "🔮 Wasz wybór: " + Fore.RESET).strip().lower()

        clear_screen()

        if action in basic_actions:
            # TODO: change it to use location name and inside method send request to db if needed
            new_location = basic_actions[action](current)
            if new_location:
                player.location = new_location
        else:
            print(Fore.YELLOW + talk(action) + Fore.RESET)


if __name__ == "__main__":
    repo = TinyDBWorldRepository("./db/world.json")
    print_welcome()
    game_loop(repo)
