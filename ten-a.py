t=0 

x="""..F7.
.FJ|.
SJ.L7
|F--J
LJ...""".splitlines()

for i in range(len(x)):
    for r in range(len(x[0])):
        if x[i][r]=="S":
            a=(i,r)
            x[i].replace("S","L")
            break
    else:continue
    break

q=a
y={}
d=0
i=0
v=set()
while 1:
    w=x[a[0]][a[1]]
    print(w)
    if a==q and i>0:break
    # e=abs(a[0]-q[0])+abs(a[1]-q[1])
    # if a in v:
    #     break
    # v.add(a)
    # y[e]=min(i,y[e])
    i+=1
    if w=="|":
        if d==0:
            a=(a[0]-1,a[1])
        else:
            a=(a[0]+1,a[1])
    if w=="-":
        if d==1:
            a=(a[0],a[1]+1)
        else:
            a=(a[0],a[1]-1)
    if w=="L" or w=="S": # HARDCODED VALUE BE CAREFUL - UNIQUE ON INPUT
        if d==2:
            a=(a[0],a[1]+1)
            d=1
        else:
            a=(a[0]-1,a[1])
            d=0
    
    if w=="J":
        if d==2:
            a=(a[0],a[1]-1)
            d=3
        else:
            a=(a[0]-1,a[1])
            d=0

    if w=="7":
        if d==0:
            a=(a[0],a[1]-1)
            d=3
        else:
            a=(a[0]+1,a[1])
            d=2

    if w=="F":
        if d==0:
            a=(a[0],a[1]+1)
            d=1
        else:
            a=(a[0]+1,a[1])
            d=2


print(i)
t=i//2

print(t) 

