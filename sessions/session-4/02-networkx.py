"""
02 networkx

Basic network visualisation.
"""

import networkx as nx
import matplotlib.pyplot as plt
import utils
import os
import create_data

src = "sessions/session-4/data/random_network.json"
#src = create_data.random_network(10, 20)

def process(data_source):
    if isinstance(data_source, dict):
        data = data_source
    else:
        data = utils.read_json(data_source)

    G = nx.Graph()

    add_nodes(data, G)
    add_edges(data, G)

    display(G, data, "name", "spring", True)
    analysis(G, data, os.path.join(os.getcwd(), "sessions", "session-4", "data"))

def add_nodes(data, graph):
    for node in data["nodes"]:
        graph.add_node(node["id"])

def add_edges(data, graph):
    for edge in data["edges"]:
        graph.add_edge(edge["source"], edge["target"])

def analysis(graph, data, out_dest):
    # https://networkx.org/documentation/stable/reference/algorithms/index.html

    # Process centrality
    centrality = nx.degree_centrality(graph)
    centrality_list = []
    for node in centrality:
        centrality_list.append({
            "id" : node, 
            "name" : get_node_prop(data, node, "name"), 
            "centrality" : centrality[node]})
    centrality_sorted = sorted(centrality_list, key=lambda d: d['centrality'], reverse = True) 

    for item in centrality_sorted:
        print(item)

    # Display centrality
    x_data = []
    y_data = []
    for item in centrality_list:
        x_data.append(item["name"])
        y_data.append(item["centrality"])
    plt.scatter(x_data, y_data)
    plt.show()
    plt.savefig(os.path.join(out_dest, "centrality.png"), dpi=300)
    
    # Shortest path
    print()
    has_path = nx.has_path(graph, centrality_sorted[0]["id"], centrality_sorted[1]["id"])
    sp = []
    if has_path:
        shortest_path = nx.all_shortest_paths(graph, centrality_sorted[0]["id"], centrality_sorted[1]["id"])
        [sp.append(p) for p in shortest_path]
        print(sp)

    # Output results
    utils.write_json(os.path.join(out_dest, "network_analysis.json"), {
        "centrality" : {"1" : centrality_sorted[0], "2" : centrality_sorted[1]},
        "path" : sp
    })

def get_node_prop(data, id, prop):
    for node in data["nodes"]:
        if node["id"] == id:
            return node[prop]

def display(graph, data, label_attribute = "name", algo = "spring", show_labels = False) -> None:
    """Display the graph in a matplotlib GUI window."""

    # Create a copy of the graph:
    gCopy = graph

    # Relabel nodes
    labelMap = get_label_map(label_attribute, data)
    gCopy = nx.relabel_nodes(gCopy, labelMap)

    # Get positions for display:
    pos = apply_layout(gCopy, algo)
    
    # Draw and display the graph:
    nx.draw(gCopy, pos = pos, with_labels = show_labels)
    plt.show()

def get_label_map(labelAttribute: str, data) -> None:
    """Return a label map for display."""
    
    labelMap = {}
    for node in data["nodes"]:
        labelMap[node["id"]] = node[labelAttribute]
    
    return labelMap

def apply_layout(graph: nx.Graph, algo: str) -> dict:
    """Apply a layout algorithm to a network graph."""

    if algo == "spring":
        pos = nx.spring_layout(graph, seed=3068)
    elif algo == "circular":
        pos = nx.circular_layout(graph)
    elif algo == "fr":
        pos = nx.fruchterman_reingold_layout(graph)
    elif algo == "spectral":
        pos = nx.spectral_layout(graph)
    elif algo == "random":
        pos = nx.random_layout(graph)
    else:
        pos = nx.spring_layout(graph, seed=3068)

    return pos

process(src)
