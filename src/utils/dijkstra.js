
export const dijkstra = (weighted_matrix, start, end) => {
    function updateU(vertex, U) {
        visited[vertex] = true
        for (let i = 0; i < weighted_matrix[vertex].length; i++) {
            if (weighted_matrix[vertex][i] !== Infinity) {
                if (U[i] === Infinity || weighted_matrix[vertex][i] + U[vertex] < U[i]) {
                    U[i] = weighted_matrix[vertex][i] + U[vertex]
                    path[i] = vertex
                }
            }
        }
        return U
    }

    const num_vertices = weighted_matrix.length

    // record the previous node in path
    const path = Array(num_vertices).fill(Infinity)

    // record choosing all vertices
    const visited = Array(num_vertices).fill(false)

    // initialization of U
    const U = Array(num_vertices).fill(Infinity)
    U[start] = 0

    let current = start

    // Getting U
    while (visited.includes(false)) {
        updateU(current, U)
        console.log("-".repeat(100))
        console.log("visited:", visited)
        console.log("path:", path)
        let w_min = Infinity
        let v_min = null
        console.log("distance:", U)
        for (let i = 0; i < weighted_matrix[current].length; i++) {
            if (weighted_matrix[current][i] < w_min && !visited[i]) {
                w_min = weighted_matrix[current][i]
                v_min = i
            }
        }
        current = v_min
        console.log("chosen:", current)
        if (current === null) {
            break
        }
    }

    // Reconstructing path using recursion
    const shortest_path = []

    function rec_reconstruction(ind) {
        shortest_path.push(path[ind])
        if (ind === start) {
            return null
        }
        rec_reconstruction(path[ind])
    }

    rec_reconstruction(end)
    shortest_path.reverse()
    shortest_path.splice(0, 1)
    shortest_path.push(end)
    console.log("shortest path:", shortest_path)
    return [U, shortest_path]
}

function test() {
    const weighted_matrix = [
        [Infinity, 12, Infinity, Infinity, Infinity, 16, 14],
        [12, Infinity, 10, Infinity, Infinity, 7, Infinity],
        [Infinity, 10, Infinity, 3, 5, 6, Infinity],
        [Infinity, Infinity, 3, Infinity, 4, Infinity, Infinity],
        [Infinity, Infinity, 5, 4, Infinity, 2, 8],
        [16, 7, 6, Infinity, 2, Infinity, 9],
        [14, Infinity, Infinity, Infinity, 8, 9, Infinity]
    ]

    const start = 0
    const end = 6
    return dijkstra(weighted_matrix, start, end)
}