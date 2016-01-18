""" tests for board """
import unittest
from src.queen import Queen
from src.board import Board 

class TestQueenMethods(unittest.TestCase):
    """testing methods for board"""
    def setUp(self):
        self.board = Board(2, 2)

    def test_valid_moves(self):
        """testing queen's valid moves"""
        queen = Queen()
        self.board.set_tile(1, 0, 0)
        valid_moves_2 = queen.valid_moves(self.board)
        self.assertEqual(len(valid_moves_2), 3)
        self.board = Board(3, 3)
        self.board.set_tile(1, 0, 0)
        valid_moves_3 = queen.valid_moves(self.board)
        self.assertEqual(len(valid_moves_3), 6)
    def test_moves(self):
        """testing queen's invalid moves"""
        queen = Queen()
        self.board = Board(10, 10)
        queen.set_position(5, 5)
        self.board.set_tile(1, 5, 5)
        valid_moves_4 = queen.valid_moves(self.board)
        self.assertEqual(len(valid_moves_4), 35)


if __name__ == "__main__":
    unittest.main()
