memo = {}
def memoizedMakeChange(n,L): #O(nm) time, O(nlogn) space
    if n==0:
        return 0
    elif n<L[0]:
        return float('inf')
    elif n in memo:
        return memo[n]
    else:
        opt = float('inf')
        for i in range(len(L)-1, -1, -1):
            if L[i]<=n:
                opt = min(opt,1+memoizedMakeChange(n-L[i],L))
        memo[n] = opt
        return opt

