# This is a sample Python script.

def draw_line(width, edge, filling):
	print(filling.join([edge] * (width + 1)))

def draw_board(width, height):
	draw_line(width, " ", "--")
	for i in range(height):
		draw_line(width, "|", "--")
	print("\n")

def display_winner(player):
	if player == 0:
		print("Tie")
	else:
		print("Player:" + str(player) + " wins!")

def check_row_winner(row):
	"""
	Return the player number that wins for that row.
	If there is no winner, return 0.
	"""
	if row[0] == row[1] and row[1] == row[2]:
		return row[0]
	return 0

def get_col(game, col_number):
	return [game[x][col_number] for x in range(3)]

def get_row(game, row_number):
	return game[row_number]

def check_winner(game):
	game_slices = []
	for index in range(3):
		game_slices.append(get_row(game, index))
		game_slices.append(get_col(game, index))

	# check diagonals
	down_diagonal = [game[x][x] for x in range(3)]
	up_diagonal = [game[0][2], game[1][1], game[2][0]]
	game_slices.append(down_diagonal)
	game_slices.append(up_diagonal)

	for game_slice in game_slices:
		winner = check_row_winner(game_slice)
		if winner != 0:
			display_winner(winner)
			return winner

	display_winner(winner)
	return winner

def start_game():
	return [[1, 0, 0] for x in range(3)]

def display_game(game):
	d = {2: "O", 1: "X", 0: " "}
	game_string = []
	for row_num in range(3):
		new_row = []
		for col_num in range(3):
			new_row.append(d[game[row_num][col_num]])
		game_string.append(new_row)
	print(game_string)


def add_piece(game, player, row, column):
	"""
	game: game state
	player: player number
	row: 0-index row
	column: 0-index column
	"""
	game[row][column] = player
	return game

def convert_input_to_coordinate(user_input):
	return user_input - 1

def switch_player(player):
	if player == 1:
		return 2
	else:
		return 1


if __name__ == '__main__':
	game = start_game()
	display_game(game)
	player = 1

	# go on forever
	while True:
		// Adding some comments
		print("Currently player::" + str(player))
		row = convert_input_to_coordinate(int(input("Which row? (start with 1) ")))
		column = convert_input_to_coordinate(int(input("Which column? (start with 1) ")))
		game = add_piece(game, player, row, column)
		display_game(game)
		player = switch_player(player)
