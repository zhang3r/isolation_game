""" tests for board """
import unittest
from src.board import Board 

class TestBoardMethods(unittest.TestCase):
    """testing methods for board"""
    def setUp(self):
        self.board = Board(2, 2)

    def test_creation(self):
        """testing board creationg"""
        my_board = Board(2, 2)
        self.assertTrue(my_board.width == 2)
        self.assertTrue(my_board.width == my_board.height)
        self.assertEqual(my_board.get_tile(X=0, Y=0), 0)
        self.assertEqual(my_board.get_tile(X=0, Y=1), 0)
        self.assertEqual(my_board.get_tile(X=1, Y=0), 0)
        self.assertEqual(my_board.get_tile(X=1, Y=1), 0)

    def test_set_tile(self):
        """ test set tile """
        self.board.set_tile(val=-1, X=0, Y=1)
        self.assertEqual(self.board.get_tile(X=0, Y=1), -1)

    def test_invalid_tile(self):
        """get tile test"""
        error = self.board.get_tile(X=10, Y=10)
        self.assertEqual(error, -1)
        error = self.board.get_tile(X=-1, Y=0)
        self.assertEqual(error, -1)
        error = self.board.get_tile(X=0, Y=-1)
        self.assertEqual(error, -1)



if __name__ == "__main__":
    unittest.main()
