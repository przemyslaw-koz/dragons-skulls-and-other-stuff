from colorama import Fore

from utils.map import print_map
from utils.terminal import clear_screen


def go_forward(current_location):
    while True:
        show_map_and_prompt(current_location)
        direction = get_user_direction()

        if direction in current_location["options"]:
            return move_to_new_location(direction, current_location)
        else:
            handle_invalid_direction()


def get_user_direction():
    return input(Fore.CYAN + "➡️  Wasz wybór: " + Fore.RESET).strip().lower()


def show_map_and_prompt(location):
    print(
        Fore.LIGHTBLUE_EX
        + "\n🗺️  Spoglądacie na mapę, szukając drogi naprzód..."
        + Fore.RESET
    )
    print_map(location)

    print(
        Fore.LIGHTWHITE_EX
        + "🌟 W którą stronę podążymy? Wybierzcie kierunek:"
        + Fore.RESET
    )


def move_to_new_location(direction, current_location):
    clear_screen()
    print(Fore.GREEN + f"🔜 Ruszamy w stronę: {direction.upper()}!" + Fore.RESET)
    return current_location["options"][direction]


def handle_invalid_direction():
    clear_screen()
    print(
        Fore.RED
        + "\n❌ O nie! Ten szlak wydaje się niebezpieczny lub zablokowany!"
        + Fore.RESET
    )
    print(
        Fore.YELLOW
        + "🔄 Sprawdźcie jeszcze raz mapę i spróbujcie innego kierunku."
        + Fore.RESET
    )
