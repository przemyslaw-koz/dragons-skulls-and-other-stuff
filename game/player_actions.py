from game.item import pick_item_in
from game.movement import go_forward
from game.npc import talk_in


def get_player_actions():
    return {"1": go_forward, "2": talk_in, "3": pick_item_in}


def print_basic_actions():
    print("🎒  1. Ruszam na przygodę!")
    print("🗣   2. Ktoś tu jest! Pogadam z nim!")
    print("🔍  3. Ooo! Coś tu leży! Sprawdzę!")
