import random
from time import time
def merge(left,right):
    merged = []
    i = 0
    j = 0
    while(i<len(left) and j<len(right)):
        if(left[i] < right[j]):
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
    if i<len(left):
        merged.extend(left[i:])
    elif j<len(right):
        merged.extend(right[j:])
    return merged

def mergesort(A):
    if len(A) <= 1:
        return A
    else:
        mid = (len(A)-1)//2
        left = mergesort(A[:mid+1])
        right = mergesort(A[mid+1:])
        return merge(left,right)

def pickX(S):
    if len(S) <=5:
        cell = mergesort(S)
        print(cell,S)
        return cell[len(cell)//2]
    else:
        medians = []
        for i in range(len(S)//5):
            cell = S[i*5: (i+1)*5]
            print(cell)
            cell = mergesort(cell)
            medians.append(cell[len(cell)//2])
        print(medians)
        return pickX(medians)

def lt(S,x):
    l = []
    g = []
    for a in S:
        if a<x:
            l.append(a)
        elif a>x:
            g.append(a)

    return g,l
    
def select(S,i):
    x = pickX(S)
    B,C = lt(S,x)
    print("bc",B,C,S,x)
    k = len(C)

    if k == i:
        return x
    elif k>i:
        return select(B,i)
    else:
        return select(C,i-k)

