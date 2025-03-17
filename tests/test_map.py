import unittest
from io import StringIO
from unittest.mock import patch
from utils.map import find_longest_word
from utils.map import print_all_locations

class TestMap(unittest.TestCase):
    def test_find_longest_word(self):
        result= find_longest_word(["test", "test1", "", "test11"])
        self.assertEqual(result, "test11")

    @patch("sys.stdout", new_callable=StringIO)
    def test_location_printing(self, mock_stdout):
        print_all_locations(["location1", "location2", "location3", "location4"])
        output= mock_stdout.getvalue().strip()
        self.assertEqual(output, "[ location1 ][ location2 ][ location3 ][ location4 ]")

if __name__ == "__main__":
    unittest.main()

