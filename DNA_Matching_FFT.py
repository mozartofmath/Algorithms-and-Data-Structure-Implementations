from Complex import *
import math
from time import time

from recursiveFFT import *
def multiplyPolyFFT(A,B):
    As = recursiveFFT(make_pow_of_2(A))
    Bs = recursiveFFT(make_pow_of_2(B))
    Cs = point_repn_mult(As,Bs)
    C  = convert_to_real(divide(recursiveIFFT(Cs),len(Cs)))
    return C

P = 'AC*A'
S = 'ACGACCAT'
print(S)
print(P)
fmap = {'A': ComplexA(5*math.pi/16), 'C': ComplexA(3*math.pi/16),'T': ComplexA(7*math.pi/16), 'G': ComplexA(1*math.pi/16),'*':Complex(0,0)}
rmap = {'A': ComplexA(-5*math.pi/16), 'C': ComplexA(-3*math.pi/16),'T': ComplexA(-7*math.pi/16), 'G': ComplexA(-1*math.pi/16),'*':Complex(0,0)}

stars = 0
for sym in P:
    if sym == '*':
        stars+=1


def convert_P(P):
    coef = []
    for i in range(len(S)):
        if i>=len(P):
            coef.append(Complex(0,0))
        else:
            coef.append(rmap[P[i]])
    
    return coef

def convert_S(S):
    coef = []
    for i in range(1,len(S)+1):
        coef.append(fmap[S[-i]])
    return coef


A = convert_S(S)
B = convert_P(P)
t1 = time()
C = multiplyPolyFFT(A,B)[:len(P)+len(S)-1]
print('FFT',time()-t1)
Cs = []
for a in C:
	if a<0.0000000001:
		Cs.append(0)
	else:
		Cs.append(a)
Cs = Cs[len(P)-1:len(Cs)-len(P)+1]
Cs.reverse()
R = []
for i in range(len(Cs)):
    if Cs[i] == len(P)-stars:
        R.append(i)
print(R)

'''l = []
t1 = time()
for i in range(1000):
    a = ComplexA(i*math.pi/128)
print(time()-t1)
l = []
t1 = time()
for i in range(1000):
    a = [math.pi,-math.pi]'''

print(time()-t1)

