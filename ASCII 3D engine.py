import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp
from scipy import ndimage


# np.set_printoptions(threshold=sys.maxsize, linewidth=sys.maxsize)

def log(*x):
    print(*x, file=sys.stderr)

a = "150 550 0"
b = 7
c = ["#######","#..#..#","#..#.##","#.....#","#...###","#.....#","#######"]

WALL = "#"

width, height = 100,100
tiles = np.zeros((width,height),dtype=int)
notiles = np.zeros((width,height),dtype=int)

tiles[:,0] = 1
tiles[:,width-1] = 1
tiles[0,:] = 2
tiles[height-1,:] = 2

grid = []
x, y, a = [int(i) for i in a.split()]
n = int(b)
maps = []
for i in range(n):
    row = c[i]
    # log(row)
    maps.append(row)
log(maps)
lines = tiles
for row in maps:
    for symbol in row:
        if symbol == WALL:
            log(symbol, "WALL")
            lines += tiles
        else:
            log(symbol, "EMPTY")
            lines += notiles
    log(len(lines))
    #plt.imshow(lines)
    #plt.show()
    grid.append(lines)

log(len(grid))
grid = np.array(grid)
log(grid.shape)    



"""for g in grid:
    log(g)"""