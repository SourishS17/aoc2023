from math import gcd
from copy import deepcopy as dp

t=0 
x="""LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)""".split("\n\n")
a,b=x
y={}
for i in b.splitlines():
    q,w=i.split(" = ")
    w=w.replace("(","").replace(")","").split(", ")
    # print(q)
    y[q]=(w[0],w[1])

g=[]
for i in y.keys():
    if i[-1]=="A":g.append(i)

d={}
s={}
for i in range(99999999999999999999999):
    j=[]
    l=0
    for gg in g:
        if a[i%len(a)] =="R":
            h=y[gg][1]
        else:
            h=y[gg][0]
            
        j.append(h)
        if h[-1]=="Z":
            l+=1

            f=d.get(gg,-1)
            if f==-1:
                d[gg]=i+1
            else:
                s[gg]=(i+1-f)
                



    if l==len(j):
        t=i+1
        break
    if len(s.keys())==len(j):
        lcm=1
        for ii in s.values():
            lcm=lcm*ii//gcd(lcm,ii)
        k=lcm
        print(k)
        break

    g=dp(j)


print(t) 

