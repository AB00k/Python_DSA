# Graph Algorithms
# Minimum Spamming Tree algorithms
# Kuskal Algoritm
import disjointset as dst
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[]
        self.nodes=[]
        self.MST=[]

    def addegde(self,s,d,w):
        self.graph.append([s,d,w])
    def addnode(self,value):
        self.nodes.append(value)
    def printsolution(self,s,d,w):
        for s,d,w in self.MST:
            print('%s - %s: %s' % (s,d,w))

    def kruskalalo(self):
        i,e=0,0
        ds=dst.disjointset(self.nodes)
        self.graph=sorted(self.graph,key=lambda item: item[2])
        while e<self.V-1:
            s,d,w=self.graph[i]
            i+=1
            x=ds.find(s)
            y=ds.find(d)
            if x !=y:
                e+=1
                self.MST.append([s,d,w])
                ds.union(x,y)
        self.printsolution(s,d,w)
g=Graph(5)
g.addnode('a')
g.addnode('b')
g.addnode('c')
g.addnode('d')
g.addnode('e')
g.addegde('a','b',5)
g.addegde('a','c',13)
g.addegde('a','e',15)
g.addegde('b','a',5)
g.addegde('b','c',10)
g.addegde('b','d',8)
g.addegde('c','a',13)
g.addegde('c','b',10)
g.addegde('c','e',20)
g.addegde('c','d',6)
g.addegde('d','b',8)
g.addegde('d','c',6)
g.addegde('e','a',15)
g.addegde('e','c',20)

g.kruskalalo()
