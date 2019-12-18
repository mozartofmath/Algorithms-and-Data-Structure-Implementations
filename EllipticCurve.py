import random
from Point import *
class EllipticCurve:
    def __init__(self,a,b,p,h,n):
        self.a = a
        self.b = b
        self.p = p
        self.h = h
        self.n = n
        
    def generator_point(self):
        pass

    def generate_key(self,G):
        secret_key = random.randint(1,self.n - 1)
        public_key = G.multiply(secret_key)
        return [secret_key, public_key]
