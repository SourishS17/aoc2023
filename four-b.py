from subprocess import Popen, PIPE
from time import sleep 
from collections import defaultdict as dd 
from collections import deque as de 
from collections import Counter as cn 
from string import ascii_uppercase as au 
from string import ascii_lowercase as al 
from copy import deepcopy as dp 
from itertools import * 
from math import prod 
from math import factorial 
from sys import exit 
from sys import setrecursionlimit as srl 
from statistics import mode 
from statistics import median 
from heapq import * 
from re import * 
# import networkx as nx 
# max(set(lst), key=lst.count) # most common item in lst

t=0 


x="""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".splitlines()

y={}
for i in x:
    a,b=i.split(" | ")
    c,a=a.split(": ")
    a=[int(r) for r in a.split()]
    b=[int(r) for r in b.split()]
    c=int(c.split()[1])
    y[c]=(a,b)


v={i:1 for i in range(1,205)}
t=len(x)
i=1
while 1:
    try:
        ii=v[i]
    except:break
    a,b=y[i]

    q=0
    for r in b:
        if r in a:
            q+=1
    
    print(q)
    print(i+q+1)
    for w in range(i+1,i+q+1):
        v[w]+=(1*ii)
    q*=ii
    t+=q
    i+=1


t=sum(v.values())







print(t) 

def copy_clipboard(msg):
    with Popen(['xclip','-selection', 'clipboard'], stdin=PIPE) as pipe:
        pipe.communicate(input=msg.encode('utf-8'))

copy_clipboard(str(t))



