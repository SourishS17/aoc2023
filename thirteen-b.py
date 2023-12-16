t=0 

x="""#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#""".split("\n\n")

x=[i.splitlines() for i in x]

for i in x:
    j=[0,0]
    for ii in range(1,len(i)):
        for r in range(min(ii,len(i)-ii)):
            if i[ii-1-r]!=i[ii+r]:
                break
        else:
            j[0]=ii

    i=list(zip(*i))

    for ii in range(1,len(i)):
        for r in range(min(ii,len(i)-ii)):
            if i[ii-1-r]!=i[ii+r]:
                break
        else:
            j[1]=ii

    i=list(zip(*i))
    iii=dp([list(q) for q in i])

    for q in range(len(iii)):
        for qq in range(len(iii[0])):
            i=dp(iii)
            i[q][qq]="#" if i[q][qq]=="." else "."
            
            for ii in range(1,len(i)):
                for r in range(min(ii,len(i)-ii)):
                    if i[ii-1-r]!=i[ii+r]:
                        break
                else:
                    if ii!=j[0]:
                        t+=100*ii

            i=list(zip(*i))

            for ii in range(1,len(i)):
                for r in range(min(ii,len(i)-ii)):
                    if i[ii-1-r]!=i[ii+r]:
                        break
                else:
                    if ii!=j[1]:
                        t+=ii


t//=2

print(t) 

