# visualization.py

import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(G, pos, title, ax=None, node_color='lightblue', edge_color='b'):

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
    ax.set_title(title)


def draw_n_things(*plots, layout='horizontal', figsize=(12, 6), zoom=True):
   
    n = len(plots)
    if n == 0:
        raise ValueError("Você precisa passar pelo menos um plot!")

    if layout == 'horizontal':
        fig, axes = plt.subplots(1, n, figsize=figsize, layout="constrained")
    else:
        fig, axes = plt.subplots(n, 1, figsize=figsize, layout="constrained")

    if n == 1:
        axes = [axes]
   
    for ax, func in zip(axes, plots):
        func(ax)

    if zoom:
        try:
            manager = plt.get_current_fig_manager()
            manager.window.state('zoomed')
        except Exception:
            pass  

    plt.show()

def plot_graph_and_mst(graph, mst):
  
    pos = nx.spring_layout(graph, seed=10) # Layout unificado para ambos

    draw_n_things(
        lambda ax: (
            draw_graph(graph, pos=pos, ax=ax, title='Grafo Original', node_color='lightblue'),
        ),
        lambda ax: (
            draw_graph(mst, pos=pos, ax=ax, title='Árvore Geradora Máxima', node_color='lightgreen'),
        )
    )

def plot_gnp_statistics(stats_data):

    n = stats_data["n_values"]
    s = stats_data["s_values"]
    deg = stats_data["degree_values"]
    deg10 = stats_data["degree_values_10"]
    p = stats_data["p_base"]
    p10 = stats_data["p_10"]
    expected_edges = stats_data["expected_edges_values"]
    expected_edges_10 = stats_data["expected_edges_values_10"]

    draw_n_things(
        lambda ax: (
            ax.plot(n, s, label="S(N)"),
            ax.set_title(f"Evolução de S com N (p={p10:.3f})"),
            ax.set_xlabel("Número de vértices (N)"),
            ax.set_ylabel("Fração do Componente Gigante (S)"),
            ax.grid(True),
            ax.legend()
        ),
        lambda ax: (
            ax.plot(n, deg, label="Grau Médio"),
            ax.set_title(f"Evolução do Grau Médio (p={p:.3f})"),
            ax.set_xlabel("Número de vértices (N)"),
            ax.set_ylabel("Grau Médio"),
            ax.grid(True),
            ax.legend()
        ),
        lambda ax: (
            ax.plot(n, deg10, label="Grau Médio (p*0.1)", color='orange'),
            ax.set_title(f"Evolução do Grau Médio (p={p10:.3f})"),
            ax.set_xlabel("Número de vértices (N)"),
            ax.set_ylabel("Grau Médio"),
            ax.grid(True),
            ax.legend()
        ),
        lambda ax: (
            ax.plot(n, expected_edges, label="Arestas Esperadas", color='green'),
            ax.set_title(f"Arestas Esperadas (p={p:.3f})"),
            ax.set_xlabel("Número de vértices (N)"),
            ax.set_ylabel("Número de Arestas Esperadas"),
            ax.grid(True),
            ax.legend()
        ),
        lambda ax: (
            ax.plot(n, expected_edges_10, label="Arestas Esperadas (p*0.1)", color='red'),
            ax.set_title(f"Arestas Esperadas (p={p10:.3f})"),
            ax.set_xlabel("Número de vértices (N)"),
            ax.set_ylabel("Número de Arestas Esperadas"),
            ax.grid(True),
            ax.legend()
        ),

    )