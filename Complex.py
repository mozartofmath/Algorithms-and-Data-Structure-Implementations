import math
class Complex:
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, addend):
        tempr = self.real + addend.real
        tempi = self.imaginary + addend.imaginary
        return Complex(tempr,tempi)
    def subtract(self, sub):
        tempr = self.real - sub.real
        tempi = self.imaginary - sub.imaginary
        return Complex(tempr,tempi)
    def multiply(self, prod):
        tempr = self.real * prod.real - self.imaginary * prod.imaginary
        tempi = self.real * prod.imaginary + self.imaginary * prod.real
        return Complex(tempr,tempi)
    
    def conjugate(self):
        return Complex(self.real, -1*self.imaginary)
    
    def norm(self):
        return math.sqrt(self.real**2 + self.imaginary**2)

    def divide(self, denom):
        tempr = self.real/denom
        tempi = self.imaginary/denom
        return Complex(tempr,tempi)
    
    def exponentiation(self, exponent):
        tempangle = math.acos(self.real/self.norm()) * exponent
        return Complex(math.cos(tempangle),math.sin(tempangle))
        
    def print(self):
        return str(round(self.real,14))+" + "+str(round(self.imaginary,14))+"i"

    
class ComplexA:
        
    def __init__(self,angle):
        self.angle = angle
        self.real = math.cos(angle)
        self.imaginary = math.sin(angle)

    def add(self, addend):
        tempr = self.real + addend.real
        tempi = self.imaginary + addend.imaginary
        return Complex(tempr,tempi)
    
    def subtract(self, sub):
        tempr = self.real - sub.real
        tempi = self.imaginary - sub.imaginary
        return Complex(tempr,tempi)
    
    def multiply(self, prod):
        tempr = self.real * prod.real - self.imaginary * prod.imaginary
        tempi = self.real * prod.imaginary + self.imaginary * prod.real
        return Complex(tempr,tempi)
    
    def divide(self, denom):
        tempr = self.real/denom
        tempi = self.imaginary/denom
        return Complex(tempr,tempi)
    
    def norm(self):
        return math.sqrt(self.real**2 + self.imaginary**2)

    def conjugate(self):
        return Complex(self.real, -1*self.imaginary)
    
    def exponentiation(self, exponent):
        tempangle = self.angle * exponent
        return Complex(math.cos(tempangle),math.sin(tempangle))
        
    def print(self):
        return str(round(self.real,14))+" + "+str(round(self.imaginary,14))+"i"
'''
def main():
    complex1 = Complex(1,2)
    complex2 = Complex(1,-2)
    complex3 = ComplexA(math.pi/6)
    complex1.add(complex2).print()
    complex1.subtract(complex2).print()
    complex1.multiply(complex2).print()
    print(complex3.print())
main()
'''
