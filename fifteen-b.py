from collections import defaultdict as dd 
from copy import deepcopy as dp 

t=0 

x="rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
x=x.split(",")
print(len(x))
y=dd(list)

for i in x:
    q=0
    if "=" in i:
        a,b=i.split("=")
        for ii in a:
            q+=ord(ii)
            q*=17
            q%=256
        if a in [f[0] for f in y[q]]:
            w=[f[0] for f in y[q]].index(a)
            y[q].pop(w)
            y[q].insert(w,(a,int(b)))
        else:
            y[q].insert(0,(a,int(b)))
    else:
        a=i[:-1]
        for ii in a:
            q+=ord(ii)
            q*=17
            q%=256
        e=dp([f[0] for f in y[q]])
        if a not in e:continue
        w=e.index(a)
        y[q].pop(w)
    print(q,a)

       
for i in range(256):
    w=[(1+i)*(ii+1)*rr[1] for ii,rr in enumerate(y[i][::-1])]
    t+=sum(w)

print(y)


print(t) 


