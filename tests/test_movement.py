import pytest
from _pytest.monkeypatch import monkeypatch

from game.movement import get_user_direction, show_map_and_prompt


def test_go_forward():
    pass


#    while True:
#        show_map_and_prompt(current_location)
#        direction = get_user_direction()
#
#        if direction in current_location["options"]:
#            return move_to_new_location(direction, current_location)
#        else:
#            handle_invalid_direction()
#
#
@pytest.mark.parametrize(
    "user_input, expected_result",
    [(" NORTH ", "north"), ("SouTH", "south"), (" 1", "1"), ("", "")],
)
def test_get_user_direction(monkeypatch, user_input, expected_result):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    assert get_user_direction() == expected_result


#
def test_show_map_and_prompt(monkeypatch, capsys):
    expected_first_line = "\n🗺️  Spoglądacie na mapę, szukając drogi naprzód..."
    expected_second_line = "🌟 W którą stronę podążymy? Wybierzcie kierunek:"

    monkeypatch.setattr("utils.map.print_map", lambda _: None)

    monkeypatch.setattr("builtins.input", lambda _: "n")

    show_map_and_prompt({"options": {"n": "north"}})

    captured = capsys.readouterr()

    assert expected_first_line in captured.out
    assert expected_second_line in captured.out


#
# def move_to_new_location(direction, current_location):
#    clear_screen()
#    print(Fore.GREEN + f"🔜 Ruszamy w stronę: {direction.upper()}!" + Fore.RESET)
#    return current_location["options"][direction]
#
#
# def handle_invalid_direction():
#    clear_screen()
#    print(
#        Fore.RED
#        + "\n❌ O nie! Ten szlak wydaje się niebezpieczny lub zablokowany!"
#        + Fore.RESET
#    )
#    print(
#        Fore.YELLOW
#        + "🔄 Sprawdźcie jeszcze raz mapę i spróbujcie innego kierunku."
#        + Fore.RESET
