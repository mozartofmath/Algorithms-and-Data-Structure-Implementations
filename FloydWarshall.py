def FloydWarshall(W):
    n = len(W)
    D0 = W
    for k in range(n):
        Dk = [[float('inf') for x in range(n)] for y in range(n)]
        for i in range(n):
            for j in range(n):
                Dk[i][j] = min(D0[i][j], D0[i][k]+D0[k][j])
        D0 = Dk
    return Dk

i = float('inf')
W = [
        [0,3,8,i,-4],
        [i,0,i,1,7],
        [i,4,0,i,i],
        [2,i,-5,0,i],
        [i,i,i,6,0]
    ]
print(FloydWarshall(W))
