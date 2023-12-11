from copy import deepcopy as dp

t=0 

x="""...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""".splitlines()

y=[]
for i in x:
    y.append(i)
    if "#" not in i:
        y.append(i)


y=list(zip(*y))
x=dp(y)
y=[]


for i in x:
    y.append(i)
    if "#" not in i:
        y.append(i)


x=dp(y)
v=set()
for i in range(len(x)):
    for r in range(len(x[0])):
        if x[i][r]=="#":
            v.add((i,r))

v=list(v)
for i in range(len(v)):
    for r in range(i+1,len(v)):
        t+=abs(v[i][0]-v[r][0])+abs(v[i][1]-v[r][1])



print(t) 

