from IPython.display import clear_output

def display_board(board):
	clear_output()
	print(board[1]+' | '+board[2]+' | '+board[3])
	print(board[4]+' | '+board[5]+' | '+board[6])
	print(board[9]+' | '+board[8]+' | '+board[9])

test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O','X', 'O', 'X']

def play_input():
	marker = ''
	while marker != 'X' and marker != 'O':
		marker = input("Player 1, choose X or O: ").upper()
	if marker == 'X':
		return ('X', 'O')
	else:
		return ('O', 'X')



if __name__ == '__main__':
	display_board(test_board)
	player1_marker, player2_marker = play_input()
	print(f"Player1: {player1_marker:-^20}")
	print(f"Player2: {player2_marker:*^20}")

