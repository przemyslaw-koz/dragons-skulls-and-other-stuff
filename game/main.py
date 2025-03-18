import os
import time
from game.logo import clear_sreen, print_logo_in
from game.player import Player
from game.world import world
from game.npc import talk
from colorama import init, Fore
from utils.map import print_map

def go_forward(current_location):
    direction=input("Dokąd się udajemy? ")

    if direction in current_location["options"]:
        return current_location["options"][direction]
    else:
        print("Chyba się pogubiliśmy! W tym kierunku nie możemy się udać! Spójrzmy jeszcze raz na mapę")
        return ""


def talk_to_npc(current_location):
    print("Pozmawiam z miejscowymi!")

def pick_item(current_location):
    print("Sprawdzam, co tu jest!")

def clear_screen():
    os.system("clear")

def game_loop():
    player= Player("JANEK I JULEK")
    basic_actions= {
        "1": go_forward,
        "2": talk_to_npc,
        "3": pick_item
    }

    print(Fore.GREEN + f"\n🌟 Witajcie, {player.name}! 🌟" + Fore.RESET)

    time.sleep(2)

    while True:
        current = world[player.location]

        #clear_sreen()

    #    print(current)

        print(Fore.CYAN + f"\n📍 Jesteście w: {player.location}" + Fore.RESET)
        print("\n" + Fore.LIGHTYELLOW_EX + current["desc"] + Fore.RESET + "\n")
        print_map(current)

        print_basic_actions()
        print()
        action= input("Co chcecie zrobić? Wpiszcie numer akcji: ").lower()
        
        if action in basic_actions:
            new_location=basic_actions[action](current)
            current = world[new_location]
            player.location=new_location

        #else:
         #   print(Fore.YELLOW + talk(action) + Fore.RESET)

def print_basic_actions():
    print("🎒  1. Ruszam na przygodę!")
    print("🗣   2. Ktoś tu jest! Pogadam z nim!")
    print("🔍  3. Ooo! Coś tu leży! Sprawdzę!")

def main():
    print("═════════════════════════════════")
    print("🌍  WITAJ W ŚWIECIE PRZYGÓD!  🌍")
    print("═════════════════════════════════")
    print("\nWybierz język:")
    print("1. English 🇬 🇧")
    print("2. Polski 🇵 🇱")

    while True:
        choice = input("🎮 Wpisz swój wybór: ")

        if choice == '1':
            print_logo_in('en')
            break
        elif choice == '2':
            print_logo_in('pl')
            break

if __name__ == "__main__":
    main()
    game_loop()
