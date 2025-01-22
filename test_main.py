import unittest
from main import move_rover
class TestMoveRover(unittest.TestCase):
    def test_basic_case(self):
        grid = (5, 5)
        position = (1, 2, 'N')
        commands = "LMLMLMLMM"
        expected = (1, 3, 'N')
        self.assertEqual(move_rover(grid, position, commands), expected)

    
    def test_advanced_case(self):
        grid = (5, 5)
        position = (3, 3, 'E')
        commands = "MMRMMRMRRM"
        expected = (5, 1, 'E')
        self.assertEqual(move_rover(grid, position, commands), expected)

    def test_rover_hits_grid_limit(self):
        grid = (5, 5)
        position = (4, 4, 'N')
        commands = "MMMM"
        expected = (4, 5, 'N')  # Le rover ne peut pas dépasser la limite supérieure.
        self.assertEqual(move_rover(grid, position, commands), expected)

    def test_no_commands(self):
        grid = (5, 5)
        position = (2, 2, 'E')
        commands = ""
        expected = (2, 2, 'E')  # Le rover reste sur place.
        self.assertEqual(move_rover(grid, position, commands), expected)

    def test_invalid_commands(self):
        grid = (5, 5)
        position = (1, 2, 'S')
        commands = "MMXLRM"  # 'X' est une commande invalide.
        with self.assertRaises(ValueError):  # On attend une exception pour une commande invalide.
            move_rover(grid, position, commands)


if __name__ == "__main__":
    unittest.main()
