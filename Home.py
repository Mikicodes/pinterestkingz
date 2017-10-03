def homepage():
	for user in USER_LIST:
		for board in user.boards:
			return board.pins