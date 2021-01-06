from nnf import Var,true
from lib204 import Encoding

def menu(title, choices):#
  while True:
    print('\n' + title + '\n')
    for choice_num in range(len(choices)):
        print(str(choice_num + 1) + '. ' + choices[choice_num])
    print('\nX. Exit')
    print()
    choice = input("Your choice: ")
    try:
      choice = int(choice)
      if (choice > 0 and choice <= len(choices)):
        return choice
    except ValueError:
      pass
    if choice in ['x','X']:
      return None
    print('\nInvalid choice. Try again.')

def model (rows):
  print("RUNNING MODEL")
  print(rows)
  #check for horizontal wins, then vertical, then diagonal
  #DFS
  wins = 0
  nearWins = 0
  needTwo = 0
  needThree = 0
  needFour = 0
  for i in range(5):
    for j in range(9):
      #horizontal search
      tilesConcurrent = 0
      for index in range(5):
        # print("HOR")
        # print(i)
        # print(j)
        # print(index) #i = 3, j = 2, index = 0
        # print(tilesConcurrent)
        if (i+index >= 9):
          continue;
        elif (rows[i+index][j] == "B"):
          tilesConcurrent += 1
        else:
          break
      if (tilesConcurrent == 5):
        wins += 1
      elif (tilesConcurrent == 4) and (i+index >= 9) and (rows[i-1][j] != "B"):
        nearWins += 1
      # elif (tilesConcurrent == 3) and (i+index >= 9) and (rows[i-1][j] != "B"):
      #   needTwo += 1
      # elif (tilesConcurrent == 2) and (i+index >= 9) and (rows[i-1][j] != "B"):
      #   needThree += 1
      # elif (tilesConcurrent == 1) and (i+index >= 9) and (rows[i-1][j] != "B"):
      #   needFour += 1
      elif (tilesConcurrent == 4) and (j+index >= 9):
        continue
      elif (tilesConcurrent == 4) and (rows[i+index][j] != "B") and (rows[i-1][j] != "B"):
        nearWins += 1
      # elif (tilesConcurrent == 3) and (rows[i+index][j] != "B") and (rows[i-1][j] != "B"):
      #   needTwo += 1
      # elif (tilesConcurrent == 2) and (rows[i+index][j] != "B") and (rows[i-1][j] != "B"):
      #   needThree += 1
      # elif (tilesConcurrent == 1) and (rows[i+index][j] != "B") and (rows[i-1][j] != "B"):
      #   needFour += 1

  for i in range(9):
    for j in range(9):
      #vertical search
      tilesConcurrent = 0
      for index in range(5):
        # print("VER")
        # print(i)
        # print(j)
        # print(index) #i = 3, j = 2, index = 0
        # print(tilesConcurrent)
        if (j+index >= 9):
          continue;
        elif (rows[i][j+index] == "B"):
          tilesConcurrent += 1
        else:
          break
      if (tilesConcurrent == 5):
        wins += 1
      elif (tilesConcurrent == 4) and (j+index >= 9) and (rows[i][j-1] != "B"):
        nearWins += 1
      # elif (tilesConcurrent == 3) and (i+index >= 9) and (rows[i-1][j] != "B"):
      #   needTwo += 1
      # elif (tilesConcurrent == 2) and (i+index >= 9) and (rows[i-1][j] != "B"):
      #   needThree += 1
      # elif (tilesConcurrent == 1) and (i+index >= 9) and (rows[i-1][j] != "B"):
      #   needFour += 1
      elif (tilesConcurrent == 4) and (j+index >= 9):
        continue
      elif (tilesConcurrent == 4) and (rows[i][j+index] != "B") and (rows[i][j-1] != "B"):
        nearWins += 1
      # elif (tilesConcurrent == 3) and (rows[i][j+index] != "B") and (rows[i][j-1] != "B"):
      #   needTwo += 1
      # elif (tilesConcurrent == 2) and (rows[i][j+index] != "B") and (rows[i][j-1] != "B"):
      #   needThree += 1
      # elif (tilesConcurrent == 1) and (rows[i][j+index] != "B") and (rows[i][j-1] != "B"):
      #   needFour += 1

  for i in range(9):
    for j in range(9):
      tilesConcurrent = 0
      for index in range(5):
        if (i+index >= 9) or (j+index >= 9):
          continue;
        elif (rows[i+index][j+index] == "B"):
          tilesConcurrent += 1
        else:
          break
      if (tilesConcurrent == 5):
        wins += 1
      elif (tilesConcurrent == 4) and (i+index >= 9 or j+index >= 9) and (rows[i-1][j-1] != "B"):
        nearWins += 1
      #elif (tilesConcurrent == 3) and (i+index >= 9 or j+index >= 9) and (rows[i-1][j-1] != "B"):
      #   needTwo += 1
      # elif (tilesConcurrent == 2) and (i+index >= 9 or j+index >= 9) and (rows[i-1][j-1] != "B"):
      #   needThree += 1
      # elif (tilesConcurrent == 1) and (i+index >= 9 or j+index >= 9) and (rows[i-1][j-1] != "B"):
      #   needFour += 1
      elif (tilesConcurrent == 4) and (i+index >= 9 or j+index >= 9):
        continue
      elif (tilesConcurrent == 4) and (rows[i+index][j+index] != "B") and (rows[i-1][j-1] != "B"):
        nearWins += 1
      # elif (tilesConcurrent == 3) and (rows[i+index][j+index] != "B") and (rows[i-1][j-1] != "B"):
      #   needTwo += 1
      # elif (tilesConcurrent == 2) and (rows[i+index][j+index] != "B") and (rows[i-1][j-1] != "B"):
      #   needThree += 1
      # elif (tilesConcurrent == 1) and (rows[i+index][j+index] != "B") and (rows[i-1][j-1] != "B"):
      #   needFour += 1

  print("")
  print(wins)
  print(nearWins)
  print(needTwo)
  print(needThree)
  print(needFour)


