'''A basic set of functions for dealing with python graphs represented by a dictionary of nodes to adjacency lists.
For example graph = {'a': ['b'], 'b': ['a', 'c'], 'c': ['c']}
'''

import itertools

def permute_vertices(graph):
    return itertools.permutations(graph.keys())

def graph_import():
    vertices = list(sorted(input('Enter vertices: ')))
    graph = {}
    for i in vertices:
        connections = list(sorted(input('Enter connections to ' + i + ': ')))
        graph[i] = connections
    return graph

def is_edge(graph, a, b):
    return b in graph[a]

def is_valid_path(graph, path):
    for i in range(len(path) - 1):
        if not is_edge(graph, path[i], path[i + 1]):
            return False
    return True

def is_valid_cycle(graph, cycle):
    return is_edge(graph, cycle[-1], cycle[0]) and is_valid_path(graph, cycle)

def hamiltonian_cycles(graph):
    result = []
    for p in permute_vertices(graph):
        if is_valid_cycle(graph, p):
            result.append(p)
    return result

def dfs(graph, marked, vertex, processingFx):
    processingFx(vertex)
    marked[vertex] = True

    for adjVert in graph[vertex]:
        if not marked[adjVert]:
            dfs(graph, marked, adjVert, processingFx)

def DFS(graph, processingFx = print):
    marked = {}

    for key in graph:
        marked[key] = False

    for key in graph:
        if not marked[key]:
            dfs(graph, marked, key, processingFx)
            