def tsp(graph, v, n, currPos, count, cost, ans):


def main():
    n, m = map(int, input().split())
    graph = {}

    for i in range(m):
        u, v, w = input().split()

        # add edge to graph
        if u not in graph:
            graph[u] = {}
        if v not in graph:
            graph[v] = {}
        graph[u][v] = float(w)
        graph[v][u] = float(w)

    min_path = float('inf')
    v = {}
    v[0] = True





if __name__ == '__main__':
    main()