def main ():
  columns = ["N","N","N","N","N","N","N","N","N"] #inner list, from top to bottom ordered
  rows = [] #outer list, from left to right ordered
  column = ["1","2","3","4","5","6","7","8","9"]
  row = ["A","B","C","D","E","F","G","H","I"]

  for i in range(9):
    rows.append(list(columns[:]))

  while True:
    choices = ['Set a tile white', 'Set a tile black', 'Set a tile blank', 'Run Model']
    choice = menu('Main Menu', choices)
    horizontalTile = ""
    verticalTile = ""

    if (str(choice).isdigit() != True):
      break
    elif (int(choice) == 1):
      print("Setting a white tile")
      horizontalTile = input("Please enter the horizontal position (A-I): ")
      verticalTile = input("Please enter the vertical position (1-9): ")
      verticalIndex = column.index(verticalTile)
      horizontalIndex = row.index(horizontalTile)
      rows[horizontalIndex][verticalIndex] = "W"
    elif (int(choice) == 2):
      print("Setting a black tile")
      #horizontalTile = input("Please enter the horizontal position (A-I): ")
      #verticalTile = input("Please enter the vertical position (1-9): ")
      # rows[4][8] = "B"
      # rows[5][8] = "B"
      # rows[6][8] = "B"
      # rows[7][8] = "B"
      # rows[8][8] = "B"

      # rows[0][5] = "B"
      # rows[0][6] = "B"
      # rows[0][7] = "B"
      # rows[0][8] = "B"

      # rows[8][4] = "B"
      # rows[8][5] = "B"
      # rows[8][6] = "B"
      # rows[8][7] = "B"
      # rows[8][8] = "B"

      # rows[6][5] = "B"
      # rows[6][6] = "B"
      # rows[6][7] = "B"
      # rows[6][8] = "B"

      rows[4][3] = "B"
      rows[4][4] = "B"
      rows[4][5] = "B"
      rows[4][6] = "B"

      #rows[1][4] = "B"
      rows[5][1] = "B"
      rows[6][2] = "B"
      rows[7][3] = "B"
      rows[8][4] = "B"
      #[4][4] is already black

      #verticalIndex = column.index(verticalTile)
      #horizontalIndex = row.index(horizontalTile)
      #rows[horizontalIndex][verticalIndex] = "B"
    elif (int(choice) == 3):
      print("Resetting a tile")
      horizontalTile = input("Please enter the horizontal position (A-I): ")
      verticalTile = input("Please enter the vertical position (1-9): ")
      verticalIndex = column.index(verticalTile)
      horizontalIndex = row.index(horizontalTile)
      rows[horizontalIndex][verticalIndex] = "N"
    elif (int(choice) == 4):
      print("Running model")
      model(rows)

