import networkx as nx
import matplotlib.pyplot as plt
import math
import numpy as np


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


def draw_graph(G, ax=None, node_color='lightblue', edge_color='b'):
    # Cria o layout
    pos = nx.spring_layout(G, seed=7)

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



## CRIANDO O GRAFO
G = nx.Graph()

# ADICIONANDO OS NOS
G.add_nodes_from(NODES_IN_RANGE)

# ADICIONANDO ARESTAS COM PESOS
G.add_weighted_edges_from(EDGES_WITH_WEIGHTS, weight = 'weight')


G_maximum_tree = nx.maximum_spanning_tree(G, weight='weight', algorithm='kruskal', ignore_nan=False)


minimum_path_between_nodes = []

for source_node, target_node in PATHS_TO_TAKE:
    aux = nx.shortest_path(G_maximum_tree, source=source_node, target=target_node)
    minimum_path_between_nodes.append(aux)


greater_weight_path = [minimum_weight_path(G_maximum_tree, path) for path in minimum_path_between_nodes]


print(greater_weight_path)



#DESENHANDO O GRAFO
fig, axes = plt.subplots(1, 2, figsize=(12,6))

# Grafo original
draw_graph(G, ax=axes[0], node_color='lightblue', edge_color='gray')
axes[0].set_title("Grafo Original")

# Árvore geradora
draw_graph(G_maximum_tree, ax=axes[1], node_color='lightgreen', edge_color='gray')
axes[1].set_title("Árvore Geradora Máxima")

plt.show()
