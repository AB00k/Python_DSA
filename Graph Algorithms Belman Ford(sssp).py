#Graph Algorithms
#single source shortest path algorithms
#Bellman Ford Algorithm

class Graph:

    def __init__(self,vertices):
        self.V=vertices
        self.graph=[]
        self.nodes=[]
    def addedge(self,s,d,w):
        self.graph.append([s,d,w])
    def addnode(self,value):
        self.nodes.append(value)
    def printsolution(self,dict):
        print('vertex distance from source')
        for key , value in dict.items():
            print('  '+str(key),' :  '+str(value))

    def bellmanford(self,source):

        dist={i : float('Inf') for i in self.nodes}
        dist[source]=0

        for _ in range(self.V-1):
            for s,d,w in self.graph:
                if dist[source]!= float('Inf') and dist[s]+w <dist[d]:
                    dist[d]=dist[s]+w
        for s, d, w in self.graph:
            if dist[source] != float('Inf') and dist[s] + w < dist[d]:
                print('Graph contains negative cycle')
                return

        return self.printsolution(dist)


g=Graph(5)
g.addnode('a')
g.addnode('b')
g.addnode('c')
g.addnode('d')
g.addnode('e')
g.addedge('a','c',6)
g.addedge('a','d',6)
g.addedge('b','a',3)
g.addedge('c','d',1)
g.addedge('d','c',2)
g.addedge('d','b',1)
g.addedge('e','b',4)
g.addedge('e','d',2)
g.bellmanford('e')

