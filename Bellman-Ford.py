class G:
    def __init__(self,V,E,w):
        self.V = V
        self.E = E
        self.w = w
        
class vertex:
    def __init__(self,name):
        self.name = name
        self.d = None
        self.parent = None

def InitializeSS(G,s):
    for v in G.V:
        v.d = 1000000
        v.parent = None
    s.d = 0

def Relax(u,v,w):
    if v.d > u.d + w[(u,v)]:
        v.d = u.d + w[(u,v)]
        v.parent = u

def Bellman_Ford(G,s):
    InitializeSS(G,s)
    for i in range(1,len(G.V)):
        for e in G.E:
            Relax(e[0],e[1],G.w)
    for e in G.E:
        u,v = e
        if v.d > u.d + G.w[e]:
            return False
    return True


def make_V(d,V):
    Vertices = []
    for v in V:
        Vertices.append(d[v])
    return Vertices

def make_E(d,E):
    Edges = []
    for e in E:
        u,v = e
        Edges.append((d[u],d[v]))
    return Edges

def make_w(E,w):
    weight_function = {}
    for i in range(len(E)):
        u,v = E[i]
        weight_function[(d[u],d[v])] = w[i]
    return weight_function

d = {
    's' : vertex('s'),
    't' : vertex('t'),
    'y' : vertex('y'),
    'x' : vertex('x'),
    'z' : vertex('z')
    }

V = ['s','t','x','y','z']
E = [('s','t'),('t','x'),('x','t'),('t','y'),('s','y'),('y','x'),('y','z'),('z','x'),('t','z'),('z','s')]
w = [6,5,-2,8,7,-3,9,7,-4,2]


G = G(make_V(d,V),make_E(d,E),make_w(E,w))

Bellman_Ford(G,G.V[0])

print(G.V[0].d,G.V[1].d,G.V[2].d,G.V[3].d,G.V[4].d)


    
