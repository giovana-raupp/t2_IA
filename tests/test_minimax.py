import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from minimax.minimax import MinimaxPlayer

class TestMinimaxAlgorithm(unittest.TestCase):
    def test_choose_winning_move(self):
        board_state = [
            1, -1, 1,
            1, -1, 0,
            -1, 0, 0
        ]
        player = MinimaxPlayer(difficulty='hard', symbol='O')
        move = player.get_move(board_state)
        self.assertEqual(move, 7)

    def test_evaluate_board_results(self):
        player = MinimaxPlayer(symbol='X')

        x_win = [
            1, 1, 1,
            0, 0, 0,
            0, 0, 0,
        ]
        self.assertEqual(player.evaluate_board(x_win), 1)

        o_win = [
            -1, -1, -1,
            0, 0, 0,
            0, 0, 0,
        ]
        self.assertEqual(player.evaluate_board(o_win), -1)

        draw = [
            1, -1, 1,
            1, -1, -1,
            -1, 1, 1,
        ]
        self.assertEqual(player.evaluate_board(draw), 0)

if __name__ == '__main__':
    unittest.main()
