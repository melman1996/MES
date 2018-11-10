from utils import *


class Node:
    def __init__(self, coord, t):
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


class Grid:
    def __init__(self, nodes, elements):
        self.nodes = nodes
        self.elements = elements
