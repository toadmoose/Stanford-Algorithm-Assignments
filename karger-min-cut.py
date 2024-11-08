import random
from collections import defaultdict
import math

def read_graph(filename):
    graph = defaultdict(list)
    with open(filename, 'r') as f:
        for line in f:
            vertices = list(map(int, line.strip().split()))
            vertex = vertices[0]
            edges = vertices[1:]
            graph[vertex] = edges
    return graph

def contract(graph, u, v):
    # Combine the edge lists of u and v
    graph[u].extend(graph[v])
    
    # Remove self-loops
    graph[u] = [x for x in graph[u] if x != u and x != v]
    
    # Update all other vertices that had edges to v
    for key in graph:
        graph[key] = [u if x == v else x for x in graph[key]]
    
    # Remove v from the graph
    del graph[v]

def karger_min_cut(graph):
    while len(graph) > 2:
        u = random.choice(list(graph.keys()))
        v = random.choice(graph[u])
        contract(graph, u, v)
    
    return len(graph[list(graph.keys())[0]])

def find_min_cut(graph, iterations):
    min_cut = float('inf')
    for i in range(iterations):
        graph_copy = {k: v[:] for k, v in graph.items()}  # Create a deep copy
        current_cut = karger_min_cut(graph_copy)
        if current_cut < min_cut:
            min_cut = current_cut
        if (i + 1) % 100 == 0:
            print(f"Iteration {i+1}/{iterations}, Current min cut: {min_cut}")
    return min_cut

# Main execution
filename = 'kargerMinCut.txt'
graph = read_graph(filename)

print(f"Graph loaded with {len(graph)} vertices")

n = len(graph)
iterations = int(n * n * math.log(n))  # Number of iterations based on probability analysis
min_cut = find_min_cut(graph, iterations)

print(f"The minimum cut found is: {min_cut}")
