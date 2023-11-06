import uuid
import random
import utils
import os
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def random_network(num_nodes = 1000, num_edges = 2000):
    ret = {"nodes" : [], "edges" : []}
    for i in range(num_nodes):
        ret["nodes"].append({
            "name" : f"Node {str(i)}",
            "id" : str(uuid.uuid4())
        })
    for i in range(num_edges):
        src = ret["nodes"][random.randint(0, len(ret["nodes"]) - 1)]
        found_dest = False
        dest = None
        while found_dest == False:
            dest = ret["nodes"][random.randint(0, len(ret["nodes"]) - 1)]
            if dest != src:
                found_dest = True
        ret["edges"].append({
            "source" : src["id"],
            "target" : dest["id"]
        })
    return ret

def create_random_n_dims(num_points = 300, num_dims = 200, range = [-1000, 1000]):
    ret = np.random.rand(num_points, num_dims)
    scaled = MinMaxScaler((range[0], range[1])).fit_transform(ret)
    return scaled

def save_np_to_csv(np_data, path):
    df = pd.DataFrame(np_data)
    df.to_csv(path, index=False, header=False)

#rand_data = create_random_n_dims()
#save_np_to_csv(rand_data, os.path.join(os.getcwd(), "sessions", "session-4", "data", "random_data.csv"))


#net = random_network()
#utils.write_json(os.path.join(os.getcwd(), "sessions", "session-4", "data", "random_network.json"), net)