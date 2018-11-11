from utils import *


class Node:
    def __init__(self, id, coord, t):
        self.id = id
        self.coord = coord
        self.t = t
        self.bc = False

    def show(self):
        print("x: {}, y: {}".format(self.coord[0], self.coord[1]))


class Element:
    def __init__(self, nodes, K):
        self.nodes = nodes
        self.K = K

    def show(self):
        print("Element:")
        for node in self.nodes:
            node.show()

