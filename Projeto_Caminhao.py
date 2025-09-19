import networkx as nx
import matplotlib.pyplot as plt
import math
import numpy as np


I = 4  ## -> Numero de ilhas, nos
P = 5  ## -> Numero de pontes, arestas
S = 4  ## -> Numero de entregas, pesos maximos que deverao ser encontrados entre dois nos 


def draw_graph(G):

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


def how_much_weight(G, path):
    #RETORNA UMA LISTA COM OS PESOS DE UM PATH
    peso_total = []
    for i in range(len(path) - 1):  
        u = path[i]
        v = path[i + 1]
        peso_total.append(G[u][v]['weight']) 
    return peso_total



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

#DESENHANDO O GRAFO
draw_graph(G)

#DICIONARIO COM TODOS OS CAMINHOS DE UM NÓ SOURCE PARA UM TARGET, KEY = (source, target), values = [[caminho],[caminho],[...]]
#OBS: PARA UMA ALTA QUANTIDADE DE NÓS, É INTERESSANTE USAR HAS_PATH ANTES, CASO CONTRARIO, ALLSIMPLEPATHS PODE SE TORNAR MUITO CUSTOSO
paths_dict = {}
for source_node, target_node in paths_to_take:
     paths_dict[(source_node, target_node)] = list(
        nx.all_simple_paths(G, source_node, target_node)
     )
     
#LISTA QUE RECEBERA O CAMINHO COM MAIOR PESO MÍNIMO DE CADA CHAVE DO DICIONARIO
greater_weight_path = []
for pair, ways in paths_dict.items():

    paths_with_weight = [(path, how_much_weight(G, path)) for path in ways]

    greater_weight_path.append(max(paths_with_weight, key=lambda x: min(x[1])))

    
#EXIBINDO O MELHOR CAMINHO, CAMINHO COM MAIOR PESO MÍNIMO
for path in greater_weight_path:
    print(f"\n\nPara este caminho: {path[0]}")
    print(f"Os pesos que os caminhos suportam são: {path[1]}")
    print(f"O menor peso é: {min(path[1])}")


plt.show()

