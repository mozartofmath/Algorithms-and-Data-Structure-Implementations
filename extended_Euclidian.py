#to find the multiplicative inverse of A mod N, call the function as extended_euclidian(N,A)
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

print(extended_euclidian(11,45113))
