"""
Given a connected weighted graph (in weighted neighboring matrix), return the shortest path
"""


def dijkstra(weighted_matrix, start, end):

    def updateU(vertex, U):
        visited[vertex] = True
        for i in range(len(weighted_matrix[vertex])):
            if weighted_matrix[vertex][i] != _:
                if U[i] == _ or weighted_matrix[vertex][i] + U[vertex] < U[i]:
                    U[i] = weighted_matrix[vertex][i] + U[vertex]
                    path[i] = vertex
        return U

    num_vertices = len(weighted_matrix)

    # record the previous node in path
    path = [_] * num_vertices

    # record choosing all vertices
    visited = [False] * num_vertices

    # initialization of U
    U = [_] * num_vertices
    U[start] = 0

    current = start

    # Getting U
    while False in visited:
        updateU(current, U)
        print("-"*100)
        print("visited:", visited)
        print("path:", path)
        w_min = _
        v_min = None
        print("distance:", U)
        for i in range(len(weighted_matrix[current])):
            if weighted_matrix[current][i] < w_min and not visited[i]:
                w_min = weighted_matrix[current][i]
                v_min = i
        current = v_min
        print("chosen:", current)
        if not current:
            break

    # Reconstructing path using recursion
    shortest_path = []

    def rec_reconstruction(ind):
        shortest_path.append(path[ind])
        if ind == start:
            return None
        rec_reconstruction(path[ind])

    rec_reconstruction(end)
    shortest_path.reverse()
    shortest_path = shortest_path[1:] + [end]
    print("shortest path:", shortest_path)
    return U, shortest_path


_ = float('inf')
weighted_matrix = [
    # [_, 12, _, _, _, 16, 14],
    # [12, _, 10, _, _, 7, _],
    # [_, 10, _, 3, 5, 6, _],
    # [_, _, 3, _, 4, _, _],
    # [_, _, 5, 4, _, 2, 8],
    # [16, 7, 6, _, 2, _, 9],
    # [14, _, _, _, 8, 9, _]
    [_, 3, 7, 4, _, _, _],
    [3, _, 2, _, _, 7, _],
    [7, 2, _, 8, 1, _, _],
    [4, _, 8, _, _, _, 2],
    [_, _, 1, _, _, 7, _],
    [_, 7, _, _, 7, _, 1],
    [_, _, _, 2, _, 1, _]
]

start = 6
end = 0
dijkstra(weighted_matrix, start, end)