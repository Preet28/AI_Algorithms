# DFS algorithm
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'1': set(['2', '3']),
         '2': set(['4', '5']),
         '3': set(['5']),
         '4': set(['5','6']),
         '5': set(['6']),
         '6': set()}

dfs(graph, '1')