#variable representing black's turn to play
bt = Var('bt')

#variable representing white's turn to play
wt = Var('wt')

#no tile on any square
#make 2D array for board tiles ; 'N' means no tile, 'B' means black tile, 'W' means white tile.

#use lists of lists to make 2D array
#

#fill inner list of 9 as N
#fill outer list of 9 as N




bTile = {}
for i in range(9):
  for j in range(9):
    bTile[(i,j)] = Var("(%d,%d)" % (i,j))


print(bTile)

nA1 = Var('nA1')
nB1 = Var('nB1')
nC1 = Var('nC1')
nD1 = Var('nD1')
nE1 = Var('nE1')
nF1 = Var('nF1')
nG1 = Var('nG1')
nH1 = Var('nH1')
nJ1 = Var('nJ1')
nA2 = Var('nA2')
nB2 = Var('nB2')
nC2 = Var('nC2')
nD2 = Var('nD2')
nE2 = Var('nE2')
nF2 = Var('nF2')
nG2 = Var('nG2')
nH2 = Var('nH2')
nJ2 = Var('nJ2')
nA3 = Var('nA3')
nB3 = Var('nB3')
nC3 = Var('nC3')
nD3 = Var('nD3')
nE3 = Var('nE3')
nF3 = Var('nF3')
nG3 = Var('nG3')
nH3 = Var('nH3')
nJ3 = Var('nJ3')
nA4 = Var('nA4')
nB4 = Var('nB4')
nC4 = Var('nC4')
nD4 = Var('nD4')
nE4 = Var('nE4')
nF4 = Var('nF4')
nG4 = Var('nG4')
nH4 = Var('nH4')
nJ4 = Var('nJ4')
nA5 = Var('nA5')
nB5 = Var('nB5')
nC5 = Var('nC5')
nD5 = Var('nD5')
nE5 = Var('nE5')
nF5 = Var('nF5')
nG5 = Var('nG5')
nH5 = Var('nH5')
nJ5 = Var('nJ5')
nA6 = Var('nA6')
nB6 = Var('nB6')
nC6 = Var('nC6')
nD6 = Var('nD6')
nE6 = Var('nE6')
nF6 = Var('nF6')
nG6 = Var('nG6')
nH6 = Var('nH6')
nJ6 = Var('nJ6')
nA7 = Var('nA7')
nB7 = Var('nB7')
nC7 = Var('nC7')
nD7 = Var('nD7')
nE7 = Var('nE7')
nF7 = Var('nF7')
nG7 = Var('nG7')
nH7 = Var('nH7')
nJ7 = Var('nJ7')
nA8 = Var('nA8')
nB8 = Var('nB8')
nC8 = Var('nC8')
nD8 = Var('nD8')
nE8 = Var('nE8')
nF8 = Var('nF8')
nG8 = Var('nG8')
nH8 = Var('nH8')
nJ8 = Var('nJ8')
nA9 = Var('nA9')
nB9 = Var('nB9')
nC9 = Var('nC9')
nD9 = Var('nD9')
nE9 = Var('nE9')
nF9 = Var('nF9')
nG9 = Var('nG9')
nH9 = Var('nH9')
nJ9 = Var('nJ9')

