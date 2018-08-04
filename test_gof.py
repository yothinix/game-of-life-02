import unittest

from gof import get_neighbors_of, rule_1, rule_2


class GameOfLifeTest(unittest.TestCase):
    def setUp(self):
        self.neighbors = {
            (0, 0), (0, 1), (0, 2),
            (1, 2), (1, 0), (2, 0),
            (2, 1), (2, 2)
        }

        self.center = (1, 1)

    def test_get_neighbors_of_cell_should_return_one(self):
        cell = (0, 3)

        result = get_neighbors_of(cell)

        expected = {
            (0, 2),
            (0, 4),
            (1, 2),
            (1, 3),
            (1, 4),
            (-1, 2),
            (-1, 3),
            (-1, 4)
        }
        self.assertEqual(result, expected)

    def test_get_neighbors_of_cell_14_should_return_set(self):
        cell = (1, 4)

        result = get_neighbors_of(cell)

        expected = {
            (0, 3),
            (0, 5),
            (0, 4),
            (1, 3),
            (1, 5),
            (2, 3),
            (2, 4),
            (2, 5)
        }
        self.assertEqual(result, expected)

    def test_neighbors_less_than_2_should_return_cell_died(self):
        board = {(1, 1), (0, 2)}
        expected = {(0, 2)}

        result = rule_1(board, self.center, self.neighbors)

        self.assertEqual(result, expected)

    def test_cell_has_two_neighbors_should_return_cell_alive(self):
        board = {(1, 1), (0, 0), (2, 2)}
        expected = {(1, 1), (0, 0), (2, 2)}

        result = rule_2(board, self.center, self.neighbors)

        self.assertEqual(result, expected)

    def test_cell_has_three_neighbors_should_return_cell_alive(self):
        board = {(1, 1), (0, 0), (0, 2), (2, 2)}
        expected = {(1, 1), (0, 0), (0, 2), (2, 2)}

        result = rule_2(board, self.center, self.neighbors)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
