graph = {
    'CS': {'MD': 55, 'JA': 255, 'HU': 100},
    'MD': {'TL': 389},
    'HU': {'JA': 125, 'LF': 689},
    'JA': {'AL': 130, 'MG': 168},
    'TL': {'AL': 155, 'CL': 255},
    'AL': {'CL': 320, 'MG': 89},
    'MG': {'CL': 166, 'WL': 90},
    'LF': {'MG': 213, 'MB': 489},
    'CL': {'WL': 175},
    'MB': {'WL': 164},
    'WL': {}
}

def dijkstra(graph, start, goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)

    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0, start)
    if shortest_distance[goal] != infinity:
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('And the path is ' + str(path))

dijkstra(graph, 'CS', 'WL')

