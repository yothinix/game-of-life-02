import unittest

from gof import get_neighbors_of, rule_1


class GameOfLifeTest(unittest.TestCase):
    def test_get_neighbors_of_cell_should_return_one(self):
        cell = (0, 3)
        result = get_neighbors_of(cell)
        self.assertEqual(result, 1)

    def test_neighbors_less_than_2_should_return_cell_died(self):
        neighbors = {
            (0, 0), (0, 1), (0, 2),
            (1, 2), (1, 0), (2, 0),
            (2, 1), (2, 2)
        }
        board = {(1, 1), (0, 2)}
        center = (1, 1)
        expected = {(0, 2)}

        result = rule_1(board, center, neighbors)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
