from statistics import mode 

t=0 
x="""32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".splitlines()

y=[]
vv="AKQT98765432J"
vv=vv[::-1]
v={r:i for i,r in enumerate(vv)}
print(v)

def d(a):
    a,b=a.split()
    aa=a
    b=int(b)
    h=[]
    if mode(list(a))=="J":
        c=a.replace("J","")
        if len(c)==0:
            a=a.replace("J","A")
        else:a=a.replace("J",mode(list(c)))
    l=a.count("J")
    if l>0:k=1
    else:k=0
    if a.count(mode(list(a)))+l==5:
        h.append(10)
        for i in aa:h.append(v[i])
    elif a.count(mode(list(a)))+l==4:
        h.append(9)
        for i in aa:h.append(v[i])
    elif len(set(a))-k==2:
        h.append(8)
        for i in aa:h.append(v[i])
    elif a.count(mode(list(a)))+l==3:
        h.append(7)
        for i in aa:h.append(v[i])
    elif len(set(a))-k==3 and a.count(mode(list(a)))+l==2:
        h.append(6)
        for i in aa:h.append(v[i])
    elif len(set(a))-k==4 and a.count(mode(list(a)))+l==2:
        h.append(5)
        for i in aa:h.append(v[i])
    else:
        h.append(4)
        for i in aa:h.append(v[i])
    return tuple(h),b

for i in x:
    a,b=d(i)
    y.append(a)
    
y=sorted(y)

for i,r in enumerate(y):
    for ii in x:
        a,b=d(ii)
        if a==r:
            t+=(i+1)*b
            break




print(t) 

