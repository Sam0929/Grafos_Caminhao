import networkx as nx
import matplotlib.pyplot as plt
import math
import numpy as np

I = 4  ## -> Numero de ilhas, nos
P = 5  ## -> Numero de pontes, arestas
S = 4  ## -> Numero de entregas, pesos maximos que deverao ser encontrados entre dois nos 

nodes_in_range = list(range(1, I + 1))

edges_with_weights = [(4,5,4), 
                      (1,2,9), 
                      (1,3,0), 
                      (2,3,8), 
                      (2,4,7), 
                      (3,4,4)]

paths_to_take = [(1,4),
                 (2,1),
                 (3,1),
                 (4,3)]

## CRIANDO O GRAFO
G = nx.Graph()

# ADICIONANDO OS NOS
G.add_nodes_from(nodes_in_range)

# ADICIONANDO ARESTAS COM PESOS
G.add_weighted_edges_from(edges_with_weights, weight = 'weight')

#CRIANDO UM SPRING LAYOUT PARA A POSICAO DOS NOS E ARESTAS
pos = nx.spring_layout(G, seed = 7)


#DESENHANDO OS NOS
nx.draw_networkx_nodes(G, pos, node_size=400)
#DESENHANDO AS ARESTAS
nx.draw_networkx_edges(G, pos, width=3, alpha=0.5, edge_color="b")


#ROTULOS PARA OS NOS
nx.draw_networkx_labels(G, pos, font_size=15, font_family="sans-serif")

#ROTULOS PARA AS ARESTAS, NO CASO OS PESOS
edge_labels = nx.get_edge_attributes(G, "weight")
#DESENHANDO OS ROTULOS DAS ARESTAS
nx.draw_networkx_edge_labels(G, pos, edge_labels)


#MOSTRANDO O GRAFICO
plt.show()