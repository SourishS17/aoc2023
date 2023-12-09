t=0 

x="""0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""".splitlines()

for i in x:
    i=[int(r) for r in i.split()]
    a=-1 
    q=[]
    q.append(dp(i))
    g=[]
    k=0
    while 1:
        qq=[]
        for ii in range(len(q[k])-1):
            qq.append(q[k][ii+1]-q[k][ii])
        q.append(dp(qq))
        k+=1
        if not (any(qq)):
            break

    for ii in range(len(q)-1,0,-1):
        q[ii-1][-1]+=q[ii][-1]
    t+=q[0][-1]

            


print(t) 


