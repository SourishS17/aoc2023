from collections import defaultdict as dd 
from copy import deepcopy as dp

t=0 

x="""seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

a,*x=x.split("\n\n")
a=[int(i) for i in a.split(": ")[1].split()]

t=1e99
for i in range(0,len(a),2):
    y=dd(list)
    y["seed"].append((a[i],a[i]+a[i+1]))

    for ii in x:
        q,*ii=ii.splitlines()
        q,qq=q.split()[0].split("-to-")
        c=dp(y[q])
        # print(y)
        # print(ii)
        while c:
            k=c.pop()
            for iii in ii:
                iii=[int(w) for w in iii.split()]
                n=list(dp(k))
                if iii[1]<k[1] and iii[1]+iii[-1]>k[0]:
                    if iii[1]<=k[0]:
                        n[0]=k[0]+iii[0]-iii[1]
                    else:
                        n[0]=iii[0]
                    if k[1]<=iii[1]+iii[-1]:
                        n[1]=k[1]+iii[0]-iii[1]
                    else:
                        n[1]=iii[0]+iii[-1]
                # print(n,k,qq)
                # if iii[1]<k[0] and iii[1]+iii[-1]>=k[1]:
                #     n[0]=k[0]+iii[0]-iii[1]
                #     n[1]=k[1]+iii[0]-iii[1]
                if (n[0],n[1])!=(k[0],k[1]):
                    if n[0]!=k[0]+iii[0]-iii[1]:
                        c.append((k[0],iii[1]))
                    if n[1]!=k[1]+iii[0]-iii[1]:
                        c.append((iii[1]+iii[-1],k[1]))
                    # print()
                    # print(n)
                    # print(k)
                    # print(iii)
                    # print(c)
                    y[qq].append(tuple(n))
                    # exit(0)
                    break
            else:
                y[qq].append(k)

    y["location"].sort(key=lambda g:g[0])
    t=min(t,y["location"][0][0])



print(t) 