#white tile on any possible square
wA1 = Var('wA1')
wB1 = Var('wB1')
wC1 = Var('wC1')
wD1 = Var('wD1')
wE1 = Var('wE1')
wF1 = Var('wF1')
wG1 = Var('wG1')
wH1 = Var('wH1')
wJ1 = Var('wJ1')
wA2 = Var('wA2')
wB2 = Var('wB2')
wC2 = Var('wC2')
wD2 = Var('wD2')
wE2 = Var('wE2')
wF2 = Var('wF2')
wG2 = Var('wG2')
wH2 = Var('wH2')
wJ2 = Var('wJ2')
wA3 = Var('wA3')
wB3 = Var('wB3')
wC3 = Var('wC3')
wD3 = Var('wD3')
wE3 = Var('wE3')
wF3 = Var('wF3')
wG3 = Var('wG3')
wH3 = Var('wH3')
wJ3 = Var('wJ3')
wA4 = Var('wA4')
wB4 = Var('wB4')
wC4 = Var('wC4')
wD4 = Var('wD4')
wE4 = Var('wE4')
wF4 = Var('wF4')
wG4 = Var('wG4')
wH4 = Var('wH4')
wJ4 = Var('wJ4')
wA5 = Var('wA5')
wB5 = Var('wB5')
wC5 = Var('wC5')
wD5 = Var('wD5')
wE5 = Var('wE5')
wF5 = Var('wF5')
wG5 = Var('wG5')
wH5 = Var('wH5')
wJ5 = Var('wJ5')
wA6 = Var('wA6')
wB6 = Var('wB6')
wC6 = Var('wC6')
wD6 = Var('wD6')
wE6 = Var('wE6')
wF6 = Var('wF6')
wG6 = Var('wG6')
wH6 = Var('wH6')
wJ6 = Var('wJ6')
wA7 = Var('wA7')
wB7 = Var('wB7')
wC7 = Var('wC7')
wD7 = Var('wD7')
wE7 = Var('wE7')
wF7 = Var('wF7')
wG7 = Var('wG7')
wH7 = Var('wH7')
wJ7 = Var('wJ7')
wA8 = Var('wA8')
wB8 = Var('wB8')
wC8 = Var('wC8')
wD8 = Var('wD8')
wE8 = Var('wE8')
wF8 = Var('wF8')
wG8 = Var('wG8')
wH8 = Var('wH8')
wJ8 = Var('wJ8')
wA9 = Var('wA9')
wB9 = Var('wB9')
wC9 = Var('wC9')
wD9 = Var('wD9')
wE9 = Var('wE9')
wF9 = Var('wF9')
wG9 = Var('wG9')
wH9 = Var('wH9')
wJ9 = Var('wJ9')

#black tile on any possible square
bA1 = Var('bA1')
bB1 = Var('bB1')
bC1 = Var('bC1')
bD1 = Var('bD1')
bE1 = Var('bE1')
bF1 = Var('bF1')
bG1 = Var('bG1')
bH1 = Var('bH1')
bJ1 = Var('bJ1')
bA2 = Var('bA2')
bB2 = Var('bB2')
bC2 = Var('bC2')
bD2 = Var('bD2')
bE2 = Var('bE2')
bF2 = Var('bF2')
bG2 = Var('bG2')
bH2 = Var('bH2')
bJ2 = Var('bJ2')
bA3 = Var('bA3')
bB3 = Var('bB3')
bC3 = Var('bC3')
bD3 = Var('bD3')
bE3 = Var('bE3')
bF3 = Var('bF3')
bG3 = Var('bG3')
bH3 = Var('bH3')
bJ3 = Var('bJ3')
bA4 = Var('bA4')
bB4 = Var('bB4')
bC4 = Var('bC4')
bD4 = Var('bD4')
bE4 = Var('bE4')
bF4 = Var('bF4')
bG4 = Var('bG4')
bH4 = Var('bH4')
bJ4 = Var('bJ4')
bA5 = Var('bA5')
bB5 = Var('bB5')
bC5 = Var('bC5')
bD5 = Var('bD5')
bE5 = Var('bE5')
bF5 = Var('bF5')
bG5 = Var('bG5')
bH5 = Var('bH5')
bJ5 = Var('bJ5')
bA6 = Var('bA6')
bB6 = Var('bB6')
bC6 = Var('bC6')
bD6 = Var('bD6')
bE6 = Var('bE6')
bF6 = Var('bF6')
bG6 = Var('bG6')
bH6 = Var('bH6')
bJ6 = Var('bJ6')
bA7 = Var('bA7')
bB7 = Var('bB7')
bC7 = Var('bC7')
bD7 = Var('bD7')
bE7 = Var('bE7')
bF7 = Var('bF7')
bG7 = Var('bG7')
bH7 = Var('bH7')
bJ7 = Var('bJ7')
bA8 = Var('bA8')
bB8 = Var('bB8')
bC8 = Var('bC8')
bD8 = Var('bD8')
bE8 = Var('bE8')
bF8 = Var('bF8')
bG8 = Var('bG8')
bH8 = Var('bH8')
bJ8 = Var('bJ8')
bA9 = Var('bA9')
bB9 = Var('bB9')
bC9 = Var('bC9')
bD9 = Var('bD9')
bE9 = Var('bE9')
bF9 = Var('bF9')
bG9 = Var('bG9')
bH9 = Var('bH9')
bJ9 = Var('bJ9')



