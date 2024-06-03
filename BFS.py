def (graph, node):

    v = []
    q = []
    v.append(node)
    q.append(node)

    while q:
        nodee = q.pop(0)
        print("poped node",nodee)

        for i in range v:
            print("node  in loop -->",i)
            if i not in v:
                print("node to be added",i)
                v.append(i)
                q.append(i)
    return v

    '''  
    graph = { 'A' : ['B','C'],
               'B': ['D','E'],
               'C': ['E'],
               'D': ['F']
               'E': [],
               'F': []
               }
    BFS(graph,'A')
    
    '''
