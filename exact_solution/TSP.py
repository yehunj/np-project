def tsp(graph):
    vertices = list(graph.keys())
    permutations = get_permutations(vertices)

    shortest_cycle = None
    shortest_length = float('inf')
    for cycle in permutations:
        cycle_length = get_cycle_length(graph, cycle)
        if cycle_length < shortest_length:
            shortest_length = cycle_length
            shortest_cycle = cycle

    shortest_cycle.append(shortest_cycle[0])

    return shortest_length, shortest_cycle


def get_permutations(vertices):
    if len(vertices) == 1:
        return [vertices]
    permutations = []
    for i in range(len(vertices)):
        sub_permutations = get_permutations(vertices[:i] + vertices[i+1:])
        for sub_permutation in sub_permutations:
            permutations.append([vertices[i]] + sub_permutation)
    return permutations


def get_cycle_length(graph, cycle):
    length = 0
    for i in range(len(cycle)):
        length += graph[cycle[i]][cycle[(i+1)%len(cycle)]]
    return length


def main():
    n, m = map(int, input().split())
    graph = {}

    for i in range(m):
        u, v, w = input().split()
        if u not in graph:
            graph[u] = {}
        if v not in graph:
            graph[v] = {}
        graph[u][v] = float(w)
        graph[v][u] = float(w)

    cycle_length, cycle = tsp(graph)
    cycle_length = int(cycle_length)
    print(cycle_length)
    print(' '.join(cycle))


if __name__ == '__main__':
    main()