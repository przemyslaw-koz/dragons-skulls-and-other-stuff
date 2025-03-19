import unittest
from io import StringIO
from unittest.mock import patch

from utils.map import find_longest_word, print_top


class TestMap(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_find_longest_word(self):
        result = find_longest_word(["test", "test1", "", "test11"])
        self.assertEqual(result, "test11")

    @patch("sys.stdout", new_callable=StringIO)
    def test_print_top(self, mock_stdout):
        print_top(40, "north")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(
            output,
            """┌────────────────────────────────────────┬────────────────────────────────────────┬────────────────────────────────────────┐
│                                        │               north (N)                │                                        │
├────────────────────────────────────────┼────────────────────────────────────────┼────────────────────────────────────────┤""",
        )


if __name__ == "__main__":
    unittest.main()
