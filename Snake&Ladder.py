#Snake and Ladder
import numpy
import random

def Board(a):
	arr = []
	a = 91
	b = 101
	for j in range(1,11):
		lst = []
		for i in range(a,b):
			lst.append(i)
		a = a - 10
		b = b - 10
		arr.append(lst)

	d = {}

	#defining Snake and Ladder
	arr[7][4] = '25(S1S)'
	arr[9][5] = '6(S1E)'
	d['74'] = '95'

	arr[8][8] = '19(L1S)'
	arr[3][5] = '66(L1E)'
	d['88'] = '35'

	arr[5][5] = '46(S2S)'
	arr[8][1] = '12(S2E)'
	d['55'] = '81'

	arr[6][1] = '32(L2S)'
	arr[4][2] = '53(L2E)'
	d['61'] = '42'

	arr[2][3] = '74(S3S)'
	arr[4][1] = '52(S3E)'
	d['23'] = '41'

	arr[3][6] = '67(L3S)'
	arr[0][9] = '100(L3E)'
	d['36'] = '09'

	arr[2][2] = '73(L4S)'
	arr[0][0] = '91(L4E)'
	d['22'] = '00'

	arr[1][7] = '88(S4S)'
	arr[2][5] = '76(S4E)'
	d['17'] = '25'
	
	Board = numpy.array(arr)
	return Board,d


def quiting(i1,i2,Boards,z,name):
	a = Boards[i1][i2]
	b = a[:3]
	if b == '100':
		print('Player ',name,' Wins the Game')
		q = input('Play again? - Y/N: ')
		if q == 'y':
			Game(name1,name2)
		else:
			quit()


def SnakeLadder(i1,i2,Boards,dict1):
	a = Boards[i1][i2]
	try:
		b = int(a)
	except:
		if len(a) <= 3:
			pass
		elif a[3] == 'S' and a[5] == 'S':
			print('Snake bite the player')
			b = str(i1) + str(i2)
			val = dict1[b]
			i1 = int(val[0])
			i2 = int(val[1])
			pos = Boards[i1][i2]
			print('Player is at ',pos[:2],' position')
		elif a[3] == 'L' and a[5] == 'S':
			print('Player got a jump of ladder')
			b = str(i1) + str(i2)
			val = dict1[b]
			i1 = int(val[0])
			i2 = int(val[1])
			pos = Boards[i1][i2]
			print('Player is at ',pos[:2],' position')
		else:
			pass
	return i1,i2


def Game(name1,name2):
	Boards = Board(0)[0]
	dict1 = Board(0)[1]
	Boards[9][0] = Boards[9][0] + '⚫⚪'
	print(Boards)
	
	#player 1 initial index
	i11 = 9
	i21 = 0
	#player 2 initial index
	i12 = 9
	i22 = 0

	l = 1
	while True:
		if l%2 != 0:
			print('Player 1 Turn')
			i1 = i11
			i2 = i21
			name = name1
			z = '⚫'
		else:
			print('Player 2 Turn')
			i1 = i12
			i2 = i22
			name = name2
			z = '⚪'

		#Dice rolling
		w = input('press any key / press q to quit ')
		if w == 'q':
			quit()
		n1 = random.randrange(1,7,1)
		print(n1)
		str1 = Boards[i1][i2]
		
		#removing from previous position
		lst1 = list(str1)
		str1 = ''
		i = 0
		while i <= len(lst1):
			if lst1[i] == z:
				del lst1[i]
			else:
				str1 = str1 + lst1[i]
				i = i + 1
			if i == (len(lst1)):
				break
		Boards[i1][i2] = str1

		#incrementation
		if i2 + n1 <= 9 and i1 != 0:
			i2 = i2 + n1
		elif i2 + n1 > 9 and i1 != 0:
			i2 = ((i2 + n1)%9) - 1
			i1 = i1 - 1
			

		#checking snake or ladder
		if i1 != 0:
			m = SnakeLadder(i1,i2,Boards,dict1)
			i1 = m[0]
			i2 = m[1]
			Boards[i1][i2] = Boards[i1][i2] + z
		else:
			#handling last line case
			try:
				f = Boards[i1][i2+n1]
				if f[0] == '9' or f[:3] == '100':
					i2 = i2 + n1
					Boards[i1][i2] = Boards[i1][i2] + z
					quiting(i1,i2,Boards,z,name)
				else:
					i2 = i2 - n1
					Boards[i1][i2] = Boards[i1][i2] + z
			except:
				pass

		#storing index of Players
		if l%2 != 0:
			i11 = i1
			i21 = i2
		else:
			i12 = i1
			i22 = i2
		
		print(Boards)
		
		quiting(i1,i2,Boards,z,name)
		l =l + 1




print('SNAKE AND LADDER')
print('NOTE: S*S and S*E indicates Start and End of Snake')
print('NOTE: L*S and L*E indicates Start and End of Ladder')
name1 = input('PLAYER 1 NAME: ')
name2 = input('PLAYER 2 NAME: ')
print('PLAYER 1 - ⚫')
print('PLAYER 2 - ⚪')
Game(name1,name2)
#Board(0)
