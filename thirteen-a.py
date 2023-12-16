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
    for ii in range(1,len(i)):
        for r in range(min(ii,len(i)-ii)):
            if i[ii-1-r]!=i[ii+r]:
                break
        else:
            t+=100*ii

    i=list(zip(*i))

    for ii in range(1,len(i)):
        for r in range(min(ii,len(i)-ii)):
            if i[ii-1-r]!=i[ii+r]:
                break
        else:
            t+=ii

print(t) 

