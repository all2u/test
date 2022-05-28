import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp
from scipy import ndimage


np.set_printoptions(threshold=sys.maxsize, linewidth=sys.maxsize)

def log(*x):
    print(*x, file=sys.stderr)

c = "420 78"
d = "W 4742 B 6 W 167 B 6 W 240 B 8 W 165 B 8 W 238 B 10 W 163 B 10 W 237 B 10 W 163 B 10 W 220 B 4 W 13 B 10 W 146 B 4 W 13 B 10 W 218 B 8 W 11 B 10 W 144 B 8 W 11 B 10 W 218 B 8 W 11 B 10 W 144 B 8 W 11 B 10 W 217 B 10 W 10 B 9 W 144 B 10 W 10 B 9 W 128 B 400 W 92 B 6 W 12 B 10 W 10 B 1 W 134 B 6 W 12 B 10 W 10 B 1 W 207 B 1 W 6 B 1 W 11 B 10 W 10 B 1 W 133 B 1 W 6 B 1 W 11 B 10 W 10 B 1 W 206 B 2 W 6 B 2 W 10 B 9 W 11 B 1 W 132 B 2 W 6 B 2 W 10 B 9 W 11 B 1 W 206 B 1 W 8 B 1 W 10 B 9 W 11 B 1 W 81 B 1 W 50 B 1 W 8 B 1 W 10 B 9 W 11 B 1 W 61 B 1 W 127 B 4 W 13 B 1 W 8 B 1 W 10 B 1 W 2 B 4 W 13 B 1 W 44 B 4 W 33 B 1 W 33 B 4 W 13 B 1 W 8 B 1 W 10 B 1 W 2 B 4 W 13 B 1 W 44 B 4 W 13 B 1 W 125 B 2 W 4 B 2 W 11 B 1 W 8 B 1 W 10 B 1 W 19 B 1 W 42 B 2 W 4 B 2 W 31 B 1 W 31 B 2 W 4 B 2 W 11 B 1 W 8 B 1 W 10 B 1 W 19 B 1 W 42 B 2 W 4 B 2 W 11 B 1 W 125 B 1 W 6 B 1 W 11 B 2 W 6 B 2 W 10 B 1 W 19 B 1 W 42 B 1 W 6 B 1 W 31 B 1 W 31 B 1 W 6 B 1 W 11 B 2 W 6 B 2 W 10 B 1 W 19 B 1 W 42 B 1 W 6 B 1 W 11 B 1 W 124 B 1 W 8 B 1 W 10 B 2 W 6 B 1 W 11 B 1 W 19 B 1 W 41 B 1 W 8 B 1 W 30 B 1 W 30 B 1 W 8 B 1 W 10 B 2 W 6 B 1 W 11 B 1 W 19 B 1 W 41 B 1 W 8 B 1 W 10 B 1 W 74 B 51 W 8 B 94 W 8 B 63 W 8 B 94 W 8 B 66 W 52 B 6 W 12 B 1 W 8 B 1 W 10 B 1 W 19 B 1 W 19 B 1 W 41 B 1 W 8 B 1 W 30 B 1 W 12 B 6 W 12 B 1 W 8 B 1 W 10 B 1 W 19 B 1 W 19 B 1 W 41 B 1 W 8 B 1 W 10 B 1 W 105 B 1 W 6 B 1 W 11 B 1 W 8 B 1 W 10 B 1 W 19 B 1 W 61 B 1 W 8 B 1 W 30 B 1 W 11 B 1 W 6 B 1 W 11 B 1 W 8 B 1 W 10 B 1 W 19 B 1 W 61 B 1 W 8 B 1 W 10 B 1 W 104 B 2 W 6 B 2 W 10 B 2 W 6 B 1 W 11 B 1 W 19 B 1 W 61 B 2 W 6 B 1 W 31 B 1 W 10 B 2 W 6 B 2 W 10 B 2 W 6 B 1 W 11 B 1 W 19 B 1 W 61 B 2 W 6 B 1 W 11 B 1 W 104 B 1 W 8 B 1 W 10 B 3 W 4 B 2 W 11 B 1 W 19 B 1 W 48 B 1 W 12 B 3 W 4 B 2 W 31 B 1 W 10 B 1 W 8 B 1 W 10 B 3 W 4 B 2 W 11 B 1 W 19 B 1 W 48 B 1 W 12 B 3 W 4 B 2 W 11 B 1 W 87 B 4 W 13 B 1 W 8 B 1 W 10 B 1 W 2 B 4 W 13 B 1 W 19 B 1 W 48 B 1 W 4 B 4 W 4 B 1 W 2 B 4 W 7 B 4 W 16 B 4 W 2 B 1 W 10 B 1 W 8 B 1 W 10 B 1 W 2 B 4 W 13 B 1 W 19 B 1 W 48 B 1 W 4 B 4 W 4 B 1 W 2 B 4 W 7 B 4 W 2 B 1 W 85 B 8 W 11 B 1 W 8 B 1 W 10 B 1 W 19 B 1 W 19 B 1 W 48 B 1 W 2 B 8 W 2 B 1 W 11 B 8 W 12 B 9 W 10 B 1 W 8 B 1 W 10 B 1 W 19 B 1 W 19 B 1 W 48 B 1 W 2 B 8 W 2 B 1 W 11 B 9 W 85 B 8 W 11 B 2 W 6 B 2 W 10 B 1 W 19 B 1 W 68 B 1 W 2 B 8 W 2 B 1 W 11 B 8 W 12 B 9 W 10 B 2 W 6 B 2 W 10 B 1 W 19 B 1 W 68 B 1 W 2 B 8 W 2 B 1 W 11 B 9 W 84 B 10 W 10 B 2 W 6 B 1 W 11 B 1 W 19 B 1 W 68 B 1 W 1 B 10 W 1 B 1 W 10 B 10 W 10 B 10 W 10 B 2 W 6 B 1 W 11 B 1 W 19 B 1 W 68 B 1 W 1 B 10 W 1 B 1 W 10 B 10 W 74 B 400 W 30 B 10 W 10 B 1 W 19 B 1 W 19 B 1 W 68 B 1 W 1 B 10 W 1 B 1 W 10 B 10 W 10 B 10 W 10 B 1 W 19 B 1 W 19 B 1 W 68 B 1 W 1 B 10 W 1 B 1 W 10 B 10 W 84 B 10 W 10 B 1 W 19 B 1 W 88 B 1 W 1 B 10 W 1 B 1 W 10 B 10 W 10 B 10 W 10 B 1 W 19 B 1 W 88 B 1 W 1 B 10 W 1 B 1 W 10 B 10 W 84 B 9 W 11 B 1 W 19 B 1 W 88 B 1 W 1 B 9 W 2 B 1 W 10 B 9 W 12 B 8 W 11 B 1 W 19 B 1 W 88 B 1 W 1 B 9 W 2 B 1 W 11 B 8 W 85 B 9 W 11 B 1 W 19 B 1 W 88 B 1 W 1 B 9 W 2 B 1 W 10 B 9 W 12 B 8 W 11 B 1 W 19 B 1 W 88 B 1 W 1 B 9 W 2 B 1 W 11 B 8 W 85 B 1 W 2 B 4 W 13 B 1 W 19 B 1 W 82 B 4 W 2 B 1 W 1 B 1 W 2 B 4 W 4 B 1 W 10 B 1 W 2 B 4 W 16 B 4 W 13 B 1 W 19 B 1 W 82 B 4 W 2 B 1 W 1 B 1 W 2 B 4 W 4 B 1 W 13 B 4 W 87 B 1 W 19 B 1 W 19 B 1 W 80 B 9 W 1 B 1 W 10 B 1 W 10 B 1 W 39 B 1 W 19 B 1 W 80 B 9 W 1 B 1 W 10 B 1 W 104 B 1 W 19 B 1 W 100 B 9 W 1 B 1 W 21 B 1 W 39 B 1 W 100 B 9 W 1 B 1 W 115 B 1 W 19 B 1 W 99 B 10 W 1 B 1 W 21 B 1 W 39 B 1 W 99 B 10 W 1 B 1 W 105 B 400 W 30 B 1 W 19 B 1 W 99 B 10 W 1 B 1 W 21 B 1 W 39 B 1 W 99 B 10 W 1 B 1 W 115 B 1 W 119 B 10 W 1 B 1 W 21 B 1 W 139 B 10 W 1 B 1 W 115 B 1 W 120 B 8 W 2 B 1 W 21 B 1 W 140 B 8 W 2 B 1 W 115 B 1 W 120 B 8 W 2 B 1 W 21 B 1 W 140 B 8 W 2 B 1 W 115 B 1 W 122 B 4 W 4 B 1 W 21 B 1 W 142 B 4 W 4 B 1 W 115 B 1 W 130 B 1 W 21 B 1 W 150 B 1 W 945 B 400 W 9250"


