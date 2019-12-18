import random
from EllipticCurve import *
from Point import *

def encrypt(M,PK,G):
    r = random.randint(1,M.curve.n - 1)
    print("r:",r)
    while PK.multiply(r).x == M.x:
        r = random.randint(1,M.curve.n - 1)
        print("r:",r)
    rG = G.multiply(r)
    eM = M.add(PK.multiply(r))
    return [rG,eM]

def decrypt(C,sk,G):
    rPK = C[0].multiply(sk)
    M = C[1].subtract(rPK)
    return M

def main():
    curve = EllipticCurve(2,2,17,1,19)
    G = Point(5,1,curve)
    secret_key = random.randint(1,curve.n - 1)
    public_key = G.multiply(secret_key)
    
    public_key.Print()
    

    M = Point(3,1,curve)
    print("plain: ("+str(M.x)+","+str(M.y)+")")
    C = encrypt(M, public_key, G)

    print("encrypted: ("+str(C[1].x)+","+str(C[1].y)+")")
    decM = decrypt(C, secret_key, G)

    print("decrypted: ("+str(decM.x)+","+str(decM.y)+")")
    M.double().Print()
    M.add(M).Print()

main()
curve = EllipticCurve(2,2,17,1,19)
G = Point(5,1,curve)
S = Point(5,1,curve)
print("testing")
P = G.multiply(11)
S.multiply(11).add(P).Print()
S.Print()
'''
for i in range(1,19):
    S = S.add(G)
    S.Print()'''

