from colorama import Fore

from utils.map import print_map
from utils.terminal import clear_screen


def go_forward(current_location):
    while True:
        print(Fore.LIGHTBLUE_EX + "\n🗺️  Spoglądacie na mapę, szukając drogi naprzód..." + Fore.RESET)
        print_map(current_location)

        print(Fore.LIGHTWHITE_EX + "🌟 W którą stronę podążymy? Wybierzcie kierunek:" + Fore.RESET)
        direction = input(Fore.CYAN + "➡️  Wasz wybór: " + Fore.RESET).strip().lower()

        if direction in current_location["options"]:
            clear_screen()
            print(Fore.GREEN + f"🔜 Ruszamy w stronę: {direction.upper()}!" + Fore.RESET)
            return current_location["options"][direction]
        else:
            clear_screen()
            print(Fore.RED + "\n❌ O nie! Ten szlak wydaje się niebezpieczny lub zablokowany!" + Fore.RESET)
            print(Fore.YELLOW + "🔄 Sprawdźcie jeszcze raz mapę i spróbujcie innego kierunku." + Fore.RESET)

