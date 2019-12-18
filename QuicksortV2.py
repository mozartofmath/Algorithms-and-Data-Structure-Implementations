import random
def swap(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
            
def partition(A,p,r):
    y = random.randint(p,r)
    swap(A,y,p)
    print(y,p,A[y],A)
    x = A[p]
    i = p
    for j in range(p+1,r+1):
        if A[j]<=x:
            i+=1
            swap(A,i,j)
    swap(A,i,p)
    return i

def RandomizedQuicksort(A,p,r):
    if p<r:
        q = partition(A,p,r)
        RandomizedQuicksort(A,p,q-1)
        RandomizedQuicksort(A,q+1,r)
        


        
def quicksort(L,low,high):
    #print(L)
    if low >= high:
        return L
    pivot = L[random.randint(low,high)]
    i = low
    j = high
    while i<=j:
        if L[i]>=pivot and L[j]<=pivot:
            L[i],L[j] = L[j],L[i]
        if L[i]<=pivot:
            i+=1
        if L[j]>=pivot:
            j-=1
    quicksort(L,low,i-1)
    quicksort(L,i,high)
    return L
L = [random.randint(1,1000) for _ in range(1000)]
print(quicksort(L,0,len(L)-1)==sorted(L))
