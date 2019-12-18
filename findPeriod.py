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

N = 10**9 + 7
new = N-1
i = 2
while i<100000:
    if new%i == 0 and expmod(10,new//i,N) == 1:
        new = new//i
    else:
        i+=1

print(new)
