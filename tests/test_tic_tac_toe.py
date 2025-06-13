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

    def test_check_winner_rows_cols_diagonals(self):
        # Linha
        game = TicTacToe()
        game.board = [1, 1, 1, 0, 0, 0, 0, 0, 0]
        self.assertEqual(game.check_winner(), 1)

        # Coluna
        game = TicTacToe()
        game.board = [1, 0, 0, 1, 0, 0, 1, 0, 0]
        self.assertEqual(game.check_winner(), 1)

        # Diagonal
        game = TicTacToe()
        game.board = [1, 0, 0, 0, 1, 0, 0, 0, 1]
        self.assertEqual(game.check_winner(), 1)

    def test_check_winner_draw(self):
        game = TicTacToe()
        game.board = [
            1, -1, 1,
            1, -1, -1,
            -1, 1, 1
        ]
        self.assertEqual(game.check_winner(), 0)

    def test_is_game_over_states(self):
        # Vitória
        game = TicTacToe()
        game.board = [1, 1, 1, 0, 0, 0, 0, 0, 0]
        self.assertTrue(game.is_game_over())
        self.assertEqual(game.winner, 1)

        # Empate
        game = TicTacToe()
        game.board = [
            1, -1, 1,
            1, -1, -1,
            -1, 1, 1
        ]
        self.assertTrue(game.is_game_over())
        self.assertEqual(game.winner, 0)

        # Jogo continua
        game = TicTacToe()
        game.board = [
            1, 0, 0,
            0, -1, 0,
            0, 0, 0
        ]
        self.assertFalse(game.is_game_over())

if __name__ == '__main__':
    unittest.main()
