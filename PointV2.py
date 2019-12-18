
class Point:
    def __init__(self,x,y,curve):
        self.x = x
        self.y = y
        self.curve = curve

    def inverse(self):
        return Point(self.x,(-self.y)%self.curve.p,self.curve)

    def double(self):
        if self.gcd((2*self.y)%self.curve.p,self.curve.p) != 1 and self.gcd((2*self.y)%self.curve.p,self.curve.p) != self.curve.p:
            print(self.gcd((2*self.y)%self.curve.p,self.curve.p))
            exit()
        s = ((3*self.x**2 + self.curve.a)*(self.extended_euclidian((2*self.y)%self.curve.p, self.curve.p)))%self.curve.p
        x2p = (s*s - 2*self.x)%self.curve.p
        y2p = (s*(self.x - x2p) - self.y)%self.curve.p
        return Point(x2p,y2p,self.curve)

    def add(self, point):
        if self.x == point.x and self.y == point.y:
            return self.double()
        if self.gcd((self.x - point.x)%self.curve.p,self.curve.p) != 1 and self.gcd((self.x - point.x)%self.curve.p,self.curve.p) != self.curve.p:
            print(self.gcd((self.x - point.x)%self.curve.p,self.curve.p))
            exit()
        s = ((self.y - point.y)*self.extended_euclidian((self.x - point.x)%self.curve.p, self.curve.p))%self.curve.p
        xR = (s*s - (self.x + point.x))%self.curve.p
        yR = (s*(self.x - xR) - self.y)%self.curve.p

        return Point(xR,yR,self.curve)

    def subtract(self,point):
        return self.add(point.inverse())

    def multiply(self,c):
        bin_c = self.toBinary(c)
        P = Point(self.x,self.y,self.curve)
        for i in range(1,len(bin_c)+1):
            if bin_c[-i] == 1:
                break
            else:
                P = P.double()
        Q = Point(P.x,P.y,P.curve)

        for j in range(i+1,len(bin_c)+1):
            P = P.double()
            if bin_c[-j] == 1:
                Q = Q.add(P)
        return Q
            
    def extended_euclidian(self,a,b):
        qi = [0,0]
        ri = [max(a,b),min(a,b)]
        si = [1,0]
        ti = [0,1]

        while(ri[-1] != 0):
            qi.append(ri[-2] // ri[-1])
            ri.append(ri[-2] % ri[-1])
            si.append(si[-2] - qi[-1]*si[-1])
            ti.append(ti[-2] - qi[-1]*ti[-1])
        return (max(a,b) + ti[-2])%max(a,b)

    def gcd(self,a,b):
        if min(a,b)==0:
            return max(a,b)
        else:
            return self.gcd(min(a,b),max(a,b)%min(a,b))
        
    def toBinary(self,a):
        l=[]
        quo = a
        rem = 0
        while quo !=0:
            rem = quo % 2
            quo = quo // 2
            l.append(rem)
            
        l.reverse()
        return l
    def Print(self):
        print("("+str(self.x)+","+str(self.y)+")")
