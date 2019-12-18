import random
from EllipticCurve import *
from PointV2 import *

def randomCurve(N):
    x0 = random.randint(2,N-1)
    y0 = random.randint(2,N-1)
    a  = random.randint(2,N-1)
    b  = (y0**2 - x0**3 - a*x0)%N
    return Point(x0,y0,EllipticCurve(a,b,N,0,0))

def main():
    N = 455839
    B = 100
    curve = EllipticCurve(5,-5,N,0,0)
    G = Point(1,1,curve)
    P = G

    for i in range(2,B+1):
        P = P.multiply(i)
main()
        
    
    
    
