"""
03 Scikit learn

Basic data manipulation.
"""
import utils
import os
import create_data
import matplotlib.pyplot as plt
import numpy as np
import random

from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors


src = "sessions/session-4/data/random_data.csv"
#src = create_data.create_random_n_dims(1000)

def process(data_source):
    # Load data
    if os.path.isfile(data_source):
        data = utils.read_csv_to_np(data_source)
    else:
        data = data_source

    data = standardize(data)

    print(data)
    reduced = dimensionality_reduction(data)
    print(reduced)
    
    scatter_vis(reduced)

    normalized = normalize(reduced)
    print(normalized)
    scatter_vis(normalized)

    clusters = cluster(normalized)
    print(clusters)
    colour_map = get_colour_map(clusters)
    print(colour_map)
    
    scatter_vis_colour(normalized, clusters, colour_map)

    # Nearest neighbour
    nn = nearest_neighbour(normalized, [0.5, 0.5])
    print(nn)
    
    
def dimensionality_reduction(data, dims = 2):
    reductor = TSNE(n_components = dims)
    reduced = reductor.fit_transform(data)
    return reduced

def scatter_vis(data):
    transposed = np.transpose(data)
    plt.scatter(transposed[0], transposed[1])
    plt.show()

def normalize(data):
    return MinMaxScaler((0, 1)).fit_transform(data)

def standardize(data):
    return StandardScaler().fit_transform(data)

def cluster(data, num_clusters = 4):
    kmeans = KMeans(n_clusters = num_clusters, random_state=0) 
    clustered = kmeans.fit(data) 

    # kmeans.cluster_centers_
    # kmeans.predict([[0, 0], [12, 3]])

    return clustered.labels_

def get_colour_map(clusters):
    ret = {}
    used = []
    for item in clusters:
        if item not in used:
            ret[str(item)] = (random.random(), random.random(), random.random())
            used.append(item)
    return ret

def scatter_vis_colour(data, clusters, colour_map):
    transposed = np.transpose(data)
    col = []
    for item in clusters:
        col.append(colour_map[str(item)])

    plt.scatter(transposed[0], transposed[1], c=col)
    plt.show()

def nearest_neighbour(data, query, num_neighbours = 1):
    neigh = NearestNeighbors(n_neighbors = num_neighbours)
    neigh.fit(data)

    result =  neigh.kneighbors([query])

    point_index_array = result[1][0]
    distance_array = result[0][0]

    return point_index_array

process(src)