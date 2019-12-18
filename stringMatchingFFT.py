from Complex import *
import math

from recursiveFFT import *
def multiplyPolyFFT(A,B):
    As = recursiveFFT(make_pow_of_2(A))
    Bs = recursiveFFT(make_pow_of_2(B))
    Cs = point_repn_mult(As,Bs)
    C  = convert_to_real(divide(recursiveIFFT(Cs),len(Cs)))
    return C

P = 'a*b**a'
S = 'ababbaababbbbabababbbbaaaababbabab'
print(S)
print(P)
fmap = {'a': ComplexA(5*math.pi/16), 'b': ComplexA(3*math.pi/16),'*':Complex(0,0)}
rmap = {'a': ComplexA(-5*math.pi/16), 'b': ComplexA(-3*math.pi/16),'*':Complex(0,0)}

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
C = multiplyPolyFFT(A,B)[:len(P)+len(S)-1]
Cs = []
for a in C:
	if a<0.0000000001:
		Cs.append(0)
	else:
		Cs.append(a)
Cs = Cs[len(P)-1:len(Cs)-len(P)+1]
Cs.reverse()
print(Cs,len(A),len(B))
R = []
for i in range(len(Cs)):
    if Cs[i] == len(P)-stars:
        R.append(i)
print(R)





