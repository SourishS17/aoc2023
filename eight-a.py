t=0 

x="""RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)""".split("\n\n")

a,b=x
y={}
for i in b.splitlines():
    q,w=i.split(" = ")
    w=w.replace("(","").replace(")","").split(", ")
    # print(q)
    y[q]=(w[0],w[1])

g="AAA"
for i in range(99999999):
    if a[i%len(a)] =="R":
        g=y[g][1]
    else:
        g=y[g][0]
        
    if g=="ZZZ":
        t=i+1
        break

print(t) 



