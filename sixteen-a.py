from collections import deque as de 

t=0 

x=r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....""".replace("\\","w").splitlines()
for i in range(len(x[0])):
    v=set()
    vv=set()

    a,b=0,0
    q=de([(a,b,1)])
    while q:

        a,b,c=q.popleft()
        if (a,b,c) in v:continue
        v.add((a,b,c))
        vv.add((a,b))

        if c==0:
            for aa in range(a-1,-1,-1):
                if x[aa][b] not in ".|":
                    break
                v.add((aa,b,c))
                vv.add((aa,b))
            else:
                continue

            if x[aa][b]=="/":
                q.append((aa,b,1))
            elif x[aa][b]=='w':
                q.append((aa,b,3))
            elif x[aa][b]=='-':
                q.append((aa,b,3))
                q.append((aa,b,1))
        elif c==2:
            for aa in range(a+1,len(x)):
                if x[aa][b] not in ".|":
                    break
                v.add((aa,b,c))
                vv.add((aa,b))
            else:
                continue

            if x[aa][b]=="/":
                q.append((aa,b,3))
            elif x[aa][b]=='w':
                q.append((aa,b,1))
            elif x[aa][b]=='-':
                q.append((aa,b,3))
                q.append((aa,b,1))
        elif c==1:
            for bb in range(b+1,len(x[0])):
                if x[a][bb] not in ".-":
                    break
                v.add((a,bb,c))
                vv.add((a,bb))
            else:
                continue
            if x[a][bb]=="/":
                q.append((a,bb,0))
            elif x[a][bb]=='w':
                q.append((a,bb,2))
            elif x[a][bb]=='|':
                q.append((a,bb,0))
                q.append((a,bb,2))
        elif c==3:
            for bb in range(b-1,-1,-1):
                if x[a][bb] not in ".-":
                    break
                v.add((a,bb,c))
                vv.add((a,bb))
            else:
                continue
            if x[a][bb]=="/":
                q.append((a,bb,2))
            elif x[a][bb]=='w':
                q.append((a,bb,0))
            elif x[a][bb]=='|':
                q.append((a,bb,0))
                q.append((a,bb,2))



t=len(vv)


print(t) 

