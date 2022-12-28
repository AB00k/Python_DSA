# Graph Algorithms
# Minimum Spamming Tree algorithms
# Disjont Set
class disjointset:
    def __init__(self,vertices):
        self.vertices=vertices
        self.parent={}
        for v in vertices:
            self.parent[v]=v
        self.rank=dict.fromkeys(vertices,0)
    def find(self,item):
        if self.parent[item]==item:
             return item
        else:
            res = self.find(self.parent[item])
            self.parent[item] = res
            return res
    def union(self,x,y):
        xroot=self.find(x)
        yroot=self.find(y)
        if self.rank[xroot]<self.rank[yroot]:
            self.parent[xroot]=yroot
        elif self.rank[xroot]>self.rank[yroot]:
            self.parent[yroot]=xroot
        else:
            self.parent[yroot]=xroot
            self.rank[xroot]+=1
vertices=['a','b','c','d','e','f']
disjoin=disjointset(vertices)
disjoin.union('a','c')
print(disjoin.find('c'))

