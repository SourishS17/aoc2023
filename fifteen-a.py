t=0 

x="rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
x=x.split(",")

q=0
for i in x:
    q=0
    for ii in i:
        q+=ord(ii)
        q*=17
        q%=256

    t+=q

print(t) 

