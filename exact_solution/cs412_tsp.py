"""
    Our implemantation of the approximate solution to the TSP problem using the nearest neighbor algorithm.
    Sources used: http://people.hsc.edu/faculty-staff/robbk/Math111/Lectures/Fall%202017/Lecture%2031%20-%20The%20Nearest-Neighbor%20Algorithm.pdf
    Authors: Josh Kuesters and Ye Hun Joo
"""

import itertools
import time

def tsp(graph):
    # Get all permutations of the vertices.
    vertices = list(graph.keys())
    permutations = itertools.permutations(vertices)

    shortest_cycle = None
    shortest_length = float('inf')
    # For each permutation, get the cycle length and compare it to the shortest cycle length.
    for cycle in permutations:
        cycle_length = get_cycle_length(graph, cycle)
        # If the cycle length is shorter than the shortest cycle length, update the shortest cycle length and cycle.
        if cycle_length < shortest_length:
            shortest_length = cycle_length
            shortest_cycle = cycle

    # Add the first vertex to the end of the cycle to complete the cycle.
    shortest_cycle += shortest_cycle[:1]
    return shortest_length, shortest_cycle


def get_cycle_length(graph, cycle):
    length = 0
    for i in range(len(cycle)):
        # Add the distance between the current vertex and the next vertex in the cycle.
        length += graph[cycle[i]][cycle[(i+1)%len(cycle)]]
    return length


def main():
    start_time = time.time()
    n, m = map(int, input().split())

    correct_number_of_edges = n * (n - 1) // 2
    if m != correct_number_of_edges:
        raise ValueError('Invalid number of edges. Graph is not complete.')
    
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
    print('Time: ', time.time() - start_time)


if __name__ == '__main__':
    main()