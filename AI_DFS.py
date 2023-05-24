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

dfs_search(v1, graph, '5')
print()
