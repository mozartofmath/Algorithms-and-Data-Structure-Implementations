def RecursiveKaratsuba(A,B):
    if len(str(A)) == 1 and len(str(B)) == 1:
        return A*B
    strA = str(A)
    strB = str(B)
    if len(strA)>len(strB):
        for i in range(len(strA)-len(strB)):
            strB = '0'+strB
    elif len(strA)<len(strB):
        for i in range(len(strB)-len(strA)):
            strA = '0'+strA
    
    A1 = int(strA[:len(strA)//2])
    A2 = int(strA[len(strA)//2:])
    B1 = int(strB[:len(strB)//2])
    B2 = int(strB[len(strB)//2:])
    ap = 10**(len(strA)-len(strA)//2)
    bp = 10**(len(strB)-len(strB)//2)
    
    A1B1 = RecursiveKaratsuba(A1,B1)
    A2B2 = RecursiveKaratsuba(A2,B2)
    P = RecursiveKaratsuba((A1+A2),(B1+B2))
    R = P - A2B2 - A1B1

    result = A1B1*ap*bp + A2B2 + R*bp
    return result

print(RecursiveKaratsuba(1234,5678))
