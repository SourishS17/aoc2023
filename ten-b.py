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
    v.add(a)
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
    if w=="L" or w=="S": # HARDCODED - BE CAREFUL - DEPENDENT ON INPUT
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


for i in range(len(x)):
    for ii in range(len(x[0])):
        q,w=0,0
        qq,ww=0,0
        if (i,ii) in v:continue
        for r in range(len(x)):
            if (r,ii)==(i,ii):continue
            if (r,ii) in v and x[r][ii]=="-":
                if r>i:
                    q+=1
                else:qq+=1
        for rr in range(len(x[0])):
            if (i,rr)==(i,ii):continue
            if (i,rr) in v and x[i][rr]in"|JLS":
                if rr>ii:
                    w+=1
                else:ww+=1
        print(w,ww,q,qq)
        if ww%2==1:
            t+=1
            continue

print("DONE")

# vvv=set()
# for h in range(len(x)):
#     for hh in range(len(x[0])):
#         if (h,hh) in v:continue
#         q=de([(h,hh)])
#         vv=set()
#         while q:
#             e,r=q.popleft()
#             if (e,r) in v:continue
#             if (e,r) in vv:continue
#             vv.add((e,r))
#             for ee in range(e-1,e+2):
#                 for rr in range(r-1,r+2):
#                     if (ee==e or rr==r) and 0<=ee<len(x) and 0<=rr<len(x[0]) and (e,r)!=(ee,rr):
#                         q.append((ee,rr))
#         vvv=vvv.union(vv)

# # t=len(vvv)

# # t=(len(x)*len(x[0]))-len(v)-t


print(t) 


