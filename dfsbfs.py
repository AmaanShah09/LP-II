def bfs(graph, root):
    visited = set()
    queue = [root]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            queue.extend(graph[vertex])
    print()  # Add a new line after BFS traversal
# Driver Code
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['6'],
    '8': [],
    '6': []
}
print("The Output of BFS is: ")
bfs(graph, '5')  # function calling
visited = set()  # List for visited nodes.
def dfs(visited, graph, root):
    if root not in visited:
        print(root, end=' ')
        visited.add(root)
        for neighbour in graph[root]:
            dfs(visited, graph, neighbour)

print("The Output of DFS is: ")
dfs(visited, graph, '5')
