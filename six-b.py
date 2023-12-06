t=1

x="""Time:      7  15   30
Distance:  9  40  200"""
a,b=[71530,940200]

for i in range(1):
    aa=[]
    q=0
    for ii in range(1,a[i]):
        q+=1
        j=a[i]-ii
        j=j*q
        if j>b[i]:
            aa.append(ii)
    t*=len(aa)

print(t) 

