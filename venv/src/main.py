from structures import *

import json

def read_json_from_file(path):
    with open(path) as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    json = read_json_from_file('./data.json')
    H = json["H"]
    L = json["L"]
    nH = json["nH"]
    nL = json["nL"]
    K = json["K"]
    t = json["t"]

    universal = UniversalElement()


    # nodes = list()
    # for i in range(0, nL):
    #     for j in range(0, nH):
    #         nodes.append(Node(i, j, t))
    #
    # elements = list()
    # for i in range(0, nL - 1):
    #     for j in range(0, nH - 1):
    #         tmp = [nodes[i * nH + j], nodes[(i + 1) * nH + j], nodes[(i + 1) * nH + j + 1], nodes[i * nH + j + 1]]
    #         elements.append(Element(tmp))
    #
    # grid = Grid(nodes=nodes, elements=elements)