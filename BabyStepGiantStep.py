import math
from time import time

def pattern(base,pq):
    count=1
    r=base
    while r!=1:
        r=(r*base)%pq
        count+=1
    return count

def toBinary(a):
    l=[]
    quo = a
    rem = 0
    while quo !=0:
        rem = quo % 2
        quo = quo // 2
        l.append(rem)
        
    l.reverse()
    return l

def expmod(b,a,c):
    abin= toBinary(a)
    r=1
    for i in range(len(abin)-1,-1,-1):
        if abin[i]==1:
            r=(r*b)%c
        b=(b**2)%c
    return r

N = 2017*1493
g = 7
r = pattern(g,N)
m = math.ceil(r**0.5)

h = expmod(g,101,N)
d = {}

print("r:",r)
t = time()
for j in range(0,m):
    d[expmod(g,j,N)] = j

for i in range(0,m):
    if (h*(expmod(expmod(g,r-m,N),i,N))%N) in d:
        print(i*m + d[(h*(expmod(expmod(g,r-m,N),i,N))%N)],time()-t)
        break













































