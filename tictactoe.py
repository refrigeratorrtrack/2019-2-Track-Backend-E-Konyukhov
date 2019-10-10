class TicTacToe(object):
	def __init__(self):
		""" Initializing. """
		self.fieldSize = 3
		self.playingField = [i for i in range(1, self.fieldSize ** 2 + 1)]
		self.checkingString = [str(i) for i in range(1, self.fieldSize ** 2 + 1)]
		self.order = 1
		self.win = [False, 0]
		self.draw = False
		self.variants = ["X", "0"]


	def display_playing_field(self):
		""" Display playing field. """
		print("{} | {} | {}".format(self.playingField[0], self.playingField[1], self.playingField[2]))
		print("--+---+--")
		print("{} | {} | {}".format(self.playingField[3], self.playingField[4], self.playingField[5]))
		print("--+---+--")
		print("{} | {} | {}".format(self.playingField[6], self.playingField[7], self.playingField[8]))


	def input_user_move(self):
		""" User input processing. """
		while True:
			self.move = input()

			if self.move in self.checkingString:
				if self.playingField[int(self.move) - 1] not in self.variants:
					self.move = int(self.move) - 1
					self.set_move()
					break
				else:
					print("This cell is not free! Try again.")
			else:
				print("Incorrect cell! Try again!")


	def set_move(self):
		""" Set user move. """
		if self.order == 1:
			self.playingField[self.move] = "X"
		elif self.order == 2:
			self.playingField[self.move] = "0"
		else:
			return False


	def check_win(self):
		""" Checking win. """
		if self.playingField[0] == self.playingField[1] == self.playingField[2]:
			self.win[0] = True
			self.win[1] = self.variants.index(self.playingField[0]) + 1
		elif self.playingField[3] == self.playingField[4] == self.playingField[5]:
			self.win[0] = True
			self.win[1] = self.variants.index(self.playingField[3]) + 1
		elif self.playingField[6] == self.playingField[7] == self.playingField[8]:
			self.win[0] = True
			self.win[1] = self.variants.index(self.playingField[6]) + 1
		
		if self.playingField[0] == self.playingField[3] == self.playingField[6]:
			self.win[0] = True
			self.win[1] = self.variants.index(self.playingField[0]) + 1
		elif self.playingField[1] == self.playingField[4] == self.playingField[7]:
			self.win[0] = True
			self.win[1] = self.variants.index(self.playingField[1]) + 1
		elif self.playingField[2] == self.playingField[5] == self.playingField[8]:
			self.win[0] = True
			self.win[1] = self.variants.index(self.playingField[2]) + 1

		if self.playingField[0] == self.playingField[4] == self.playingField[8]:
			self.win[0] = True
			self.win[1] = self.variants.index(self.playingField[0]) + 1
		elif self.playingField[2] == self.playingField[4] == self.playingField[6]:
			self.win[0] = True
			self.win[1] = self.variants.index(self.playingField[2]) + 1


	def check_draw(self):
		""" Check draw situation. """
		self.counter = 0

		for cell in self.playingField:
			if cell == "X" or cell == "0":
				self.counter += 1

		if self.counter == 9:
			self.draw = True


	def print_congratulation(self):
		""" Print congratulation to winner. """
		print("Congratulations!")

		if self.draw == True:
			print("It is a draw! Both win!")

		if self.win[0] == True:
			if (self.win[1] == 1):
				print("First user wins!")
			elif (self.win[1] == 2):
				print("Second user wins!")
			elif self.win[1] == 3:
				print("Draw!")


	def print_hello(self):
		""" Print hello-message to user(s). """
		print("Hello! You are in tic tac toe. Press 'Enter' to start game!")


	def print_invitation_to_move(self):
		""" Print invitation for users. """
		if self.order == 1:
			print("Move for first player.")
		elif self.order == 2:
			print("Move for second player.")
		else:
			return False

		print("Choose free cell.")


	def play(self):
		""" The main part. Start game process. """
		self.print_hello()
		self.display_playing_field()

		while self.win[0] != True and self.draw != True:
			self.print_invitation_to_move()
			self.input_user_move()
			self.set_move()
			self.display_playing_field()

			if self.order == 1:
				self.order = 2
			elif self.order == 2:
				self.order = 1

			self.check_draw()
			self.check_win()

		self.print_congratulation()


if __name__ == '__main__':
	game = TicTacToe()
	game.play()
