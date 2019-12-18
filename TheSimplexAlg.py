def toSlackForm(A,b,c):
    n = len(A) + len(A[0]) + 1
    m = len(A)
    Obj = [0] + c + [0]*m
    N = [x for x in range(1,len(A[0])+1)]
    B = [len(A[0]) + x for x in range(1,len(A)+1)]
    newA = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        newA[i][0] = b[i]
    for i in range(len(A)):
        for j in range(len(A[0])):
            newA[i][j+1] = -A[i][j]
    for i in range(m):
        newA[i][len(A[0])+i+1] = 1
    return N,B,newA,Obj

def choose_leaving_var(N,Obj):
    for x in N:
        if Obj[x]>0:
            return x
    return -1
def choose_entering_var(B,A,Obj,l):
    Min = float('inf')
    e = B[0]
    for i in range(len(A)):
        if A[i][l] >= 0:
            continue
        if -A[i][0]/A[i][l] < Min:
            Min = -A[i][0]/A[i][l]
            e = B[i]
    if Min < float('inf'):
        return e
    return -1

def Pivot(N,B,A,Obj,e,l):
    for i in range(len(B)):
        if B[i] == e:
            break
    A[i][e] = -1
    for j in range(len(A[0])):
        if j!=l:
            A[i][j] = -A[i][j]/A[i][l]
    A[i][l] = 1
    vector = A[i].copy()
    vector[l] = 0
    for j in range(len(Obj)):
        if j!=l:
            Obj[j] = Obj[j] + Obj[l]*vector[j]
    Obj[l] = 0
    for k in range(len(A)):
        if k!=i:
            for j in range(len(vector)):
                A[k][j] = A[k][j] + A[k][l]*vector[j]
            A[k][l] = 0
    N.remove(l)
    N.append(e)
    B[i] = l
    return N,B,A,Obj

def Simplex(A,b,c):
    N,B,A,Obj = toSlackForm(A,b,c)
    print(Obj)
    while choose_leaving_var(N,Obj) != -1:
        l = choose_leaving_var(N,Obj)
        e = choose_entering_var(B,A,Obj,l)
        if e == -1:
            return 'unbounded'
        N,B,A,Obj = Pivot(N,B,A,Obj,e,l)
    X = [0 for i in range(len(A[0])-1)]
    for i in range(len(B)):
        X[B[i]-1] = A[i][0]
    return X,Obj[0]

A = [
        [ 1, 1, 3],
        [ 2, 2, 5],
        [ 4, 1, 2]
    ]
b = [30,24,36]
c = [3,1,2]

print(Simplex(A,b,c))























        




















    
