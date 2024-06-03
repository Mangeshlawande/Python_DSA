def DFS(visited=[],graph,node):
    print("node->",node)
    if node node not in visited:
        print("node added ->", node)
        visited.append(node)

        for i in graph[node]:
            print("node in loop-> ", i)
            DFS(visited,graph, i)
        return visited

""" 
graph1= {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['E'],
    'D': ['F'],
    'E': [],
    'F': []      
}

"""
