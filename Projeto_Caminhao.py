import networkx as nx
import matplotlib.pyplot as plt
import math
import numpy as np
import random
import scipy as sp


I = 4  ## -> Numero de ilhas, nos
P = 5  ## -> Numero de pontes, arestas
S = 4  ## -> Numero de entregas, pesos maximos que deverao ser encontrados entre dois nos 

NODES_IN_RANGE = list(range(1, I + 1))

EDGES_WITH_WEIGHTS = [(4,5,4), 
                      (1,2,9), 
                      (1,3,0), 
                      (2,3,8), 
                      (2,4,7), 
                      (3,4,4)]

PATHS_TO_TAKE = [(1,4),
                 (2,1),
                 (3,1),
                 (4,3)]


G = nx.Graph()

# ADICIONANDO OS NOS
G.add_nodes_from(NODES_IN_RANGE)

# ADICIONANDO ARESTAS COM PESOS
G.add_weighted_edges_from(EDGES_WITH_WEIGHTS, weight = 'weight')


#GRAFO ALEATORIO
N = 20
P = 0.02 + (np.log(N) / N)

G_teste = nx.fast_gnp_random_graph(N, P, seed = 60)

for u, v in G_teste.edges():
    G_teste[u][v]['weight'] = random.randint(1, 10)

paths_to_take_random = [tuple(random.sample(range(1, 20), 2)) for node in range(N)]

# G = G_teste

# PATHS_TO_TAKE = paths_to_take_random


def draw_graph(G, ax=None, node_color='lightblue', edge_color='b'):
    # Cria o layout
    pos = nx.spring_layout(G, seed=10, method='energy')

    # Se não passar eixo, pega o atual
    if ax is None:
        ax = plt.gca()
    # Nós
    nx.draw_networkx_nodes(G, pos, node_size=400, node_color=node_color, ax=ax)
    # Arestas
    nx.draw_networkx_edges(G, pos, width=3, alpha=0.5, edge_color=edge_color, ax=ax)
    # Labels dos nós
    nx.draw_networkx_labels(G, pos, font_size=15, font_family="sans-serif", ax=ax)
    # Labels das arestas
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)


def how_much_weight(G, path):
    #RETORNA UMA LISTA COM OS PESOS DE UM PATH
    peso_total = []
    for i in range(len(path) - 1):  
        u = path[i]
        v = path[i + 1]
        peso_total.append(G[u][v]['weight']) 
    return peso_total

def minimum_weight_path(G, path):
  
    weights = []
    for i in range(len(path) - 1):
        u = path[i]
        v = path[i+1]
        weights.append(G[u][v]['weight'])
    return min(weights)

def generate_max_tree(G):
    G_max = nx.maximum_spanning_tree(G, weight='weight', algorithm='kruskal', ignore_nan=False)
    return G_max

def min_path_between_nodes(G, path):
    min_path = []
    for source_node, target_node in path:
        aux = nx.shortest_path(G, source=source_node, target=target_node)
        min_path.append(aux)
    return min_path



G_maximum_tree = generate_max_tree(G)

shortest_path_list = min_path_between_nodes(G_maximum_tree, PATHS_TO_TAKE)

greater_weight_path = [minimum_weight_path(G_maximum_tree, path) for path in shortest_path_list]


print('\nMaior peso para ir de A até B\n')

for i, path in enumerate(PATHS_TO_TAKE):

    print(f'A:{path[0]}, B:{path[1]} Maior peso: {greater_weight_path[i]}\n')

#DESENHANDO O GRAFO
fig, axes = plt.subplots(1, 2, figsize=(12,6))

# Grafo original
draw_graph(G, ax=axes[0], node_color='lightblue', edge_color='gray')
axes[0].set_title("Grafo Original")

# Árvore geradora
draw_graph(G_maximum_tree, ax=axes[1], node_color='lightgreen', edge_color='gray')
axes[1].set_title("Árvore Geradora Máxima")

plt.show()
