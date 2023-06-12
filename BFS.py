import collections

def bfs(graph, root):
    visited, queue = set(), collections.deque([(root, 0)])  # Store (vertex, distance) pairs
    visited.add(root)
    
    while queue:
        vertex, distance = queue.popleft()
        print(f"Node: {vertex}, Distance: {distance}")

        if vertex == max(graph.keys()):  # Check if the last node is reached   //dict = {key : value_pair}
            print(f"Minimum path distance from node 0 to last node: {distance}")
            break

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, distance + 1))  # Update distance

if __name__ == '__main__':
    graph = {
        0: [1, 2],
        1: [2],
        2: [3, 4],
        3: [1, 2],
        4: [5],
        5: []
    }
    print("Following is Breadth First Traversal:")
    bfs(graph, 0)
