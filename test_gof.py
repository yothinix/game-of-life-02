import unittest

from gof import get_neighbors_of


class GameOfLifeTest(unittest.TestCase):
    def test_get_neighbors_of_cell_03_should_return_set(self):
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


if __name__ == '__main__':
    unittest.main()
