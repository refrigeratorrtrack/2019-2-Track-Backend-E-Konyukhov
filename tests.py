import unittest
import tictactoe

class TestGameMethods(unittest.TestCase):
	""" Tests. """
	def test_win(self):
		self.game = tictactoe.TicTacToe()
		self.game.playingField = ["X", "X", "X", 4, 5, 6, 7, 8, 9]
		self.game.check_win()
		self.assertTrue(self.game.win[0])


if __name__ == '__main__':
	unittest.main()
