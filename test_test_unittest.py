import unittest
from test import MazeSolution

class TestTest(unittest.TestCase):
    instance = MazeSolution()

    def test_sum(self):
        testgrid1 = [[0, 0, 0, 0, 1], [0, 1, 0, 1, 1], [0, 0, 1, 1, 1], [1, 1, 0, 1, 0]]
        assert self.instance.handle(testgrid1), "inf"

if __name__ == '__main__':
    unittest.main()