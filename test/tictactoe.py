from nnf import Var, true, NNF
from lib204 import Encoding

def implication(l, r):
    return l.negate() | r

def neg(f):
    return f.negate()

NNF.__rshift__ = implication
NNF.__invert__ = neg

X = []
O = []
empty = []
winRow = []
winCol = []
for i in range(3):
  X.append([])
  O.append([])
  empty.append([])
  winRow.append(Var(f"win_at_row{i}"))
  winCol.append(Var(f"win_at_col{i}"))
  for j in range(3):
    X[i].append(Var(f"X_at_{i},{j}"))
    O[i].append(Var(f"O_at_{i},{j}"))
    empty[i].append(Var(f"empty_at_{i},{j}"))


def iff(left, right):
    return (left.negate() | right) & (right.negate() | left)


def parseBoard(solution):
  if solution == None:
    raise ValueError("no valid solutions")

  board = [
    [" " for i in range(3)] for i in range(3)
  ]
  for key, value in solution.items():
    if (key[:5] == "X_at_") & value:
      board[int(key[-1])][int(key[-3])] = "X"
    if (key[:5] == "O_at_") & value:
      board[int(key[-1])][int(key[-3])] = "O"
    if (key[:10] == "win_at_row") & value:
      print(f"{key}: {value}")
    if (key[:10] == "win_at_col") & value:
      print(f"{key}: {value}")
  
  for row in board:
    for slot in row:
      print(slot, end= " ")
    print()

def onePerSquare(E):
  for i in range(3):
    for j in range(3):
      E.add_constraint(X[i][j] >> (~empty[i][j] & ~O[i][j]))
      E.add_constraint(O[i][j] >> (~empty[i][j] & ~X[i][j]))
      E.add_constraint(empty[i][j] >> (~X[i][j] & ~O[i][j]))

      E.add_constraint(empty[i][j] | O[i][j] | X[i][j])

  return E

def checkWin(E):
  for i in range(3):
    # (b1 & b2 & b3 ......) >> rowWin[i]
    # (b2 & b3 & b4 ......) >> rowWin[i]
    row = true
    for j in range(3):
      row &= X[j][i]
    E.add_constraint(iff(row, winRow[i]))

    col = true
    for j in range(3):
      col &= X[i][j]
    E.add_constraint(iff(col, winCol[i]))
  return E




def Theory():
  E = Encoding()
  E = onePerSquare(E)
  E = checkWin(E)
  E.add_constraint(winRow[2])

  return E


if __name__ == "__main__":
  T = Theory()
  parseBoard(T.solve())