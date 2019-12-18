import random

def Partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i = i+1
        temp = A[j]
        A[j] = A[i]
        A[i] = temp
    temp = A[i+1]
    A[i+1] = A[r]
    A[r] = temp
    return i+1

def randomized_partition(A,p,r):
    i = random.randint(p,r)
    temp = A[r]
    A[r] = A[i]
    A[i] = temp
    return Partition(A,p,r)

def randomized_select(A,p,r,i):
    if p == r:
        return A[p]
    q = randomized_partition(A,p,r)
    k = q-p+1
    if i == k:
        return A[q]
    elif i<k:
        return randomized_select(A,p,q-1,i)
    else:
        return randomized_select(A,q+1,r,i-k)

print(randomized_select([1,3,2],0,2,3))
    
