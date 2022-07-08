import sys
import matplotlib.pyplot as plt
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

#wh = "5 4"
#m = ["5 5 5 5 5","5 4 4 4 5","5 3 2 1 5","5 5 5 5 5"]
#wh = "7 5"
#m = ["1 1 1 1 1 1 1","1 2 2 2 2 2 1","1 2 3 9 3 2 1","1 2 2 2 2 2 1","1 1 1 1 1 1 1"]
wh = "5 3"
m = ["1 1 9 1 1", "1 1 9 1 1", "1 1 9 1 1"]

wh = "9 9"
m = ["1 2 3 4 5 6 7 8 9", "999 999 999 999 999 999 999 999 10", "31 32 33 34 35 36 37 999 11", "30 999 999 999 999 999 38 999 12", "29 999 47 48 49 999 39 999 13",
     "28 999 46 999 999 999 40 999 14", "27 999 45 44 43 42 41 999 15", "26 999 999 999 999 999 999 999 16", "25 24 23 22 21 20 19 18 17"]

w, h = [int(i) for i in wh.split()]

maps = np.zeros((h, w), dtype=int)
for i in range(h):
    mp = [int(x) for x in m[i].split()]
    for j in range(w):
        maps[i][j] = mp[j]

mx = np.()(maps)
print(mx)

fig, ax = plt.subplots()
ax.imshow(maps)


def format_coord(x, y):
    col = int(x + 0.5)
    row = int(y + 0.5)
    if 0 <= col < w and 0 <= row < h:
        z = maps[row, col]
        return 'x=%1.4f, y=%1.4f, z=%1.4f' % (x, y, z)
    else:
        return 'x=%1.4f, y=%1.4f' % (x, y)


print(maps)
ax.format_coord = format_coord
# plt.show()
