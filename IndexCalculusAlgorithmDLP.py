import random
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

def FactorOverBase(n , Base):
    exponents = []
    if n>0:
        exponents.append(0)
    else:
        exponents.append(1)
    for i in range(1,len(Base)):
        ei = 0
        while n%Base[i]==0:
            n = n//Base[i]
            ei+=1
        exponents.append(ei)
    if n != 1:
        return -1
    else:
        return exponents

Q = 101
FactorBase = [-1,2,3,5,7]
g = 11
h = 13

relations = []
k = 2
while len(relations) <= len(FactorBase):
    es = FactorOverBase(expmod(g,k,Q),FactorBase) 
    if es!=-1:
        es.append(k)
        relations.append(es)
    k+=1
print(relations)
































