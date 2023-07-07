
def find(parent, vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent, parent[vertex])
    return parent[vertex]
def union(parent, rank, vertex1, vertex2):
    root1 = find(parent, vertex1)
    root2 = find(parent, vertex2)
    if rank[root1] < rank[root2]:
        parent[root1] = root2
    elif rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root2] = root1
        rank[root1] += 1
def kruskal_algorithm(vertices):
    parent = {v[0]: v[0] for v in vertices}
    rank = {v[0]: 0 for v in vertices}
    minimum_spanning_tree = []
    sorted_edges = sorted(vertices, key=lambda x: x[2])

    for edge in sorted_edges:
        vertex1, vertex2, weight = edge
        root1 = find(parent, vertex1)
        root2 = find(parent, vertex2)

        if root1 != root2:
            minimum_spanning_tree.append(edge)
            union(parent, rank, root1, root2)

    return minimum_spanning_tree



vertices = [
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
minimum_spanning_tree = kruskal_algorithm(vertices)
for edge in minimum_spanning_tree:
    print(edge)
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


