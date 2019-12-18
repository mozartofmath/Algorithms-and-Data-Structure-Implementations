def exp(a,b):
    if b == 0:
        return 1
    if b%2 == 1:
        return a*exp(a*a,b//2)
    return exp(a*a,b//2)

#print(exp(5,100),5**9)

def count(l,target, total, i):
    if target == total:
        return 1
    if i == len(l):
        return 0
    return count(l,target, total, i+1) + count(l,target, total+l[i], i+1)
print(count([2,4,6,10],8,0,0))
