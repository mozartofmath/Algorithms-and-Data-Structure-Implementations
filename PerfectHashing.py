import random
class UniversalHash:
    def __init__(self,U,n):
        self.p = 10**9 + 7
        self.a = random.randint(1,self.p-1)
        self.b = random.randint(0,self.p-1)
        self.n = n
        self.U = U
    def hash(self,key):
        return ((self.a*key + self.b)%self.p)%self.n
    
    
class HashTableL2:
    def __init__(self,U,n):
        self.n = max(n,1)
        self.keys = [None]*n
        self.values = [None]*n
        self.h2 = UniversalHash(100,n)

    def insert(self,key,value):
        i = self.h2.hash(key)
        if self.keys[i]!=None:
            return -1
        self.keys[i] = key
        self.values[i] = value

    def query(self,key):
        i = self.h2.hash(key)
        if self.keys[i] == key:
            return self.values[i]
        return -1

class HashTableL1:
    def __init__(self,U,n):
        self.n = n
        self.U = U
        self.keys = [[] for x in range(n)]
        self.values = [[] for x in range(n)]
        self.h1 = UniversalHash(U,n)
        self.Secondary = [HashTableL2(U,1) for x in range(self.n)]
        self.length = 0

    def insert(self,key,value):
        i = self.h1.hash(key)
        self.length = self.length - len(self.keys[i])**2 + (len(self.keys[i])+1)**2
        self.keys[i].append(key)
        self.values[i].append(value)
        if self.length > 4*self.n:
            self.redo()
        r = self.Secondary[i].insert(key,value)
        if r == -1:
            self.rehash(i)

    def query(self,key):
        i = self.h1.hash(key)
        return self.Secondary[i].query(key)

    def rehash(self,i):
        self.Secondary[i] = HashTableL2(self.U,max(1,len(self.keys[i])**2))
        for j in range(len(self.keys[i])):
            r = self.Secondary[i].insert(self.keys[i][j], self.values[i][j])
            if r == -1:
                self.rehash(i)
                break
        return

    def redo(self):
        print(self.length,'redo',self.keys)
        keys = [[] for x in range(self.n)]
        values = [[] for x in range(self.n)]
        self.h1 = UniversalHash(self.U,self.n)
        self.length = 0
        for j in range(self.n):
            for k in range(len(self.keys[j])):
                i = self.h1.hash(self.keys[j][k])
                self.length = self.length - len(self.keys[i])**2 + (len(self.keys[i])+1)**2
                keys[i].append(self.keys[j][k])
                values[i].append(self.values[j][k])
        self.Secondary = [HashTableL2(self.U,max(1,len(keys[x])**2)) for x in range(self.n)]
        
        self.keys = keys
        self.values = values
        
        for i in range(self.n):
            self.rehash(i)

        if self.length > 4*self.n:
            self.redo()
        return


D = HashTableL1(10**9,50000)
for i in range(40000):
    D.insert(i,random.randint(0,100000))
print(len(D.keys))
print(len(D.values))
print(D.query(2),D.length)

#PERFECTO!
#NIZRET! NIZRET!




















