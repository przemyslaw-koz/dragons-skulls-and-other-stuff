responses = {
    "cześć": "Witaj, młody wędrowcze!",
    "gdzie jestem?": "Jesteś w magicznej krainie",
}


def talk(player_input):
    return responses.get(player_input.lower(), "Nie rozumiem")


def talk_in(location):
    print("\n✨ **Porozmawiajmy z mieszkańcami wioski!** ✨")
    print(
        "Wybierzcie kogoś, kto Was interesuje, kierując się ich opisami. Być może imiona zdradzą Wam w trakcie rozmowy."
    )
    print("\nOto mieszkańcy, którzy mogą opowiedzieć Wam o tym magicznym miejscu:")

    npcs = location["npcs"]

    for index, (npc_name, npc_desc) in enumerate(npcs.items(), 1):
        print(f"\n🌟 **Postać {index}:**")
        print(f"  - {npc_desc}")

    choice = int(input("\nWybierz numer postaci, z którą chcesz porozmawiać"))

    if 1 <= choice <= len(npcs):
        pass
        # selected_npc_name = list(npcs.keys())[choice - 1]
        # selected_npc_desc = npcs[selected_npc_name]
        # print(f"\n🌟 **Zaczynasz rozmowę z {selected_npc_name}:**")
        # print(f"  - {selected_npc_desc}")
        # print(
        #   f"  {selected_npc_name}: 'Witaj, podróżniku! Cieszę się, że zechciałeś ze mną porozmawiać!'"
        # )
    else:
        print("\n❌ Niepoprawny wybór. Spróbuj ponownie.")
