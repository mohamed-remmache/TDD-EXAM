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
    

if __name__ == "__main__":
    unittest.main()
