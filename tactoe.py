#tic tac toe against the computer

board = [' ' for x in range(10)]


def insertLetter(letter, pos):
	board[pos] = letter

def spaceIsFree(pos):
	return board[pos] == ' '

def printBoard(board):
	print('   |   |')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('   |   |')

def isWinner(board, letter):
	return ((board[7] == letter and board[8] == letter and board[9] == letter) or
	(board[1] == letter and board[2] == letter and board[3] == letter) or 
	(board[4] == letter and board[5] == letter and board[6] == letter) or
	(board[1] == letter and board[4] == letter and board[7] == letter) or
	(board[2] == letter and board[5] == letter and board [8] == letter) or
	(board[3] == letter and board[6] == letter and board[9] == letter) or
	(board[1] == letter and board[5] == letter and board[9] == letter) or
	(board[3] == letter and board[5] == letter and board[7] == letter))


def playerMove():
	run = True
	while run:
		move = input('Please choose a position to place an \'X\':')
		try:
			move = int(move)
			if move > 0 and move < 10:
				if spaceIsFree(move):
					run = False
					insertLetter('X', move)
				else:
					print("Sorry, this space is occupied")
			else:
				print("Please type a number within range 1-9")
		except:
			print("Please type a valid number.")


def compMove():
	possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
	move = 0

	for let in ['O', 'X']:
		for i in possibleMoves:
			boardCopy = board[:]
			boardCopy[i] = let
			if isWinner(boardCopy, let):
				move = i
				return move

	cornerOpen = []
	for i in possibleMoves:
		if i in [1,3,7,9]:
			cornerOpen.append(i)
	if len(cornerOpen) > 0:
		move = selectRandom(cornerOpen)
		return move

	if 5 in possibleMoves:
		move = 5
		return move

	edgeOpen = []
	for i in possibleMoves:
		if i in [2,4,6,8]:
			edgeOpen.append(i)
	if len(edgeOpen) > 0:
		move = selectRandom(edgeOpen)
		return move

	
def selectRandom(list):
	import random

	length = len(list)
	rand = random.randrange(0, length)
	return list[rand]


def isBoardFull(board):
	if board.count(' ') > 1:
		return False
	else:
		return True

def main():
	print("Welcome to Tic Tac Toe by Monty :)\n")
	print("The layout is as follows: \n")
	print("1|2|3")
	print("-----")
	print("4|5|6")
	print("-----")
	print("7|8|9\n")
	print("Use numbers 1-9 to make your move, enjoy\n")
	printBoard(board)

	while not (isBoardFull(board)):
		if not(isWinner(board, 'O')):
			playerMove()
			printBoard(board)
		else:
			print("Sorry, O\'s won")
			break

		if not(isWinner(board, 'X')):
			move = compMove()
			if isBoardFull(board):
				print("Game is a tie")
			else:
				insertLetter('O', move)
				print("Computer placed an \'O\' in position", move)
				printBoard(board)
		else:
			print("Congrats, you beat the computer!")
			break


main()
