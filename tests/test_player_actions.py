from game.player_actions import print_basic_actions


def test_print_basic_actions(capsys):
    print_basic_actions()

    captured = capsys.readouterr()

    assert "🎒  1. Ruszam na przygodę!" in captured.out
    assert "🗣   2. Ktoś tu jest! Pogadam z nim!" in captured.out
    assert "🔍  3. Ooo! Coś tu leży! Sprawdzę!" in captured.out
