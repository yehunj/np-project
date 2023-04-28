import math

def nearest_neighbor_tsp(graph):
    start_vertex = list(graph.keys())[0]
    current_vertex = start_vertex
    unvisited_vertices = set(graph.keys())
    unvisited_vertices.remove(start_vertex)
    path = [start_vertex]
    while unvisited_vertices:
        nearest_neighbor = min(unvisited_vertices, key=lambda vertex: graph[current_vertex][vertex])
        path.append(nearest_neighbor)
        unvisited_vertices.remove(nearest_neighbor)
        current_vertex = nearest_neighbor
    path.append(start_vertex)
    total_distance = sum([graph[path[i]][path[i+1]] for i in range(len(path)-1)])
    return path, total_distance


def main():
    n, m = map(int, input().split())

    correct_number_of_edges = n * (n - 1) // 2
    if m != correct_number_of_edges:
        raise ValueError('Invalid number of edges. Graph will not be complete.')

    graph = {}

    for i in range(m):
        u, v, w = input().split()
        if u not in graph:
            graph[u] = {}
        if v not in graph:
            graph[v] = {}
        graph[u][v] = float(w)
        graph[v][u] = float(w)
    
    path, total_distance = nearest_neighbor_tsp(graph)
    total_distance = int(total_distance)
    print(total_distance)
    print(' '.join(path))
    pass

if __name__ == '__main__':
    main()