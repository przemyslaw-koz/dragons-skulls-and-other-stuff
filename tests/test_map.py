import pytest

from utils.map import find_longest_word, print_bottom, print_middle, print_top


def test_find_longest_word():
    assert find_longest_word(["test1", "test22", "test333"])


def test_print_top(capsys):
    print_top(8, "pn")
    captured = capsys.readouterr()
    assert (
        captured.out
        == "┌────────┬────────┬────────┐\n│        │ pn (N) │        │\n├────────┼────────┼────────┤\n"
    )


def test_print_top_empty(capsys):
    print_top(8, "")
    captured = capsys.readouterr()
    assert (
        captured.out
        == "┌────────┬────────┬────────┐\n│        │        │        │\n├────────┼────────┼────────┤\n"
    )


def test_print_middle_w_and_e(capsys):
    print_middle(8, "za", "ws")
    captured = capsys.readouterr()

    assert captured.out == "│ za (W) │   X    │ ws (E) │\n"


def test_print_middle_w(capsys):
    print_middle(8, "za", "")
    captured = capsys.readouterr()

    assert captured.out == "│ za (W) │   X    │        │\n"


def test_print_middle_e(capsys):
    print_middle(8, "", "ws")
    captured = capsys.readouterr()

    assert captured.out == "│        │   X    │ ws (E) │\n"


def test_print_middle_empty(capsys):
    print_middle(8, "", "")
    captured = capsys.readouterr()

    assert captured.out == "│        │   X    │        │\n"


def test_print_bottom(capsys):
    print_bottom(8, "pd")
    captured = capsys.readouterr()

    assert (
        captured.out
        == "├────────┼────────┼────────┤\n│        │ pd (S) │        │\n└────────┴────────┴────────┘\n"
    )


def test_print_bottom_empty(capsys):
    print_bottom(8, "")
    captured = capsys.readouterr()

    assert (
        captured.out
        == "├────────┼────────┼────────┤\n│        │        │        │\n└────────┴────────┴────────┘\n"
    )


def test_print_map():
    pass
    # directions = {"n": "", "s": "", "e": "", "w": ""}

    # for key in directions:
    #    directions[key] = current["options"].get(key, "")

    # print_top(40, directions["n"])
    # print_middle(40, directions["w"], directions["e"])
    # print_bottom(40, directions["s"])
