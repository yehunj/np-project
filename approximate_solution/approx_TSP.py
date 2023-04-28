def approx_TSP():
    pass


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
    
    print (graph)
    pass

if __name__ == '__main__':
    main()