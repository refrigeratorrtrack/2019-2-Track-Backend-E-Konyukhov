import unittest
import tictactoe

class TestGameMethods(unittest.TestCase):
	""" Tests. """
	def test_check_win(self):
		self.game = tictactoe.TicTacToe()
		self.game.playingField = ["X", "X", "X", 4, 5, 6, 7, 8, 9]
		self.game.check_win()
		self.assertTrue(self.game.win[0])
		self.game = tictactoe.TicTacToe()
		self.game.playingField = ["X", "0", "X", 4, 5, 6, 7, 8, 9]
		self.game.check_win()
		self.assertFalse(self.game.win[0])

	def test_print_invitation_to_move(self):
		self.game = tictactoe.TicTacToe()
		self.game.order = 3
		self.assertFalse(self.game.print_invitation_to_move())

	def test_set_move(self):
		self.game = tictactoe.TicTacToe()
		self.game.order = 3
		self.assertFalse(self.game.set_move())

	def test_check_draw(self):
		self.game = tictactoe.TicTacToe()
		self.game.playingField = ["X", "0", "X", "0", "X", "X", "0", "X", "0"]
		self.game.check_draw()
		self.assertTrue(self.game.draw)
		self.game = tictactoe.TicTacToe()
		self.game.playingField = ["X", "X", "X", "0", "X", "X", "0", 8, "0"]
		self.game.check_draw()
		self.assertFalse(self.game.draw)


if __name__ == '__main__':
	unittest.main()