w, h = [int(i) for i in c.split()]
s = w*h
image = d.split()
grid = []
txt=""
for x in range(0,len(image),2):
  color, pixels = "1" if image[x]=="B" else "0",int(image[x+1])
  txt+=color*pixels

r = 0
line = ""
while r != s:
    if r % w != 0:
        line += txt[r]
    else:
        if line != "":
            # log(line, (r//w)-1)
            grid.append([int(x) for x in line])
            line = ""
    r += 1

minX, minY = w, h
maxX = 0
lineH = 0
noteH = 0

for y in range(len(grid)):
    for x in range(len(grid[y])):
        # log(grid[y][x])
        if grid[y][x] == 1 and x < minX:
            maxX = grid[y].count(1)
            minX = x
            minY = y

lines = []
for y in range(len(grid)):
    if grid[y][minX] == 1:
        lines.append(y)
        lineH += 1
lineH = lineH//5

for y in range(minY+lineH, len(grid)):
    if grid[y][minX] == 0:
        noteH += 1
    if grid[y][minX] == 1:
        break

zones = []
som = noteH+lineH
lnt = som // 2
minY = minY-lnt
zones.append((minY-lnt, minY+lnt))
zones.append((minY+lnt, minY+som))
zones.append((minY+som, minY+som+lnt))
zones.append((minY+som+lnt, minY+som*2))
zones.append((minY+som*2, minY+som*2+lnt))
zones.append((minY+som*2+lnt, minY+som*3))
zones.append((minY+som*3, minY+som*3+lnt))
zones.append((minY+som*3+lnt, minY+som*4))
zones.append((minY+som*4, minY+som*4+lnt))
zones.append((minY+som*4+lnt, minY+som*5))
zones.append((minY+som*5, minY+som*5+lnt))
zones.append((minY+som*5+lnt, minY+som*6))

