import random
import math

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
def gen_prime(begin,end):
    for i in range(10000):
        p=random.randint(begin,end)
        if expmod(2,p-1,p)==1:
            return p
    

def extended_euclidian(a,b):
    qi = [0,0]
    ri = [max(a,b),min(a,b)]
    si = [1,0]
    ti = [0,1]

    while(ri[-1] != 0):
        qi.append(ri[-2] // ri[-1])
        ri.append(ri[-2] % ri[-1])
        si.append(si[-2] - qi[-1]*si[-1])
        ti.append(ti[-2] - qi[-1]*ti[-1])
    return ti[-2]

def GenKeys(BlockSize):
    SuperIncreasing = []
    Sum = 0
    for i in range(BlockSize):
        r = random.randint(Sum+1, 5*(Sum+1))
        SuperIncreasing.append(r)
        Sum += r
    M =  random.randint(int(Sum/2),Sum-1)
    N =  gen_prime(Sum+1,2*Sum)
    PublicKey = [(element*M)%N for element in SuperIncreasing]
    return PublicKey, SuperIncreasing, M, N

def Encrypt(PK,m):
    c = 0
    for i in range(len(m)):
        if m[i] == '1':
            c += PK[i]
    return c

def Decrypt(SK,M,N,c):
    MInv = (extended_euclidian(M,N) + N) % N
    temp = (c * MInv)%N
    m = ''
    print(temp, MInv)
    for i in range(len(SK)):
        if temp >= SK[len(SK) - i - 1]:
            m = '1' + m
            temp -= SK[len(SK) - i - 1]
        else:
            m = '0' + m
    return m


BlockSize = 24
PublicKey, SuperIncreasing, M, N = GenKeys(BlockSize)
m = '0' + bin(ord('a'))[2:] + '0' + bin(ord('b'))[2:] + '0' + bin(ord('c'))[2:]
c = Encrypt(PublicKey,m)
dec = Decrypt(SuperIncreasing, M, N, c)
print(m,c,dec, m==dec)

    

    