#every possible winning row
r1 = ((bA1 & bB1 & bC1 & bD1 & bE1) | (bB1 & bC1 & bD1 & bE1 & bF1) | (bC1 & bD1 & bE1 & bF1 & bG1) | (bD1 & bE1 & bF1 & bG1 & bH1) | (bE1 & bF1 & bG1 & bH1 & bJ1))
r2 = ((bA2 & bB2 & bC2 & bD2 & bE2) | (bB2 & bC2 & bD2 & bE2 & bF2) | (bC2 & bD2 & bE2 & bF2 & bG2) | (bD2 & bE2 & bF2 & bG2 & bH2) | (bE2 & bF2 & bG2 & bH2 & bJ2))
r3 = ((bA3 & bB3 & bC3 & bD3 & bE3) | (bB3 & bC3 & bD3 & bE3 & bF3) | (bC3 & bD3 & bE3 & bF3 & bG3) | (bD3 & bE3 & bF3 & bG3 & bH3) | (bE3 & bF3 & bG3 & bH3 & bJ3))
r4 = ((bA4 & bB4 & bC4 & bD4 & bE4) | (bB4 & bC4 & bD4 & bE4 & bF4) | (bC4 & bD4 & bE4 & bF4 & bG4) | (bD4 & bE4 & bF4 & bG4 & bH4) | (bE4 & bF4 & bG4 & bH4 & bJ4))
r5 = ((bA5 & bB5 & bC5 & bD5 & bE5) | (bB5 & bC5 & bD5 & bE5 & bF5) | (bC5 & bD5 & bE5 & bF5 & bG5) | (bD5 & bE5 & bF5 & bG5 & bH5) | (bE5 & bF5 & bG5 & bH5 & bJ5))
r6 = ((bA6 & bB6 & bC6 & bD6 & bE6) | (bB6 & bC6 & bD6 & bE6 & bF6) | (bC6 & bD6 & bE6 & bF6 & bG6) | (bD6 & bE6 & bF6 & bG6 & bH6) | (bE6 & bF6 & bG6 & bH6 & bJ6))
r7 = ((bA7 & bB7 & bC7 & bD7 & bE7) | (bB7 & bC7 & bD7 & bE7 & bF7) | (bC7 & bD7 & bE7 & bF7 & bG7) | (bD7 & bE7 & bF7 & bG7 & bH7) | (bE7 & bF7 & bG7 & bH7 & bJ7))
r8 = ((bA8 & bB8 & bC8 & bD8 & bE8) | (bB8 & bC8 & bD8 & bE8 & bF8) | (bC8 & bD8 & bE8 & bF8 & bG8) | (bD8 & bE8 & bF8 & bG8 & bH8) | (bE8 & bF8 & bG8 & bH8 & bJ8))
r9 = ((bA9 & bB9 & bC9 & bD9 & bE9) | (bB9 & bC9 & bD9 & bE9 & bF9) | (bC9 & bD9 & bE9 & bF9 & bG9) | (bD9 & bE9 & bF9 & bG9 & bH9) | (bE9 & bF9 & bG9 & bH9 & bJ9))

#a single possible winning row 

ri = (r1 | r2 | r3 | r4 | r5 | r6 | r7 | r8 | r9)

