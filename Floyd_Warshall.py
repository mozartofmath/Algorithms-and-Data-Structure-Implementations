def Floyd_Warshall(G):
    G_prev = G
    inf = float('inf')
    for k in range(len(G)):
        Gk = [[0 for _ in range(len(G))] for _ in range(len(G))]
        for i in range(len(G)):
            for j in range(len(G)):
                Gk[i][j] = min(G_prev[i][j], G_prev[i][k] + G_prev[k][j])
        G_prev = Gk
    return Gk

i = float('inf')
G = [
        [0,3,8,i,-4],
        [i,0,i,1,7],
        [i,4,0,i,i],
        [2,i,-5,0,i],
        [i,i,i,6,0]
    ]

for i in range(len(G)):
    G[i][i] = 0

def RecursiveFloyd(W,k):
    if k == -1:
        return W
    inf = float('inf')
    Gk = [[0 for _ in range(len(W))] for _ in range(len(W))]
    G_prev = RecursiveFloyd(W,k-1)
    for i in range(len(Gk)):
        for j in range(len(Gk)):
            Gk[i][j] = min(G_prev[i][j], G_prev[i][k] + G_prev[k][j])
    return Gk

print(RecursiveFloyd(G,len(G)-1)==Floyd_Warshall(G))
    
def Floyd_Warshall_Pred_Matrix(G):
    PM_prev = [[None for _ in range(len(G))] for _ in range(len(G))]
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j]!=0 and G[i][j]!=float('inf'):
                PM_prev[i][j] = i
    G_prev = G
    inf = float('inf')
    for k in range(len(G)):
        PMk = [[None for _ in range(len(G))] for _ in range(len(G))]
        Gk = [[0 for _ in range(len(G))] for _ in range(len(G))]
        
        for i in range(len(G)):
            for j in range(len(G)):
                if G_prev[i][k] + G_prev[k][j] < G_prev[i][j]:
                    Gk[i][j] = G_prev[i][k] + G_prev[k][j]
                    PMk[i][j] = PM_prev[k][j]
                else:
                    Gk[i][j] = G_prev[i][j]
                    PMk[i][j] = PM_prev[i][j]
        G_prev = Gk
        PM_prev = PMk
    
    return Gk, PMk

Gk,PMk = Floyd_Warshall_Pred_Matrix(G)
def printPath(PDM,i,j):
    l = [j]
    c = j
    while PDM[i][c] != i and PDM[i][j] != None:
        print(PDM[i][c],i)
        l.append(PDM[i][c])
        c = PDM[i][c]
    l.append(i)
    l.reverse()
    for v in l[:-1]:
        print(v, end = ' --> ')
    print(j)
printPath(PMk,1,4)
