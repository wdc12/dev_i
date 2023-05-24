def aStarAlgo(start_node, stop_node):
         
    open_set = set(start_node) 
    closed_set = set()
    g = {}
    parents = {}

    g[start_node] = 0
    parents[start_node] = start_node
    
    while len(open_set) > 0:
        n = None

        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
            
                    
        if n == stop_node or Graph_nodes[n] == None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        if n == None:
            print('Path does not exist!')
            return None

        if n == stop_node:
            path = []

            while parents[n] != n:
                path.append(n)
                n = parents[n]

            path.append(start_node)

            path.reverse()

            print('Path found: {}'.format(path))
            return path

        open_set.remove(n)
        closed_set.add(n)

    print('Path does not exist!')
    return None

def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

def heuristic(n):
        H_dist = {
            'A': 11,
            'B': 6,
            'C': 99,
            'D': 1,
            'E': 7,
            'G': 0,
             
        }
 
        return H_dist[n]

Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1),('G', 9)],
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)],
     
}
aStarAlgo('A', 'G')

'''
A* Algorithm is the advanced form of the BFS algorithm (Breadth-first search), which searches for
the shorter path first than, the longer paths. It is a complete as well as an optimal solution for
solving path and grid problems.

The key feature of the A* algorithm is that it keeps a track of each visited node which helps in
ignoring the nodes that are already visited, saving a huge amount of time. It also has a list that holds
all the nodes that are left to be explored and it chooses the most optimal node from this list, thus
saving time not exploring unnecessary or less optimal nodes.
So we use two lists namely ‘open list‘ and ‘closed list‘ the open list contains all the nodes that are
being generated and are not existing in the closed list and each node explored after its neighboring
nodes are discovered is put in the closed list and the neighbors are put in the open list this is how the
nodes expand. Each node has a pointer to its parent so that at any given point it can retrace the path
to the parent. Initially, the open list holds the start(Initial) node. The next node chosen from the open
list is based on its f score (f(n)), the node with the least f-score is picked up and explored.

f(n) = g(n) + h(n)

Heuristic used in A*
Where
g (n) : The actual cost path from the start node to the current node.
h (n) : The actual cost path from the current node to goal node.
f (n) : The actual cost path from the start node to the goal node.

Performance Measure:
Optimal – find the least cost from the starting point to the ending point.
Complete – It means that it will find all the available paths from start to end.
'''