#every possible winning column
cA = ((bA1 & bA2 & bA3 & bA4 & bA5) | (bA2 & bA3 & bA4 & bA5 & bA6) | (bA3 & bA4 & bA5 & bA6 & bA7 ) | (bA4 & bA5 & bA6 & bA7 & bA8) | (bA5 & bA6 & bA7 & bA8 & bA9))
cB = ((bB1 & bB2 & bB3 & bB4 & bB5) | (bB2 & bB3 & bB4 & bB5 & bB6) | (bB3 & bB4 & bB5 & bB6 & bB7 ) | (bB4 & bB5 & bB6 & bB7 & bB8) | (bB5 & bB6 & bB7 & bB8 & bB9))
cC = ((bC1 & bC2 & bC3 & bC4 & bC5) | (bC2 & bC3 & bC4 & bC5 & bC6) | (bC3 & bC4 & bC5 & bC6 & bC7 ) | (bC4 & bC5 & bC6 & bC7 & bC8) | (bC5 & bC6 & bC7 & bC8 & bC9))
cD = ((bD1 & bD2 & bD3 & bD4 & bD5) | (bD2 & bD3 & bD4 & bD5 & bD6) | (bD3 & bD4 & bD5 & bD6 & bD7 ) | (bD4 & bD5 & bD6 & bD7 & bD8) | (bD5 & bD6 & bD7 & bD8 & bD9))
cE = ((bE1 & bE2 & bE3 & bE4 & bE5) | (bE2 & bE3 & bE4 & bE5 & bE6) | (bE3 & bE4 & bE5 & bE6 & bE7 ) | (bE4 & bE5 & bE6 & bE7 & bE8) | (bE5 & bE6 & bE7 & bE8 & bE9))
cF = ((bF1 & bF2 & bF3 & bF4 & bF5) | (bF2 & bF3 & bF4 & bF5 & bF6) | (bF3 & bF4 & bF5 & bF6 & bF7 ) | (bF4 & bF5 & bF6 & bF7 & bF8) | (bF5 & bF6 & bF7 & bF8 & bF9))
cG = ((bG1 & bG2 & bG3 & bG4 & bG5) | (bG2 & bG3 & bG4 & bG5 & bG6) | (bG3 & bG4 & bG5 & bG6 & bG7 ) | (bG4 & bG5 & bG6 & bG7 & bG8) | (bG5 & bG6 & bG7 & bG8 & bG9))
cH = ((bH1 & bH2 & bH3 & bH4 & bH5) | (bH2 & bH3 & bH4 & bH5 & bH6) | (bH3 & bH4 & bH5 & bH6 & bH7 ) | (bH4 & bH5 & bH6 & bH7 & bH8) | (bH5 & bH6 & bH7 & bH8 & bH9))
cJ = ((bJ1 & bJ2 & bJ3 & bJ4 & bJ5) | (bJ2 & bJ3 & bJ4 & bJ5 & bJ6) | (bJ3 & bJ4 & bJ5 & bJ6 &bJ7 ) | (bJ4 & bJ5 & bJ6 & bJ7 & bJ8) | (bJ5 & bJ6 & bJ7 & bJ8 & bJ9))

#a single possible winning column
ci = (cA | cB | cC | cD | cE | cF | cG | cH | cJ)

#set up diagonals down here somehow
'''
a = Var('a')
b = Var('b')
c = Var('c')
x = Var('x')
y = Var('y')
z = Var('z')
'''

def iff(left, right):
    return (left.negate() | right) & (right.negate() | left)

#
# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.

