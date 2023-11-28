import networkx as nx
import matplotlib.pyplot as plt
import utils
import os

chemin = os.path.join(os.getcwd(), "sessions", "session-4", "data", "random_network.json")


def process(path):
    # Changer les donnees:
    donnees = utils.read_json(path)

    # Créer un graphe networkx:
    G = nx.Graph()

    # Ajouter les noeuds:
    ajouter_noeuds(G, donnees)

    # Ajouter les arretes:
    ajouter_arretes(G, donnees)

    # Visualiser le graph:
    #visualisation(G, donnees)

    # Analyser le réseau:
    analyse(G)
    
def analyse(graph):
    centrality = nx.degree_centrality(graph)
    
    centrality_list = []
    for node in centrality:
        centrality_list.append({
            "id" : node,
            "centrality" : centrality[node]
        })
    centrality_ordonnee = sorted(centrality_list, key = lambda d: d['centrality'], reverse=True)
    print(centrality_ordonnee[:5])

    source = centrality_ordonnee[0]
    target = centrality_ordonnee[1]

    has_path = nx.has_path(graph, source["id"], target["id"])
    print(has_path)
    sp = []
    if has_path:
        shortest_path = nx.all_shortest_paths(graph, source["id"], target["id"])
        [sp.append(p) for p in shortest_path]
        print(len(sp))
    else:
        print("No path found")
    

# def analysis(graph, data, out_dest):
    
#     # Shortest path
#     print()
#     has_path = nx.has_path(graph, centrality_sorted[0]["id"], centrality_sorted[1]["id"])
#     sp = []
#     if has_path:
#         shortest_path = nx.all_shortest_paths(graph, centrality_sorted[0]["id"], centrality_sorted[1]["id"])
#         [sp.append(p) for p in shortest_path]
#         print(sp)

#     # Output results
#     utils.write_json(os.path.join(out_dest, "network_analysis.json"), {
#         "centrality" : {"1" : centrality_sorted[0], "2" : centrality_sorted[1]},
#         "path" : sp
#     })

def ajouter_noeuds(graph, data):
    for node in data["nodes"]:
        graph.add_node(node["id"])

def ajouter_arretes(graph, data):
    for arrete in data["edges"]:
        graph.add_edge(arrete["source"], arrete["target"])

def creer_etiquettes(data):
    etiquettes = {}
    for node in data["nodes"]:
        etiquettes[node["id"]] = node["name"]
    return etiquettes


def visualisation(graph, data):
    """Cette fonction permet de visualiser le graph."""
    
    # Creer une copie du graphe networkx:
    gCopy = graph

    # Créer les étiquettes:
    et = creer_etiquettes(data)
    gCopy = nx.relabel_nodes(gCopy, et)

    # Appliquer un algorithme de disposition:
    p = aplliquer_disposition(gCopy, "spring")
    
    # Visualiser:
    nx.draw_networkx(gCopy, pos = p)
    plt.show()
    

def aplliquer_disposition(graph, algo = "spring"):
    if algo == "spring":
        pos = nx.spring_layout(graph, seed = 3000)
    elif algo == "circular":
        pos = nx.circular_layout(graph)
    else:
        pos = nx.spring_layout(graph, seed = 3000)

    return pos
    
process(chemin)