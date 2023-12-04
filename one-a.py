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
# max(set(lst), key=lst.count) 

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

def copy_clipboard(msg):
    with Popen(['xclip','-selection', 'clipboard'], stdin=PIPE) as pipe:
        pipe.communicate(input=msg.encode('utf-8'))

copy_clipboard(str(t))
 



