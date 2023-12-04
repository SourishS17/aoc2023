from collections import defaultdict as dd

t=0 


x="""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".splitlines()
y=dd(str)
for i in range(len(x)):
    for r in range(len(x[0])):
        y[(i,r)]=x[i][r]
 

a,b=0,0
while 1:
    if y[(a,b)].isdigit():
        aa=""
        for i in range(b,b+10):
            if y[(a,i)].isdigit():
                aa+=y[(a,i)]
            else:break
        aa=int(aa)
        l=0
        for ii in range(a-1,a+2):
            for iii in range(b-1,i+1):
                if y[(ii,iii)].isdigit():continue
                if len(y[(ii,iii)])==1 and y[(ii,iii)]!= ".":
                    if l:continue
                    t+=aa
                    l=1
                    print(aa)


        b=i
        if b>=len(x[0]):
            b=0
            a+=1
            if a>=len(x):
                break



    else:
        b+=1
        if b>=len(x[0]):
            b=0
            a+=1
            if a>=len(x):
                break
 

 

print(t) 

