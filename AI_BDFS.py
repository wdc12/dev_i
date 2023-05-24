graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

v1 = set()

def dfs_search(v1, graph, curr):
    if curr not in v1:
        print(curr, end = ' ')
        v1.add(curr)

        for i in graph[curr]:
            dfs_search(v1, graph, i)
            
            
print("DFS:", end=" ")
dfs_search(v1, graph, '5')
print()


v2 = []
q = []

def bfs_search(v2, graph, curr):
    v2.append(curr)
    q.append(curr)

    while len(q) > 0:
        temp = q.pop(0)
        print(temp, end = ' ')

        for i in graph[temp]:
            if i not in v2:
                v2.append(i)
                q.append(i)

print("BFS:", end=" ")
bfs_search(v2, graph, '5')

"""
Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures.
The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of
a graph) and explores as far as possible along each branch before backtracking.

Time complexity: Equivalent to the number of nodes traversed in DFS.
T(n) = 1 + n^2 + n^3+ n^4+ .....+n^d = O(n^d)

Space complexity: Equivalent to how large can the fringe get.
S(n) = O(n*d)

Completeness: DFS is complete if the search tree is finite, meaning for a given finite search tree,
DFS will come up with a solution if it exists.

Optimality: DFS is not optimal, meaning the number of steps in reaching the solution, or the cost
spent in reaching it is high.
"""

"""
Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data
structures. It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a
‘search key’), and explores all of the neighbour nodes at the present depth prior to moving on to
the nodes at the next depth level.

Time complexity: Equivalent to the number of nodes traversed in BFS until the shallowest
solution.
T(n) = 1 + n^2 + n^3+ n^4+ .....+n^d = O(n^d)

Space complexity: Equivalent to how large can the fringe get.
S(n) = O(n^d)

Completeness: BFS is complete, meaning for a given search tree, BFS will come up with a
solution if it exists.
"""
