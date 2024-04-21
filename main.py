from community import community_louvain
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import networkx as nx

from read_data import convert_to_graph, read_dimacs

# load dataset from read_data.py
G = convert_to_graph(read_dimacs())

# compute the best partition
partition = community_louvain.best_partition(G)

# draw the graph
pos = nx.spring_layout(G)

# color the nodes according to their partition
cmap = cm.get_cmap("viridis", max(partition.values()) + 1)
nx.draw_networkx_nodes(
    G,
    pos,
    partition.keys(),
    node_size=40,
    cmap=cmap,
    node_color=list(partition.values()),
)
nx.draw_networkx_edges(G, pos, alpha=0.5)
plt.show()
