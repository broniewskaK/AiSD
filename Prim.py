V = [
    ['A', 'B', 1],
    ['A', 'E', 4],
    ['A', 'F', 8],
    ['B', 'A', 1],
    ['B', 'C', 2],
    ['B', 'F', 6],
    ['B', 'G', 6],
    ['C', 'B', 2],
    ['C', 'D', 3],
    ['C', 'G', 2],
    ['D', 'C', 3],
    ['D', 'G', 1],
    ['D', 'H', 4],
    ['H', 'D', 4],
    ['H', 'G', 1],
    ['G', 'H', 1],
    ['G', 'D', 1],
    ['G', 'C', 2],
    ['G', 'B', 6],
    ['G', 'F', 1],
    ['F', 'G', 1],
    ['F', 'B', 6],
    ['F', 'A', 8],
    ['F', 'E', 5],
    ['E', 'F', 5],
    ['E', 'A', 4]
]

def prim_algorithm(graph):
    minimum_spanning_tree = []
    visited = set()
    start_vertex = graph[0][0]

    visited.add(start_vertex)

    while len(visited) < len(set(v[0] for v in graph)):
        min_weight = float('inf')
        min_edge = None

        for edge in graph:
            vertex1, vertex2, weight = edge
            if (vertex1 in visited) ^ (vertex2 in visited) and weight < min_weight:
                min_weight = weight
                min_edge = edge
        if min_edge:
            minimum_spanning_tree.append(min_edge)
            visited.add(min_edge[0])
            visited.add(min_edge[1])

    return minimum_spanning_tree



minimum_spanning_tree = prim_algorithm(V)

print("Prim")
for edge in minimum_spanning_tree:
    print(edge)

