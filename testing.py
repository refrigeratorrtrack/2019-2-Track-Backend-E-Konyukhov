import unittest
import tictactoe

class TestGameMethods(unittest.TestCase):
	""" Fucking tests. """
	def __init__(self):
		self.game = tictactoe.TicTacToe()

	def isWin(self):
		self.game = tictactoe.TicTacToe()
		self.game.playingField = ["X", "X", "X", 4, 5, 6, 7, 8, 9]
		self.game.checkWin()
		self.assertTrue(game.win[0])


if __name__ == '__main__':
	unittest.main()
