from logo import print_logo_in
from player import Player
from world import world
from npc import talk
from colorama import init, Fore

def print_map(current):


def game_loop():
    player= Player("Bohater")
    print(Fore.GREEN+f"Witaj, {player.name}!" + Fore.RESET)
    while True:
        current = world[player.location]
        print(Fore.CYAN + f"\nJesteś w: {player.location}" + Fore.RESET)
        print(current["desc"])
        action= input("Co robisz ?").lower()
        if action in current["options"]:
            player.location = current["options"][action]
        else:
            print(Fore.YELLOW + talk(action) + Fore.RESET)

def main():
    print("Select Language")
    print("1. English")
    print("2. Polski")

    while True:
        choice = input("Enter your choice: ")

        if choice == '1':
            print_logo_in('en')
            break
        elif choice == '2':
            print_logo_in('pl')
            break

if __name__ == "__main__":
    main()
    game_loop()
