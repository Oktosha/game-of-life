import random
import time

def printState(state, *, live="*", dead="."):
  for row in state:
    for item in row:
      print(live if item else dead, end="")
    print()
  print()

def getCell(i, j, state):
  N = len(state)
  M = len(state[0])
  if i < 0 or j < 0 or i >= N or j >= M:
    return False
  return state[i][j]

def countLiveNeighbours(i, j, state):
  ans = 0
  for di in [-1, 0, 1]:
    for dj in [-1, 0, 1]:
      if not (di == 0 and dj == 0):
        ans += 1 if getCell(i + di, j + dj, state) else 0
  return ans

def nextCellState(i, j, state):
  if getCell(i, j, state):
    return (countLiveNeighbours(i, j, state) == 2
        or countLiveNeighbours(i, j, state) == 3)
  return  countLiveNeighbours(i, j, state) == 3

def nextState(state):
  N = len(state)
  M = len(state[0])
  return [[nextCellState(i, j, state) for j in range(M)] for i in range(N)]

N = 5
M = 80
state = [[random.choice([True, False]) for j in range(M)] for i in range(N)]

while True:
  printState(state)
  state = nextState(state)
  time.sleep(1)