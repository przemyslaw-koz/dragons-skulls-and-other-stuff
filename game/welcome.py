from game.logo import print_logo_in

def print_welcome():
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
