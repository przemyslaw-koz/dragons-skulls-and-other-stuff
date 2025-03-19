from colorama import Fore, init

from utils.terminal import clear_screen

init(autoreset=True)

responses = {
    "cześć": "Witaj, młody wędrowcze!",
    "gdzie jestem?": "Jesteś w magicznej krainie",
}

npcs_data = {
    "Ailith Świetlista": {
        "desc": "Elficka bardka, która gra na harfie i opowiada historie o dawnych czasach.",
        "responses": {
            "Kim jesteś?": "Jestem Ailith, bardka i strażniczka dawnych opowieści.",
            "Opowiedz historię": "Dawno temu, wśród drzew tego lasu, żył smok, który strzegł pradawnej wiedzy...",
            "Co grasz?": "To pieśń o bohaterach, którzy wędrowali po świecie w poszukiwaniu magii.",
        },
    },
    "Lorien Zielonooki": {
        "desc": "Strażnik wioski, zawsze czujny, ale przyjazny dla podróżnych.",
        "responses": {
            "Kim jesteś?": "Jestem Lorien, strażnik tej wioski. Pilnuję, by nikt nie zakłócał jej spokoju.",
            "Czy to bezpieczne miejsce?": "Tak, dopóki ja tu jestem, nikt nie zrobi Wam krzywdy.",
            "Co sądzisz o elfickiej magii?": "To część naszej historii. Bez niej nie bylibyśmy tym, kim jesteśmy.",
        },
    },
}


def talk(player_input):
    return responses.get(player_input.lower(), "Nie rozumiem")


def talk_in(location):
    user_name = "Janek i Julek"
    print(Fore.YELLOW + "\n✨ **Porozmawiajmy z mieszkańcami wioski!** ✨\n")
    print("🔎 Wybierzcie kogoś, kto Was interesuje!\n")
    print(
        Fore.CYAN
        + "👥 Oto mieszkańcy, którzy mogą opowiedzieć Wam o tym magicznym miejscu:\n"
    )

    npcs = location["npcs"]

    for index, (npc_name, npc_desc) in enumerate(npcs.items(), 1):
        print(Fore.GREEN + "═════════════════════════════")
        print(Fore.GREEN + f" {index}. {npc_name}")
        print(Fore.GREEN + "═════════════════════════════")
        print(Fore.WHITE + f"  {npc_desc}\n")

    try:
        choice = int(
            input(
                Fore.YELLOW + "\n🎯 Wybierz numer postaci, z którą chcesz porozmawiać: "
            )
        )
    except ValueError:
        print(Fore.RED + "\n❌ Niepoprawny wybór. Wpisz numer!")
        return

    clear_screen()

    if 1 <= choice <= len(npcs):
        selected_npc_name = list(npcs.keys())[choice - 1]
        npc_data = npcs_data[selected_npc_name]

        available_questions = list(npc_data["responses"].keys())

        while True:
            clear_screen()
            print(Fore.MAGENTA + f"\n🎙️ {selected_npc_name} oczekuje na rozmowę!\n")
            print(Fore.YELLOW + "💬 Możecie zapytać o:\n")
            print(Fore.CYAN + "0. 🏃  Podziękujmy za rozmowę i pożegnajmy się.")

            for index, question in enumerate(available_questions):
                print(Fore.CYAN + f"{index + 1}. {question}")

            try:
                selected_question = int(
                    input(
                        Fore.YELLOW + "\n❓ O co chcecie zapytać młodzi łowcy przygód? "
                    )
                )
                if selected_question == 0:
                    print(
                        f"{user_name}: Dziękujemy za rozmowę! Musimy udać się w dalszą podróż. Do rychłego zobaczenia!"
                    )
                    print(
                        Fore.GREEN
                        + f"\n👋 {selected_npc_name}: 'Do zobaczenia, dzielni podróżnicy!'\n"
                    )
                    break
                elif 1 <= selected_question <= len(available_questions):
                    question_text = available_questions[selected_question - 1]
                    response = npc_data["responses"][question_text]

                    print(
                        Fore.LIGHTWHITE_EX + "\n╔════════════════════════════════════╗"
                    )
                    print(
                        Fore.LIGHTWHITE_EX
                        + f"║ 🎭 {user_name}: {Fore.YELLOW}{question_text}"
                    )
                    print(Fore.LIGHTWHITE_EX + "╚════════════════════════════════════╝")
                    print(
                        Fore.LIGHTBLUE_EX + "\n╔════════════════════════════════════╗"
                    )
                    print(
                        Fore.LIGHTBLUE_EX
                        + f"║ 🗣️ {selected_npc_name}: {Fore.WHITE}{response}"
                    )
                    print(
                        Fore.LIGHTBLUE_EX + "╚════════════════════════════════════╝\n"
                    )

                    input(
                        Fore.YELLOW + "\n🔹 Naciśnij ENTER, aby kontynuować rozmowę..."
                    )

                else:
                    print(Fore.RED + "\n❌ Nie rozumiem pytania, spróbuj ponownie!")
            except ValueError:
                print("\n❌ Wpisz numer pytania!")
    else:
        print("\n❌ Niepoprawny wybór. Sróbuj ponownie.")
