#lesson no: 32
# topological sort algorithm
from collections import defaultdict
class graph:
    def __init__(self,noofvertices):
        self.graph=defaultdict(list)
        self.noofvertices=noofvertices
    def addedge(self,vertex,edge=None):
        self.graph[vertex].append(edge)

    def topologicalsortuti(self,v,visited,stack):
        visited.append(v)
        for i in self.graph[v]:
            if i not in visited:
                self.topologicalsortuti(i,visited,stack)
        stack.insert(0,v)
    def topologicalsort(self,vertex):
        visited=[]
        stack=[]
        for k in list(self.graph):
            if k not in visited:
                self.topologicalsortuti(k,visited,stack)
        print(stack)


customgraph=graph(8)
customgraph.addedge('a','c')
customgraph.addedge('c','e')
customgraph.addedge('e','h')
customgraph.addedge('e','f')
customgraph.addedge('f','g')
customgraph.addedge('d','f')
customgraph.addedge('b','d')
customgraph.addedge('b','c')

customgraph.topologicalsort('a')