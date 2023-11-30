"""
Given a connected indirected graph in weighted Adjacency matrix, source node, and terminal node
will return the shortest path and the distance
"""


def dijkstra(adj_matrix, start, end):
    num_vertices = len(adj_matrix)
    distances = [float('inf')] * num_vertices
    distances[start] = 0
    path = [-1] * num_vertices
    visited = [False] * num_vertices

    def updateU():
        # Update distances of adjacent vertices
        for neighbor, weight in enumerate(adj_matrix[current_vertex]):
            if weight != _ and not visited[neighbor]:
                distance = min_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    path[neighbor] = current_vertex
        print("distances:", distances)

    for i in range(num_vertices):
        print('-'*100)
        # Find the vertex with the minimum distance to the source point
        min_distance = float('inf')
        for v in range(num_vertices):
            if not visited[v] and distances[v] < min_distance:
                min_distance = distances[v]
                current_vertex = v
        print("current vertex:", current_vertex)
        visited[current_vertex] = True
        updateU()

    # Reconstruct the path and calculate total distance
    total_distance = distances[end]
    shortest_path = []
    while end != -1:
        shortest_path.append(end)
        end = path[end]
    shortest_path.reverse()
    print("shortest path:", shortest_path)
    print("shortest distance:", total_distance)

    return shortest_path, total_distance


_ = float('inf')
weighted_matrix1 = [
    [_, 12, _, _, _, 16, 14],
    [12, _, 10, _, _, 7, _],
    [_, 10, _, 3, 5, 6, _],
    [_, _, 3, _, 4, _, _],
    [_, _, 5, 4, _, 2, 8],
    [16, 7, 6, _, 2, _, 9],
    [14, _, _, _, 8, 9, _]
]

weighted_matrix2 = [
    [_, 3, 7, 4, _, _, _],
    [3, _, 2, _, _, 7, _],
    [7, 2, _, 8, 1, _, _],
    [4, _, 8, _, _, _, 2],
    [_, _, 1, _, _, 7, _],
    [_, 7, _, _, 7, _, 1],
    [_, _, _, 2, _, 1, _]
]

weighted_matrix3 = [
    [_, 4, 2, 4, _, _, _],
    [4, _, 2, _, _, 1, _],
    [2, 2, _, 5, 1, _, _],
    [4, _, 5, _, _, _, 2],
    [_, _, 5, _, _, _, _],
    [_, 1, _, _, _, _, 2],
    [_, _, _, 2, _, 2, _]
]

start = 0
end = 6
dijkstra(weighted_matrix1, start, end)