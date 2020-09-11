#Grid
grid = [[" ", " ", " ", " ", " ", " ",
         " "], [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ",
         " "], [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "]]

def displayGrid():
	print("\n" * 250)
	count = 0
	for x in range(6):
		print(grid[count])
		print()
		count = count + 1


#ValidityChecker
def validCheck(dataType):
	dataType = str(dataType)
	valid = False
	while True:
		while valid == False:
			if dataType == "number":
				try:
					check = ""
					check = int(input("Pick a Column (1-7)\n"))
					print()
					valid = True
				except:
					print("Input is not a valid", dataType)
			elif dataType == "colour":
				try:
					check = ""
					check = str(input("Pick a Colour (R or Y)\n"))
					print()
					valid = True
				except:
					print("Please enter a colour (R or Y)\n")
			if dataType == "colour":
				try:
					if check == "R" or check == "Y":
						break
					else:
						print("Input is not a valid", dataType)
						valid = False
						continue
				except:
					print("Input is not a valid", dataType)
			elif dataType == "number":
				try:
					if check >= 1 and check <= 7:
						break
					else:
						print("Input is not a valid", dataType)
						valid = False
						continue
				except:
					continue
		break
	return (check)


#Menu
def menu():
	print("The Lad's Connect 4 - Press the enter key to play")
	input()
	dataType = "colour"
	currentPlayer = validCheck(dataType)
	return (currentPlayer)


def move():
	dataType = "number"
	print("It's", currentPlayer, "'s Turn!'")
	column = validCheck(dataType)
	return (column)


def makeMove(column, currentPlayer):
	moveDone = False
	while moveDone == False:
		count = 5
		for x in range(6):
			if grid[0][column] == "R" or grid[0][column] == "Y":
				displayGrid()
				print("That column is full!")
				column = move()
				column = column - 1
			elif grid[count][column] == " ":
				grid[count][column] = currentPlayer
				break
			else:
				count = count - 1
		moveDone = True
	displayGrid()


def checkWinner():
	boardWidth = 6
	boardHeight = 7
	tile = currentPlayer
	# check horizontal spaces
	for y in range(boardHeight):
		for x in range(boardWidth - 3):
			if grid[x][y] == tile and grid[x + 1][y] == tile and grid[
			    x + 2][y] == tile and grid[x + 3][y] == tile:
				return True

	# check vertical spaces
	for x in range(boardWidth):
		for y in range(boardHeight - 3):
			if grid[x][y] == tile and grid[x][y + 1] == tile and grid[x][
			    y + 2] == tile and grid[x][y + 3] == tile:
				return True

	# check / diagonal spaces
	for x in range(boardWidth - 3):
		for y in range(3, boardHeight):
			if grid[x][y] == tile and grid[x + 1][y - 1] == tile and grid[
			    x + 2][y - 2] == tile and grid[x + 3][y - 3] == tile:
				return True

	# check \ diagonal spaces
	for x in range(boardWidth - 3):
		for y in range(boardHeight - 3):
			if grid[x][y] == tile and grid[x + 1][y + 1] == tile and grid[
			    x + 2][y + 2] == tile and grid[x + 3][y + 3] == tile:
				return True
	return False


#Start of Program
winCondition = False
currentPlayer = menu()
while winCondition == False:
	column = move()
	column = column - 1
	makeMove(column, currentPlayer)
	winCondition = checkWinner()
	if currentPlayer == "R":
		currentPlayer = "Y"
	elif currentPlayer == "Y":
		currentPlayer = "R"
if currentPlayer == "R":
	currentPlayer = "Y"
elif currentPlayer == "Y":
	currentPlayer = "R"
print(currentPlayer, " Wins!")

print("END OF PROGRAM")

#James Worley and Tom Comrie 09/09/2020
