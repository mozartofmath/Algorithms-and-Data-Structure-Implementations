#Fermat's Primality Test
import math
import random

def toBinary(a):
    c=math.floor(math.log(a,2))
    l=[]
    for i in range(int(c),-1,-1):
        
        if a - 2**i >= 0:
            l.append(1)
            a=a - 2**i
        else:
            l.append(0)
    return l    

def expmod(b,a,c):
    abin= toBinary(a)
    r=1
    for i in range(len(abin)-1,-1,-1):
        if abin[i]==1:
            r=(r*b)%c
        b=(b**2)%c
    return r
def gen_prime(begin,end)
    for i in range(10000):
        p=random.randint(begin,end)
        if expmod(2,p-1,p)==1:
            return p
    
