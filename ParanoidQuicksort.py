import random
from time import time
def swap(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
            
def partition(A,p,r):
    y = random.randint(p,r)
    swap(A,y,p)
    x = A[p]
    i = p
    for j in range(p+1,r+1):
        if A[j]<=x:
            i+=1
            swap(A,i,j)
    swap(A,i,p)
    return i



def ParanoidQuicksort(A,p,r):
    if p<r:
        q = partition(A,p,r)
        ParanoidQuicksort(A,p,q-1)
        ParanoidQuicksort(A,q+1,r)

A = [random.randint(1,100000) for x in range(1000000)]
t1 = time()
ParanoidQuicksort(A,0,len(A)-1)
t2 = time()
print(A[:10],t2-t1)
        

import random
def quicksort(L):
    if len(L) <= 1:
        return L
    pivot = L[random.randint(0,len(L)-1)] # randint is inclusive
    i = 0
    j = len(L)-1
    while i<j:
        if L[i]>=pivot and L[j]<pivot: # changed L[i]>pivot to L[i]>=pivot
            L[i],L[j] = L[j],L[i]
        if L[i] <= pivot:
            i += 1
        if L[j] >= pivot:
            j -= 1
    return quicksort(L[0:i])+quicksort(L[i:])
quicksort([2,1,4,5,0])
