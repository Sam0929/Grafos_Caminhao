# main.py

import random

import config as cfg
import graph_utils as gu
import visualization as vi


def main():
  
    mode = 'random' # 'random' ou 'fixed'
    
    if mode == 'fixed':
        G = gu.create_fixed_graph()
        paths_to_take = cfg.FIXED_PATHS_TO_TAKE
    else:
        G = gu.create_random_graph(cfg.RANDOM_GRAPH_NODES, cfg.P_PROBABILITY_FACTOR, cfg.RANDOM_SEED)
        paths_to_take = [tuple(random.sample(range(cfg.RANDOM_GRAPH_NODES), 2)) for _ in range(cfg.RANDOM_GRAPH_NODES)] #lista de tuplas, com nós sendo gerados dois a dois no range 0 até random_graph_nodes

    print(f"Analisando o grafo no modo: '{mode}' com {G.number_of_nodes()} nós e {G.number_of_edges()} arestas.")
    
    path_analysis_results, G_max_tree = gu.analyze_paths(G, paths_to_take)
    
    print('\nResultado da Análise (Maior peso para ir de A até B):\n')
    for (source, target), weight in list(path_analysis_results.items()):
        print(f'De A:{source} para B:{target} -> Maior peso suportado: {weight}')
    

    ## PLOTANDO GRAFOS
    print("\nGerando visualizações...")

    #  Plotando grafos apenas se N < 50 ou modo fixo
    if cfg.RANDOM_GRAPH_NODES <= 50 or mode == 'fixed':
        vi.plot_graph_and_mst(G, G_max_tree)

    # Plotando estatisticas GNP
    stats = gu.calculate_gnp_statistics(G.number_of_nodes(), cfg.P_PROBABILITY_FACTOR)
    vi.plot_gnp_statistics(stats)
 
    

if __name__ == "__main__":
    main()