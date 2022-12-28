# Graph Algorithms
# Minimum Spamming Tree algorithms
# Prim's Algoritm
import sys
class Graph:
    def __init__(self,vertexnum,edges,nodes):
        self.edges=edges
        self.nodes=nodes
        self.vertexnum=vertexnum
        self.MST=[]
    def printsolution(self):
        print('Edge : Weight')
        for s,d,w in self.MST:
            print('%s - %s: %s' % (s,d,w))
    def primsalgo(self):
        visited=[0]*self.vertexnum
        edgenum=0
        visited[0]=True
        while edgenum<self.vertexnum-1:
            min=sys.maxsize
            for i in range(self.vertexnum):
                if visited[i]:
                    for j in range(self.vertexnum):
                        if ((not visited[j]) and self.edges[i][j] ):
                            if min > self.edges[i][j]:
                                s=i
                                d=j
            self.MST.append([self.nodes[s],self.nodes[d],self.edges[s][d]])
            visited[d]=True
            edgenum+=1
        self.printsolution()
edges=[[0,10,20,0,0],
       [10,0,30,5,0],
       [20,30,0,15,6],
       [0,5,15,0,8],
       [0,0,6,8,0]]
nodes=['a','b','c','d','e']
g=Graph(5,edges,nodes)
g.primsalgo()