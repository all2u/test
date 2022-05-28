x=[int(i)for i in input().split()]

e=[[int(j)for j in input().split()]for i in range(x[7])]
e.append((x[3],x[4]))
e = sorted(e)

while True:
    i=input().split()
    a=int(i[0])
    b = int(i[1])
    c = i[2]
    d="BLOCK","WAIT"
    f=d[1]
    if a == e[a][0]:
        if b == w-1 or b == 0:
            f=d[0]
        elif c == "RIGHT" and b > e[a][1]:
            f=d[0]
        elif c == "LEFT" and b < e[a][1]:
            f=d[0]
        else:
            f=d[1]
    print(f)