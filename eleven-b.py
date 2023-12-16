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

q=[]
for i in x:
    if all(r=="." for r in i):
        q.append(1000000)
    else:q.append(1)

y=list(zip(*x))

qq=[]
for i in y:
    if all(r=="." for r in i):
        qq.append(1000000)
    else:qq.append(1)

w=set()
q=[i-1 for i in q]
qq=[i-1 for i in qq]
for i in range(len(x)):
    for r in range(len(x[0])):
        if x[i][r]=="#":w.add((i+sum(q[:i]),r+sum(qq[:r])))

for i in w:
    for r in w:
        t+=abs(i[0]-r[0])+abs(i[1]-r[1])

t//=2

print(t) 

