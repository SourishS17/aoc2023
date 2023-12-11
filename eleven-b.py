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

for i in range(len(x)):
    if "#" not in x[i]:
        y.append(i)


yy=[]
for r in range(len(x[0])):
    for i in range(len(x)):
        if x[i][r]=="#":break
    else:
        yy.append(r)


print(y)
print(yy)
v=set()

ii=0
rr=0
for i in range(len(x)):
    if i in y:
        ii+=1000000
        ii-=1
    rr=0
    for r in range(len(x[0])):
        if r in yy:
            rr+=1000000
            rr-=1
        if x[i][r]=="#":
            v.add((i+ii,r+rr))

v=list(v)
for i in range(len(v)):
    for r in range(i+1,len(v)):
        t+=abs(v[i][0]-v[r][0])+abs(v[i][1]-v[r][1])





print(t) 