def model_gomoku():
  goE = Encoding()
  
  goE.add_constraint(ri | ci)

  #cannot have two winning lines at the same time
  goE.add_constraint((r1.negate() | r2.negate()) & (r1.negate() | r3.negate()) & (r1.negate() | r4.negate()) & (r1.negate() | r5.negate()) & (r1.negate() | r6.negate()) & (r1.negate() | r7.negate()) & (r1.negate() | r8.negate()) & (r1.negate() | r9.negate()) & (r2.negate() | r3.negate()) & (r2.negate() | r4.negate()) & (r2.negate() | r5.negate()) & (r2.negate() | r6.negate()) & (r2.negate() | r7.negate()) & (r2.negate() | r8.negate()) & (r2.negate() | r9.negate()) & (r3.negate() | r4.negate()) & (r3.negate() | r5.negate()) & (r3.negate() | r6.negate()) & (r3.negate() | r7.negate()) & (r3.negate() | r8.negate()) & (r3.negate() | r9.negate()) & (r4.negate() | r5.negate()) & (r4.negate() | r6.negate()) & (r4.negate() | r7.negate()) & (r4.negate() | r8.negate()) & (r4.negate() | r9.negate()) & (r5.negate() | r6.negate()) & (r5.negate() | r7.negate()) & (r5.negate() | r8.negate()) & (r5.negate() | r9.negate()) & (r6.negate() | r7.negate()) & (r6.negate() | r8.negate()) & (r6.negate() | r9.negate()) & (r7.negate() | r8.negate()) & (r7.negate() | r9.negate()) & (r8.negate() | r9.negate()))

  #cannot have both a white and a black tile on the same square
  for i in range(9):
    for j in range(9):
      goE.add_constraint(rows[i][j] == "B" & rows[i][j] = "W").negate()
  goE.add_constraint((bA1 & wA1).negate() & (bA2 & wA2).negate() & (bA3 & wA3).negate() & (bA4 & wA4).negate() & (bA5 & wA5).negate() &(bA6 & wA6).negate() & (bA7 & wA7).negate() &(bA8 & wA8).negate() &(bA9 & wA9).negate() & (bB1 & wB1).negate() & (bB2 & wB2).negate() & (bB3 & wB3).negate() & (bB4 & wB4).negate() & (bB5 & wB5).negate() & (bB6 & wB6).negate() & (bB7 & wB7).negate() & (bB8 & wB8).negate() & (bB9 & wB9).negate() & (bC1 & wC1).negate() & (bC2 & wC2).negate() & (bC3 & wC3).negate() & (bC4 & wC4).negate() & (bC5 & wC5).negate() & (bC6 & wC6).negate() & (bC7 & wC7).negate() & (bC8 & wC8).negate() & (bC9 & wC9).negate() & (bD1 & wD1).negate() & (bD2 & wD2).negate() & (bD3 & wD3).negate() & (bD4 & wD4).negate() & (bD5 & wD5).negate() & (bD6 & wD6).negate() & (bD7 & wD7).negate() & (bD8 & wD8).negate() & (bD9 & wD9).negate() & (bE1 & wE1).negate() & (bE2 & wE2).negate() & (bE3 & wE3).negate() & (bE4 & wE4).negate() & (bE5 & wE5).negate() & (bE6 & wE6).negate() & (bE7 & wE7).negate() & (bE8 & wE8).negate() & (bE9 & wE9).negate() & (bF1 & wF1).negate() & (bE2 & wF2).negate() & (bF3 & wF3).negate() & (bF4 & wF4).negate() & (bF5 & wF5).negate() & (bF6 & wF6).negate() & (bF7 & wF7).negate() & (bF8 & wF8).negate() & (bF9 & wF9).negate() & (bG1 & wG1).negate() & (bG2 & wG2).negate() & (bG3 & wG3).negate() & (bG4 & wG4).negate() & (bG5 & wG5).negate() & (bG6 & wG6).negate() & (bG7 & wG7).negate() & (bG8 & wG8).negate() & (bG9 & wG9).negate() &(bH1 & wH1).negate() & (bH2 & wH2).negate() & (bH3 & wH3).negate() & (bH4 & wH4).negate() & (bH5 & wH5).negate() & (bH6 & wH6).negate() & (bH7 & wH7).negate() & (bH8 & wH8).negate() & (bH9 & wH9).negate() & (bJ1 & wJ1).negate() & (bJ2 & wJ2).negate() & (bJ3 & wJ3).negate() & (bJ4 & wJ4).negate() & (bJ5 & wJ5).negate() & (bJ6 & wJ6).negate() & (bJ7 & wJ7).negate() & (bJ8 & wJ8).negate() & (bJ9 & wJ9).negate())

  #it cannot be both white and black's turn to play
  goE.add_constraint((wt & bt).negate())

  #checking to see which column has a winning configuration
  goE.add_constraint(iff(ri, (cA | cB | cC | cD | cE | cF | cG | cH | cJ)))

  #checking to see which row has a winning configuration
  goE.add_constraint(iff(ci, (r1 | r2 | r3 | r4 | r5 | r6 | r7 | r8 | r9)))

  return goE

'''
def example_theory():
    E = Encoding()
    E.add_constraint(a | b)
    E.add_constraint(~a | ~x)
    E.add_constraint(c | y | z)
    return E
'''

if __name__ == "__main__":
    main()
    #T = example_theory()
    G = model_gomoku()
    #print(G.size())
    #print("\nSatisfiable: %s" % G.is_satisfiable())
    #print("\nSatisfiable: %s" % G.is_satisfiable())
    #print("# Solutions: %d" % G.count_solutions())
    #print("   Solution: %s" % G.solve())

    """
    print("\nVariable likelihoods:")
    for v,vn in zip([a,b,c,x,y,z], 'abcxyz'):
        print(" %s: %.2f" % (vn, T.likelihood(v)))
    print()
    """
