from functools import cache

t=0 

x="""???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

x=[("?".join([i.split()[0]]*5),tuple(int(r) for r in i.split()[1].split(","))*5) for i in x.splitlines()]

@cache
def d(a,b,l):
    # print(a,b,l)
    y=0
    ll=0

    if b[0]==0:b=b[1:];ll=1
    
    if len(b)==0:
        if a.count("#")==0:return 1
        if len(a)==0:return 1
        return 0
    if len(a)==0:
        return 0

    if a[0]==".":
        if ll==0 and b[0] and l:return 0
        y+=d(a[1:],b,0)
    elif a[0]=="#":
        if ll and l:return 0
        y+=d(a[1:],(b[0]-1,)+b[1:],1)
    else:
        if not(ll and l):
            y+=d(a[1:],(b[0]-1,)+b[1:],1)
        if not(ll==0 and l):
            y+=d(a[1:],b,0)

    return y



for a,b in x:
    t+=d(a,b,0)



print(t) 
