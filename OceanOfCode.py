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
                self.board[j][i] = ISLAND if self.grid[j][i] == "x" else EMPTY
        return self.board

    def get_Tile(self, x, y):
        return self.grid[x][y]

    def isOnMap(self, tile):
        if tile.x < 0 or tile.x >= self.width or tile.y < 0 or tile.y >= self.height:
            return False
        return True

    def isSafe(self, tile):
        return self.isOnMap(tile) and self.board[tile.y][tile.x] == EMPTY

    def isShootable(self, tile):
        return self.board[tile.y][tile.x] != ISLAND

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
        for x, y in ((tile.x-1, tile.y), (tile.x+1, tile.y), (tile.x, tile.y-1), (tile.x, tile.y+1)):
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

    def play(self):
        move = self.move()
        shoot = self.shoot()
        print(move+shoot)

    def move(self):
        north = Tile(self.pos.x, self.pos.y - 1)
        south = Tile(self.pos.x, self.pos.y + 1)
        east = Tile(self.pos.x + 1, self.pos.y)
        west = Tile(self.pos.x - 1, self.pos.y)

        if self.board.isSafe(north):
            return self.moveTo("N")
        elif self.board.isSafe(south):
            return self.moveTo("S")
        elif self.board.isSafe(east):
            return self.moveTo("E")
        elif self.board.isSafe(west):
            return self.moveTo("W")
        elif not self.silence():
            self.surface()
            
        
        # log(board.neighbours(self.myship))

    def silence(self):
        if self.silence_cooldown > 0:
            return False
        for i in range(2,5):
            north = Tile(self.pos.x, self.pos.y - i)
            south = Tile(self.pos.x, self.pos.y + i)
            east = Tile(self.pos.x + i, self.pos.y)
            west = Tile(self.pos.x - i, self.pos.y)
            if self.board.isSafe(north):
                return self.silenceTo("N", i)
            elif self.board.isSafe(south):
                return self.silenceTo("S", i)
            elif self.board.isSafe(east):
                return self.silenceTo("E", i)
            elif self.board.isSafe(west):
                return self.silenceTo("W", i)
        return False

    def shoot(self):
        if self.torpedo_cooldown == 0:
            north = Tile(self.pos.x, self.pos.y - 3)
            south = Tile(self.pos.x, self.pos.y + 3)
            east = Tile(self.pos.x + 3, self.pos.y)
            west = Tile(self.pos.x - 3, self.pos.y)

            if self.board.isOnMap(north) and self.board.isShootable(north):
                return self.shootAt(north)
            elif self.board.isOnMap(south) and self.board.isShootable(south):
                return self.shootAt(south)
            elif self.board.isOnMap(east) and self.board.isShootable(east):
                return self.shootAt(east)
            elif self.board.isOnMap(west) and self.board.isShootable(west):
                return self.shootAt(west)
        return ""

    def moveTo(self, direction):
        power = self.charge()
        return (f"MOVE {direction} {power}")

    def silenceTo(self, direction, distance):
        print(f"SILENCE {direction} {distance}")
        return True
    
    def charge(self):
        return "TORPEDO"
        if self.silence_cooldown > 0:
            return "SILENCE"
        else:
            return "TORPEDO"

    def shootAt(self, tile):
        return f"| TORPEDO {tile.x} {tile.y}"

    def surface(self):
        print("SURFACE")
        self.board.boardInit()

    def sonar(self, sector):
        print(f"SONAR {sector}")

class Enemy(Ship):
    def findEnemy(self, orders):
        self.pos = 0, 0
        sector = None
        splitOrders = orders.split()
        if splitOrders[0] == "SURFACE":
            sector = sectors[int(splitOrders[1])]
        if sector is not None:
            log(sector)
        else:
            pass




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
enemyShip = Enemy()

sectors = {
    1: [[0,5],[0,5]], 2: [[5,10],[0,5]], 3: [[10,15],[0,5]],
    4: [[0,5],[5,10]], 5: [[5,10],[5,10]], 6: [[10,15],[5,10]],
    7: [[0,5],[10,15]], 8: [[5,10],[10,15]], 9: [[10,15],[10,15]]
}

# game loop
while True:
    # inputs = input()
    x, y, my_life, opp_life, torpedo_cooldown, sonar_cooldown, silence_cooldown, mine_cooldown = [
        int(i) for i in input().split()]
    sonar_result = input()
    opponent_orders = input()
    log(sonar_result, opponent_orders)
    myShip.update(Tile(x, y), my_life, torpedo_cooldown,sonar_cooldown, silence_cooldown, mine_cooldown)
    myShip.play()
    enemyShip.findEnemy(opponent_orders)
