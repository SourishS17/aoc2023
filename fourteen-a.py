t=0 
x="""O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""".splitlines()

x=list(zip(*x))
x=[p[::-1] for p in x]

for i in x:
    i="".join(i)
    for r in range(len(i)):
        if i[r]=="O":
            q=i[r:].find("#")
            if q==-1:q=len(i)+1
            else:q+=1;q+=r
            print(q)
            w=i[r:q].count("O")
            t+=q
            t-=w

print(t) 

