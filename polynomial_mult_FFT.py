from recursiveFFT import *
def multiplyPolyFFT(A,B):
    As = recursiveFFT(make_pow_of_2(convert_to_complex(A)))
    Bs = recursiveFFT(make_pow_of_2(convert_to_complex(B)))
    Cs = point_repn_mult(As,Bs)
    C  = convert_to_real(divide(recursiveIFFT(Cs),len(Cs)))
    return C
A = [1,2]
B = [2,3]
print(multiplyPolyFFT(A,B))

def convert_to_coef(x):
    x = str(x)
    coef = []
    for i in range(1,len(x)+1):
        coef.append(int(x[-i]))
    return coef

def multiplyIntFFT(x,y):
    return evaluate(multiplyPolyFFT(convert_to_coef(x),convert_to_coef(y)),10)
    
print(multiplyIntFFT(123,345),123*345)
