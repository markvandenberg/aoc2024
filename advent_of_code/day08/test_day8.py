import os
import unittest
from .day8 import solve_part1, solve_part2

class TestDay8(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        input_1_file_path = os.path.join(os.path.dirname(__file__), "test_input_1.txt")
        with open(input_1_file_path) as f:
            cls.test_input_1 = [line.strip() for line in f.readlines()]
        
        input_2_file_path = os.path.join(os.path.dirname(__file__), "test_input_2.txt")
        with open(input_2_file_path) as f:
            cls.test_input_2 = [line.strip() for line in f.readlines()]
        
        assert_answer_1_file_path = os.path.join(os.path.dirname(__file__), "assert_answer_1.txt")
        with open(assert_answer_1_file_path) as f:
            cls.assert_answer_1 = int(f.read())

        assert_answer_2_file_path = os.path.join(os.path.dirname(__file__), "assert_answer_2.txt")
        with open(assert_answer_2_file_path) as f:
            cls.assert_answer_2 = int(f.read())

    def test_solve_part1(self):
        self.assertEqual(solve_part1(self.test_input_1), self.assert_answer_1) 

    def test_solve_part2(self):
        self.assertEqual(solve_part2(self.test_input_2), self.assert_answer_2) 

if __name__ == "__main__":
    unittest.main()