import os
import unittest
from .day4 import solve_part1, solve_part2

class TestDay4(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Get the absolute path of the input file
        input_file_path = os.path.join(os.path.dirname(__file__), "test_input.txt")

        with open(input_file_path) as f:
            cls.test_input = [line.strip() for line in f.readlines()]

    def test_solve_part1(self):
        self.assertEqual(solve_part1(self.test_input), 0)  # Replace with actual expected result

    def test_solve_part2(self):
        self.assertEqual(solve_part2(self.test_input), 0)  # Replace with actual expected result

if __name__ == "__main__":
    unittest.main()