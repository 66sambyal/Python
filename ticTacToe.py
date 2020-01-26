theBoard = {'top-L' : ' ','top-M' : ' ','top-R' : ' ', 'mid-L' : ' ', 'mid-M' : ' ', 'mid-R' : ' ', 'low-L' : ' ', 'low-M' : ' ','low-R' : ' '}
def printBoard(stuff):
	print(' '+stuff['top-L']+' ' + '|' + ' '+stuff['top-M']+' ' + '|' + ' '+stuff['top-R']+' ')
	print('---+---+---')
	print(' '+stuff['mid-L'] +' '+ '|' + ' '+stuff['mid-M']+' ' + '|' + ' '+stuff['mid-R']+' ')
	print('---+---+---')
	print(' '+stuff['low-L'] +' '+ '|' + ' '+stuff['low-M']+' ' + '|' + ' '+stuff['low-R']+' ')
turn = 'X'
while 1==1:
	if (theBoard['top-L'] == 'X' and theBoard['top-M'] == 'X' and theBoard['top-R'] == 'X') or (theBoard['mid-L'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['mid-R'] == 'X') or (theBoard['low-L'] == 'X' and theBoard['low-M'] == 'X' and theBoard['low-R'] == 'X')or (theBoard['top-L'] == 'X' and theBoard['mid-L'] == 'X' and theBoard['low-L'] == 'X') or (theBoard['top-M'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['low-M'] == 'X') or (theBoard['top-R'] == 'X' and theBoard['mid-R'] == 'X' and theBoard['low-R'] == 'X')or (theBoard['top-L'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['low-R'] == 'X') or (theBoard['top-R'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['low-L'] == 'X'):
			print('########## Awesome X has WON the Game ##########')
			break
	if (theBoard['top-L'] == 'O' and theBoard['top-M'] == 'O' and theBoard['top-R'] == 'O') or (theBoard['mid-L'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['mid-R'] == 'O') or (theBoard['low-L'] == 'O' and theBoard['low-M'] == 'O' and theBoard['low-R'] == 'O')or (theBoard['top-L'] == 'O' and theBoard['mid-L'] == 'O' and theBoard['low-L'] == 'O') or (theBoard['top-M'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['low-M'] == 'O') or (theBoard['top-R'] == 'O' and theBoard['mid-R'] == 'O' and theBoard['low-R'] == 'O')or (theBoard['top-L'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['low-R'] == 'O') or (theBoard['top-R'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['low-L'] == 'O'):
			print('########## Awesome O has WON the Game ##########')
			break
	if theBoard['top-L'] == ' ' or theBoard['top-M'] == ' ' or theBoard['top-R'] == ' ' or theBoard['mid-L'] == ' ' or theBoard['mid-M'] == ' ' or theBoard['mid-R'] == ' ' or theBoard['low-L'] == ' ' or theBoard['low-M'] ==- ' ' or theBoard['low-R'] == ' ':
		printBoard(theBoard)
		print('Turn for ' + turn + '. Move on which space?')
		move = input()
		if 1==1:
			if (theBoard[move] == 'X') or (theBoard[move] == 'O'):
				print('Soory this place is already occupied!!')
			else:
				theBoard[move]
				theBoard[move] = turn
				if turn == 'X':
					turn = 'O'
				else:	
					turn = 'X'
printBoard(theBoard)
