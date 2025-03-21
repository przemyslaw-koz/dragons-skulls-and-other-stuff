import pytest

from game.movement import (
    get_user_direction,
    go_forward,
    handle_invalid_direction,
    move_to_new_location,
    show_map_and_prompt,
)


def test_go_forward(monkeypatch):
    current_location = {"options": {"n": "north", "e": "east"}}

    directions = iter(["z", "z", "n"])
    monkeypatch.setattr("game.movement.get_user_direction", lambda: next(directions))

    monkeypatch.setattr(
        "game.movement.move_to_new_location", lambda d, l: l["options"][d]
    )

    monkeypatch.setattr("game.movement.handle_invalid_direction", lambda: None)

    result = go_forward(current_location)

    assert result == "north"


@pytest.mark.parametrize(
    "user_input, expected_result",
    [(" NORTH ", "north"), ("SouTH", "south"), (" 1", "1"), ("", "")],
)
def test_get_user_direction(monkeypatch, user_input, expected_result):
    monkeypatch.setattr("builtins.input", lambda _: user_input)

    assert get_user_direction() == expected_result


def test_show_map_and_prompt(monkeypatch, capsys):
    expected_first_line = "\n🗺️  Spoglądacie na mapę, szukając drogi naprzód..."
    expected_second_line = "🌟 W którą stronę podążymy? Wybierzcie kierunek:"

    monkeypatch.setattr("utils.map.print_map", lambda _: None)
    monkeypatch.setattr("builtins.input", lambda _: "n")

    show_map_and_prompt({"options": {"n": "north"}})

    captured = capsys.readouterr()

    assert expected_first_line in captured.out
    assert expected_second_line in captured.out


def test_move_to_new_location(capsys):
    direction = "n"
    expected_text = f"🔜 Ruszamy w stronę: {direction.upper()}!"
    current_location = {"options": {"n": "north", "e": "east"}}

    assert move_to_new_location(direction, current_location) == "north"

    captured = capsys.readouterr()
    assert expected_text in captured.out


def test_handle_invalid_direction(capsys):
    expected_first_line = (
        "\n❌ O nie! Ten szlak wydaje się niebezpieczny lub zablokowany!"
    )
    expected_second_line = (
        "🔄 Sprawdźcie jeszcze raz mapę i spróbujcie innego kierunku."
    )

    handle_invalid_direction()

    captured = capsys.readouterr()

    assert expected_first_line in captured.out
    assert expected_second_line in captured.out