notes = ['G','F','E','D','C','B','A','G','F','E','D','C']

grid = np.array(grid)
detect = []
Pitches = []
part = []
ok = False

do = np.zeros((h-1,), dtype=int)
doidx = minY+(noteH*5)+(lineH*5)+lnt
do[doidx:doidx+lineH]=1
lines.extend([int(i) for i in range(doidx,doidx+lineH+1)])

staff=grid[:,minX]
staff2 = staff + do

grid = grid[:,minX:w]
l,lgNote = 0, 0
largNotes = []

for m in grid.T:
    c1=(m==staff).all()
    c2=(m==staff2).all()
    #log(c1,c2)
    compare=c2 if c2 else c1
    ok = False if compare.all() else True
    if ok:
      l+=1
      detect.append(m)
    else:
        largNotes.append(l)
        lgNote = sum(largNotes)
        l = 0

largNotes= np.array(largNotes)
largNotes=largNotes[largNotes>0]
detect=np.array(detect)

l=0
n = (noteH)//2 if 
result = ""
for j in largNotes:
  for i in range(l,j+l,j):
    maskh=detect[i-n+j//2:i+n+j//2].T
    plt.imshow(maskh)
    plt.show()
    p = 0
    r = []
    for m in range(len(maskh)):
        if m not in lines and maskh[m].sum(0) != 0:
            p+=1
            r.append((maskh[m],m))
    x = r[(p//2+1)]
    t=x[0]
    s=x[1]
    for zone in zones:
        if s > zone[0] and s <= zone[1]:
            result += notes[zones.index(zone)]
    if t[len(t)//2] == 0:
        result += "H "
    else:
        result += "Q "
  l+=j
  
print(result.strip())
