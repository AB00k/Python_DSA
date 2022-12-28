#Lesson no: 30
#Graphs

class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict

    def addedge(self,vertex,edge):
        self.gdict[vertex].append(edge)

    def bfs(self,vertex):
        visited=[vertex]
        queue=[vertex]
        while queue:
            dvertex=queue.pop(0)
            print(dvertex)
            for adjacentvertex in self.gdict[dvertex]:
                if adjacentvertex not in visited:
                    visited.append(adjacentvertex)
                    queue.append(adjacentvertex)
    def dfs(self,vertex):
        visited=[vertex]
        stack=[vertex]
        while stack:
            dvertex=stack.pop()
            print(dvertex)
            for adjacentvertex in self.gdict[dvertex]:
                if adjacentvertex not in visited:
                    visited.append(adjacentvertex)
                    stack.append(adjacentvertex)

dict={'a':['b','c'],
      'b':['a','e','d'],
      'c':['a','e'],
      'd':['b','f'],
      'e':['b','c','f'],
      'f':['d','e']}

graph=Graph(dict)
graph.dfs('a')