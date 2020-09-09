#Tic Tac Toe
import numpy
def win(Board):
	# Player 1 Horizontal
	if Board[0][0] == ' X ' and Board[0][1] == ' X ' and Board[0][2] == ' X ':
		print('Player 1 wins')
		quiting(Board)
	elif Board[1][0] == ' X ' and Board[1][1] == ' X ' and Board[1][2] == ' X ':
		print('Player 1 wins')
		quiting(Board)	
	elif Board[2][0] == ' X ' and Board[2][1] == ' X ' and Board[2][2] == ' X ':
		print('Player 1 wins')
		quiting(Board)
	#Player 1 vertical
	elif Board[0][0] == ' X ' and Board[1][0] == ' X ' and Board[2][0] == ' X ':
		print('Player 1 wins')
		quiting(Board)
	elif Board[0][1] == ' X ' and Board[1][1] == ' X ' and Board[2][1] == ' X ':
		print('Player 1 wins')
		quiting(Board)
	elif Board[0][2] == ' X ' and Board[1][2] == ' X ' and Board[2][2] == ' X ':
		print('Player 1 wins')
		quiting(Board)
	#Player 1 Diagonal
	elif Board[0][0] == ' X ' and Board[1][1] == ' X ' and Board[2][2] == ' X ':
		print('Player 1 wins')
		quiting(Board)
	elif Board[0][2] == ' X ' and Board[1][1] == ' X ' and Board[2][0] == ' X ':
		print('Player 1 wins')
		quiting(Board)

	#Player 2 Horizontal
	elif Board[0][0] == ' O ' and Board[0][1] == ' O ' and Board[0][2] == ' O ':
		print('Player 2 wins')
		quiting(Board)
	elif Board[1][0] == ' O ' and Board[1][1] == ' O ' and Board[1][2] == ' O ':
		print('Player 2 wins')
		quiting(Board)
	elif Board[2][0] == ' O ' and Board[2][1] == ' O ' and Board[2][2] == ' O ':
		print('Player 2 wins')
		quiting(Board)
	#Player 2 Vertical
	elif Board[0][0] == ' O ' and Board[1][0] == ' O ' and Board[2][0] == ' O ':
		print('Player 2 wins')
		quiting(Board)
	elif Board[0][1] == ' O ' and Board[1][1] == ' O ' and Board[2][1] == ' O ':
		print('Player 2 wins')
		quiting(Board)
	elif Board[0][2] == ' O ' and Board[1][2] == ' O ' and Board[2][2] == ' O ':
		print('Player 2 wins')
		quiting(Board)
	#Player 2 Diagonal
	elif Board[0][0] == ' O ' and Board[1][1] == ' O ' and Board[2][2] == ' O ':
		print('Player 2 wins')
		quiting(Board)
	elif Board[0][2] == ' O ' and Board[1][1] == ' O ' and Board[2][0] == ' O ':
		print('Player 2 wins')
		quiting(Board)
	else:
		pass


def takinginput(Board):
	i = 1
	while i<=9:
		if i%2 != 0:
			print('Player 1 turn:')
			z = ' X '
		else:
			print('Player 2 turn:')
			z = ' O '

		row1 = int(input('enter row: '))
		column1 = int(input('enter column: '))
		c = 0
		if row1>3  or column1>3 or row1<1 or column1<1:
			print('Wrong Input- Enter Again')
			i = i - 1
			c = c + 1
		if c == 0:
			if Board[row1-1][column1-1] != ' - ':
				print('Wrong Input- Enter Again')
				i = i - 1
			else:
				Board[row1-1][column1-1] = z
		print(Board)
		if i > 4:
			win(Board)
		i = i + 1

	print('Match Draws')
	quiting(Board)

def quiting(Board):
	print('Play Again - Y/N ?')
	t = input()
	if t == 'Y':
		takinginput(Board)
	else:
		quit()


Board = numpy.array([[' - ',' - ',' - ',],[' - ',' - ',' - '],[' - ',' - ',' - ']])
print("Tic-Tac-Toe : \n",Board)
print('Player 1 - X','Player 1 - O')
takinginput(Board)	
