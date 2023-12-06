t=1

x="""Time:      7  15   30
Distance:  9  40  200"""
a,b=[7,15,30],[9,40,200]

for i in range(4):
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

