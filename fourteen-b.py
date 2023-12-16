t=0 
xx="""O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""".splitlines()
x=[list(i) for i in x]
y={}
for i in range(len(x)):
    for r in range(len(x[0])):
        y[(i,r)]=x[i][r]

e=[]
c=1
# for w in range(1000000000):
for w in range(163+(1000000000-163)%18):
    for q in range(4):
        xx=dp(x)
        for i in range(len(x)):
            for r in range(len(x[0])):
                if x[i][r]=="O":
                    xx[i][r]="."
                    ii=i
                    for ii in range(i-1,-1,-1):
                        if xx[ii][r]==".":
                            continue
                        break
                    else:
                        xx[ii][r]="O"
                        continue
                    xx[ii+1][r]="O"
        x=dp(xx)
        x=list(zip(*x))
        x=[list(p[::-1]) for p in x]
        y={}
        for i in range(len(x)):
            for r in range(len(x[0])):
                y[(i,r)]=x[i][r]
        # for i,r in y.items():
        #     yy[(i[1],len(x)-1-i[0])]=r
        # y=dp(yy)

    ee=tuple((i,r) for i,r in y.items())
    # print(w,e.count(ee))
    # sleep(0.02)
    if e.count(ee)==c:
        print(e.index(ee)+1,e[::-1].index(ee))
        c+=1
    e.append(ee)
        

for i,r in y.items():
    if r=="O":
        t+=len(x)-i[0]


for i in range(len(x)):
    for r in range(len(x[0])):
        print(y[(i,r)],end="")
    print()



print(t) 

