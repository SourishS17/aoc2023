t=0 


x="""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".splitlines()

for i in x:
    q,w=i.split(": ")
    a,b,c=12,13,14

    w=w.split(";")
    
    l=0
    print(q,w)
    for ii in w:
        ii=ii.split(", ")
        a,b,c=12,13,14
        for iii in ii:
            if "red" in iii:
                a-=(int(iii.split()[0]))
            if "green" in iii:
                b-=(int(iii.split()[0]))
            if "blue" in iii:
                c-=(int(iii.split()[0]))

        if not(a>=0 and b>=0 and c >=0):
            l=1
    
    if l==0:
        t+=int(q.split()[1])
 

 

print(t) 

