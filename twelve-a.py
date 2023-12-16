from itertools import * 

t=0 

x="""???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".splitlines()

for i in x:
    a,b=i.split()
    b=[int(r) for r in b.split(",")]
    q=[r for r,rr in enumerate(a) if rr=="?"]
    for r in range(0,len(q)+1):
        for ii in combinations(q,r):
            l=list(a)
            for h in ii:
                l[h]="#"
            p=[]
            pp=-2
            for j in range(len(l)):
                if l[j]=="#":
                    if pp==j-1:
                        pp+=1
                        p[-1]+=1
                    else:
                        pp=j
                        p.append(1)
            if p==b:t+=1


print(t) 

