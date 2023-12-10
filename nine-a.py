t=0 

x="""0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""".splitlines()


def d(a):
    aa=[a[i+1]-a[i]for i in range(len(a)-1)]
    if all(i==0 for i in aa):
        return a[-1]
    return a[-1]+d(aa)

for i in x:
    i=[int(r) for r in i.split()]
    t+=d(i)


print(t) 

