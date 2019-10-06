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


	def displayPlayingField(self):
		""" Display playing field. """
		print("{} | {} | {}".format(self.playingField[0], self.playingField[1], self.playingField[2]))
		print("--+---+--")
		print("{} | {} | {}".format(self.playingField[3], self.playingField[4], self.playingField[5]))
		print("--+---+--")
		print("{} | {} | {}".format(self.playingField[6], self.playingField[7], self.playingField[8]))


	def inputUserMove(self):
		""" User input processing. """
		while True:
			self.move = input()

			if self.move in self.checkingString:
				if self.playingField[int(self.move) - 1] not in self.variants:
					self.move = int(self.move) - 1
					self.setMove()
					break
				else:
					print("This cell is not free! Try again.")
			else:
				print("Incorrect cell! Try again!")


	def setMove(self):
		""" Set user move. """
		if self.order == 1:
			self.playingField[self.move] = "X"
		elif self.order == 2:
			self.playingField[self.move] = "0"


	def checkWin(self):
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


	def checkDraw(self):
		""" Check draw situation. """
		self.counter = 0

		for cell in self.playingField:
			if cell == "X" or cell == "0":
				self.counter += 1

		if self.counter == 9:
			self.draw = True


	def printCongratulation(self):
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


	def printHello(self):
		""" Print hello-message to user(s). """
		print("Hello! You are in tic tac toe. Press 'Enter' to start game!")


	def printInvitationToMove(self):
		""" Print invitation for users. """
		if self.order == 1:
			print("Move for first player.")
		elif self.order == 2:
			print("Move for second player.")

		print("Choose free cell.")


	def play(self):
		""" The main part. Start game process. """
		self.printHello()
		self.displayPlayingField()

		while self.win[0] != True and self.draw != True:
			self.printInvitationToMove()
			self.inputUserMove()
			self.setMove()
			self.displayPlayingField()

			if self.order == 1:
				self.order = 2
			elif self.order == 2:
				self.order = 1

			self.checkDraw()
			self.checkWin()

		self.printCongratulation()


if __name__ == '__main__':
	game = TicTacToe()
	game.play()
	# game.playingField = ["X", "X", "X", 4, 5, 6, 7, 8, 9]
	# game.checkWin()
	# print(game.win[0])
