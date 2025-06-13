import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from game.tic_tac_toe import TicTacToe

class TestTicTacToeMoves(unittest.TestCase):
    def test_make_move_valid(self):
        game = TicTacToe()
        success = game.make_move(0, 1)
        self.assertTrue(success)
        self.assertEqual(game.board[0], 1)
        self.assertEqual(game.current_player, -1)

    def test_make_move_invalid(self):
        game = TicTacToe()
        game.board[1] = -1
        success = game.make_move(1, 1)
        self.assertFalse(success)
        self.assertEqual(game.board[1], -1)

if __name__ == '__main__':
    unittest.main()
