from structures.element import *
from structures.grid import *
from structures.universal_element import *
from utils import *


def generate_grid():
    json = read_json_from_file('./data.json')
    H = json["H"]
    L = json["L"]
    nH = json["nH"]
    nL = json["nL"]
    K = json["conductivity"]
    t = json["initial_temperature"]
    #generate nodes
    dx = H / (nH - 1)
    dy = L / (nL - 1)
    nodes = list()
    for i in range(0, nL):
        for j in range(0, nH):
            node = Node(i * nL + j, (i * dx, j * dy), t)
            if (i == 0 or i == nL - 1) or (j == 0 or j == nL - 1):
                node.bc = True
            nodes.append(node)

    #generate nodes
    elements = list()
    for i in range(0, nL - 1):
        for j in range(0, nH - 1):
            tmp = [nodes[i * nH + j], nodes[(i + 1) * nH + j], nodes[(i + 1) * nH + j + 1], nodes[i * nH + j + 1]]
            elements.append(Element(tmp, K))

    return Grid(nodes=nodes, elements=elements, k=K)


if __name__ == "__main__":
    grid = generate_grid()
    grid.initialize()
