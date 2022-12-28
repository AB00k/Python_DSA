# Graph Algorithms
# all pairs  shortest path algorithms
# Floyd Warshall Algorithm

inf = 9999
def printsol(nv, distance):
    for i in range(nv):
        for j in range(nv):
            if distance[i][j] == inf:
                print('Inf', end=' ')
            else:
                print(distance[i][j], end=' ')
        print('')

def floydwarshall(nv, Graph):
    distance = Graph
    for k in range(nv):
        for i in range(nv):
            for j in range(nv):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    printsol(nv, distance)


g = [[0, 8, inf, 1],
     [inf, 0, 1, inf],
     [4, inf, 0, inf],
     [inf, 2, 9, 1]
     ]
floydwarshall(4, g)
