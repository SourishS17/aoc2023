t=0 

x="""1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".splitlines()
 

for i in x:
    a=""
    for ii in i:
        if ii.isnumeric():
            a+=ii
    t+=int(a[0]+a[-1])


print(t) 

