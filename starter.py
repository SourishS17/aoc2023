from subprocess import Popen, PIPE
from functools import cache
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
from math import gcd
from math import lcm
from sys import exit 
from sys import setrecursionlimit as srl 
from statistics import mode 
from statistics import median 
from heapq import * 
from re import * 
# import networkx as nx 

t=0 















print(t) 

def copy_clipboard(msg):
    with Popen(['xclip','-selection', 'clipboard'], stdin=PIPE) as pipe:
        pipe.communicate(input=msg.encode('utf-8'))

copy_clipboard(str(t))











