t=0 

x="""two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".splitlines()

y="one two three four five six seven eight nine".split()

for i in x:
    for r in y:
        i=i.replace(r,r+str(y.index(r)+1)+r)
    a=""
    for ii in i:
        if ii.isdigit():a+=ii
    t+=int(a[0]+a[-1])
 

print(t) 

