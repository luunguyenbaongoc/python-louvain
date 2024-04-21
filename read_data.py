import os
import networkx as nx

#Read raw data from file and transfer to list
def read_dimacs(
    path="./dimacs10-polbooks/out.dimacs10-polbooks",
):
    with open(path, "r") as f:
        lines = f.readlines()

        datas = []
        for line in lines[1:]:
            line = line.strip().split()
            datas.append(line)

    return datas

#Convert data to graph
def convert_to_graph(datas):
    G = nx.Graph()

    #Get a list of non-duplicate nodes then add nodes to graph
    all_members = set(ele for data in datas for ele in data)
    G.add_nodes_from(all_members)
    G.name = "Koblenz Network Collection"

    #Add edge to graph
    for data in datas:
        G.add_edge(data[0], data[1])
    return G


if __name__ == "__main__":
    print(len(read_dimacs()))
