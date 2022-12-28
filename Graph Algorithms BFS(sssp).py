#Graph Algorithms
#single source shortest path algorithms
#BFS
class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict

    def addedge(self,vertex,edge):
        self.gdict[vertex].append(edge)

    def bfs(self,start,end):
        queue=[]
        queue.append([start])
        while queue:
            path=queue.pop(0)
            node=path[-1]
            if node==end:
                return path
            for adjacent in self.gdict.get(node,[]):
                newpath = list(path)
                newpath.append(adjacent)
                queue.append(newpath)

dict={'a':['b','c'],
      'b':['a','e','d'],
      'c':['a','e'],
      'd':['b','f'],
      'e':['b','c','f'],
      'f':['d','e']}

graph=Graph(dict)
print(graph.bfs('a','e'))