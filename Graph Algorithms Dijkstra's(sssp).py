#Graph Algorithms
#single source shortest path algorithms
#Dijkstras Algorithm
from collections import defaultdict
class Graph:
    def __init__(self):
        self.nodes=set()
        self.edges=defaultdict(list)
        self.distances={}
    def addnodes(self,value):
        self.nodes.add(value)
    def addedge(self,fromnode,tonode,distances):
        self.edges[fromnode].append(tonode)
        self.distances[(fromnode,tonode)]=distances
    def printsolution(self,dict):
        print('vertex distance from source')
        for key , value in dict.items():
            print('  '+str(key),' :  '+str(value))
def Dijkstras(graph,initial):
    visited={initial:0}
    Path=defaultdict(list)
    nodes=set(graph.nodes)
    while nodes:
        minnode=None
        for node in nodes:
            if node in visited:
                if minnode is None:
                    minnode=node
                elif visited[node]<visited[minnode]:
                    minnode=node
        if minnode is None:
            break
        nodes.remove(minnode)
        currentweight=visited[minnode]
        for edge in graph.edges[minnode]:
            weight=currentweight+graph.distances[(minnode,edge)]
            if edge not in visited or weight<visited[edge]:
                visited[edge]=weight
                Path[edge].append(minnode)
    return graph.printsolution(visited),Path
customgraph=Graph()
customgraph.addnodes('a')
customgraph.addnodes('b')
customgraph.addnodes('c')
customgraph.addnodes('d')
customgraph.addnodes('e')
customgraph.addnodes('f')
customgraph.addnodes('g')
customgraph.addedge('a','b',2)
customgraph.addedge('a','c',5)
customgraph.addedge('b','c',6)
customgraph.addedge('b','d',1)
customgraph.addedge('b','e',3)
customgraph.addedge('c','f',8)
customgraph.addedge('d','e',4)
customgraph.addedge('e','g',9)
customgraph.addedge('f','g',7)

print(Dijkstras(customgraph,'a'))
