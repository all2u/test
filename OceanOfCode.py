import sys
import math
import random

def log(*x):
    print(*x, file=sys.stderr)

EMPTY = 0
ISLAND = 1
ISVISITED = 2

class Tile:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"{self.x},{self.y}"

    def __str__(self):
        return str(f"{self.x},{self.y}")     


class Board:
    def __init__(self, width, height, grid):
        self.grid = grid
        self.width, self.height = width, height
        self.board = [[0 for i in range(width)] for j in range(height)]

    def boardInit(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.board[j][i] = ISLAND if self.grid[j][i]=="x" else EMPTY
        return self.board

    def get_Tile(self, x, y):
        return self.grid[x][y]

    def isSafe(self, tile):
        if tile.x<0 or tile.x>=self.width or tile.y<0 or tile.y>=self.height:
            return False
        return self.board[tile.y][tile.x] == EMPTY

    def startCoord(self):
        x = random.randint(0, 2)
        y = random.randint(0, 8)
        while self.board[y][x] != EMPTY:
            self.startCoord()
        return x, y

    def isVisited(self, tile):
        self.board[tile.y][tile.x] = ISVISITED

    def neighbours(self, tile):
        count = 0
        for x, y in ((tile.x-1, tile.y),(tile.x+1, tile.y),(tile.x, tile.y-1),(tile.x, tile.y+1)):
            if not (0 <= x < len(self.grid[0]) and 0 <= y < len(self.grid)):
                # out of bounds
                continue
            # log(x, y)
            if self.grid[x][y] == ".":
                count += 1
        return count

    def __str__(self):
        for i in self.grid:
            log("".join(i))


class Ship:
    def update(self, pos, life, torpedo_cooldown, sonar_cooldown, silence_cooldown, mine_cooldown, target=None):
        self.pos = pos
        self.life = life
        self.torpedo_cooldown = torpedo_cooldown
        self.sonar_cooldown = sonar_cooldown
        self.silence_cooldown = silence_cooldown
        self.mine_cooldown = mine_cooldown
        self.board.isVisited(self.pos)

    def setBoard(self, board):
        self.board = board

    def move(self, action="MOVE", power="TORPEDO"):
        north = Tile(self.pos.x, self.pos.y - 1)
        south = Tile(self.pos.x, self.pos.y + 1)
        east = Tile(self.pos.x + 1, self.pos.y)
        west = Tile(self.pos.x - 1, self.pos.y)

        if self.board.isSafe(north):
            print(f"{action} N {power}")
        elif self.board.isSafe(south):
            print(f"{action} S {power}")
        elif self.board.isSafe(east):
            print(f"{action} E {power}")
        elif self.board.isSafe(west):
            print(f"{action} W {power}")
        else:
            print("SURFACE")
            self.board.boardInit()
       # log(board.neighbours(self.myship))

    def silence(self, distance):
        self.move("SILENCE", distance)

    def sonar(self, sector):
        print(f"SONAR {sector}")


grid = []
width, height, my_id = [int(i) for i in input().split()]
for y in range(height):
    line = input()
    row = []
    for x in range(width):
        row.append(line[x])
    grid.append(row)
board = Board(width, height, grid)
board.boardInit()
# log(board.board)

startX, startY = board.startCoord()
# log(board.get_Tile(startX, startY))
print("{} {}".format(startX, startY))
myShip = Ship()
myShip.pos = Tile(startX, startY)
myShip.setBoard(board)

sector = 1

# game loop
while True:
    # inputs = input()
    x, y, my_life, opp_life, torpedo_cooldown, sonar_cooldown, silence_cooldown, mine_cooldown = [int(i) for i in input().split()]
    sonar_result = input()
    opponent_orders = input()
    log(sonar_result, opponent_orders)
    myShip.update(Tile(x, y), my_life, torpedo_cooldown, sonar_cooldown, silence_cooldown, mine_cooldown)
    # if myShip.torpedo_cooldown > 0:
    if myShip.torpedo_cooldown > 0:
        myShip.move()
    elif myShip.sonar_cooldown > 0:
        myShip.move("MOVE", "SONAR")
    elif myShip.silence_cooldown > 0:
        myShip.move("MOVE", "SILENCE")
    if myShip.sonar_cooldown == 0:
        myShip.sonar(sector)
        sector += 1
    log(myShip.sonar_cooldown)
    """for _ in range(6):
        print("MOVE N TORPEDO")
    print("TORPEDO 5 1")"""