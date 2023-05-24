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

bfs_search(v2, graph, '5')
