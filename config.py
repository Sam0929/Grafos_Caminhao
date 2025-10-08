# config.py

# Configuração para o grafo Fixo 
FIXED_NODES = list(range(1, 5))
FIXED_EDGES_WITH_WEIGHTS = [
    (4, 5, 4), (1, 2, 9), (1, 3, 0),
    (2, 3, 8), (2, 4, 7), (3, 4, 4)
]
FIXED_PATHS_TO_TAKE = [(1, 4), (2, 1), (3, 1), (4, 3)]

# Configuração para o grafo Aleatório
RANDOM_GRAPH_NODES = 1000
P_PROBABILITY_FACTOR = 0.12
RANDOM_SEED = 60