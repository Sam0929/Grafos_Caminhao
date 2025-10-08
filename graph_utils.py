# graph_utils.py

import networkx as nx
import numpy as np
import random
import math
from config import * 

def create_fixed_graph():
    G = nx.Graph()
    G.add_nodes_from(FIXED_NODES)
    G.add_weighted_edges_from(FIXED_EDGES_WITH_WEIGHTS, weight='weight')
    return G

def create_random_graph(n_nodes, p_factor, seed):
    p = p_factor + (np.log(n_nodes) / n_nodes if n_nodes > 0 else 0)
    G = nx.gnp_random_graph(n_nodes, p, seed=seed)
    for u, v in G.edges():
        G[u][v]['weight'] = random.randint(1, 10)
    return G

def get_minimum_edge_weight_in_path(G, path):
    weights = []
    for i in range(len(path) - 1):
        u = path[i]
        v = path[i+1]
        weights.append(G[u][v]['weight'])
    return min(weights) if weights else 0

def analyze_paths(G, paths_to_take):
    max_spanning_tree = nx.maximum_spanning_tree(G, weight='weight', algorithm='kruskal')
    results = {}
    for source, target in paths_to_take:
        try:
            path = nx.shortest_path(max_spanning_tree, source=source, target=target)
            min_weight = get_minimum_edge_weight_in_path(max_spanning_tree, path)
            results[(source, target)] = min_weight                                    #key = (origem e destino), value = peso_minimo
        except nx.NetworkXNoPath:
            results[(source, target)] = "Sem caminho na árvore"
    return results, max_spanning_tree


def giant_fraction(c, tolerance=1e-9): # S me diz qual a probabilidade de um vertice estar em um componente gigante, 
                                       #(componente gigante é um componente de um grafo aleatório que contém uma fração significativa dos vértices.)
    if c <= 1:
        return 0.0
    
    s = 0.5
    
    while True:
        next_s = 1 - math.exp(-c * s)
      
        if abs(next_s - s) < tolerance:
            break
        
        s = next_s
        
    return s

def calculate_gnp_statistics(max_nodes, p_base):

    p_10 = p_base * 0.10
    n_values = list(range(1, max_nodes + 1))
    s_values = []
    degree_values = []
    degree_values_10 = []
    expected_edges_values = [] 
    expected_edges_values_10 = []

    for n in n_values:
        c = p_10 * (n - 1)
        s = giant_fraction(c)
        s_values.append(s)
        
        # Cálculo para os graus médios
        medium_degree = (n - 1) * p_base
        medium_degree_10 = (n - 1) * p_10
        degree_values.append(medium_degree)
        degree_values_10.append(medium_degree_10)

        # Cálculo do número esperado de arestas em um grafo G(n, p)
        expected_edges = (n * (n - 1) / 2) * p_base
        expected_edges_values.append(expected_edges)

        expected_edges_10 = (n * (n - 1) / 2) * p_10
        expected_edges_values_10.append(expected_edges_10)

        

    # Dicionário com todos os dados calculados
    return {
        "n_values": n_values,
        "s_values": s_values,
        "degree_values": degree_values,
        "degree_values_10": degree_values_10,
        "expected_edges_values": expected_edges_values,
        "expected_edges_values_10": expected_edges_values_10, 
        "p_base": p_base,
        "p_10": p_10
    }