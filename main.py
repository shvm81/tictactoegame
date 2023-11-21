print("Hello World")

#Variable
#Variable is a container that stores data
number = 9
print(number)

#multiplying the variable
print(number * 999)

#Lesson 2
#Arrays

array = [
    [1, 2],  #0                              #This entire array is a board
    [3, 4],  #1
    [5, 6]
]  #2, this row is called an index

print(array[0][1])
print(array[2][0])

#Lesson 3 and 4- Loops and Arrays refresher and functions
#tic-tac-toe type board
board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
turn = "X"
numberOfmoves = 0


def printBoard():
  print("Tic-Tac-Toe-Board")
  print("   0     1    2")
  count = 0
  while count <= 2:
    print(count, board[count])
    count += 1


def makeMove():
  xPos = 3  #we set this to be intentionally invalid so that we can see the error in the game
  yPos = 3

  while (xPos < 0 or xPos > 2 or yPos < 0 or yPos > 2
         or board[yPos][xPos] != '_'):
    xPos = int(input("Enter the x coordinates of your piece"))
    yPos = int(input("Enter the y coordinates of your piece"))

  board[yPos][xPos] = turn


def checkWinner():
  rowNumber = 0
  columnNumber = 0
  #Check for a horizontal winner

  while rowNumber < 3:
    if (board[rowNumber][0] == board[rowNumber][1] == board[rowNumber][2] ==
        turn):
      print("Winner detected horizontally")
      return True
    rowNumber += 1

  #Check for a vertical winner
  while columnNumber < 3:
    if (board[0][columnNumber] == board[1][columnNumber] ==
        board[2][columnNumber] == turn):
      print("Winner detected vertically")
      return True
    columnNumber += 1

  #Check for a diagonal winner
  return board[0][0] == board[1][1] == board[2][2] == turn or board[0][
      2] == board[1][1] == board[2][0] == turn
      


printBoard()

won = False
while not won:
  print("It is " + turn + "'s turn")
  makeMove()
  printBoard()
  numberOfmoves += 1

  if checkWinner():
    print(turn + " has won the game!")
    won = True
  elif numberOfmoves == 9:
    print("The players have tied!")
  else:
    if turn == "X":
      turn = "O"
    else:
      turn = "X"
