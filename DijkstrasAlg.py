class G:
    def __init__(self,V,E,w):
        self.V = V
        self.E = E
        self.w = w
        self.Adj = {}
        self.prepare_adjecency_list()
    def prepare_adjecency_list(self):
        for e in self.E:
            u,v = e
            if u not in self.Adj:
                self.Adj[u] = []
            self.Adj[u].append(v)
        
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

def Extract_Min(Queue):
    minimum = 1000000
    min_element = None
    for v in Queue:
        if v.d <= minimum:
            minimum = v.d
            min_element = v
    Queue.remove(min_element)
    
    return min_element

def Dijkstra(G,s):
    InitializeSS(G,s)
    S = set()
    Q = [] + G.V
    while len(Q)>0:
        u = Extract_Min(Q)
        S.add(u)
        for v in G.Adj[u]:
            Relax(u,v,G.w)

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
E = [('s','t'),('s','y'),('t','x'),('t','y'),('y','t'),('y','x'),('y','z'),('z','x'),('x','z'),('z','s')]
w = [10,5,1,2,3,9,2,6,4,7]


G = G(make_V(d,V),make_E(d,E),make_w(E,w))

Dijkstra(G,G.V[0])

print(G.V[0].d,G.V[1].d,G.V[2].d,G.V[3].d,G.V[4].d)
    
