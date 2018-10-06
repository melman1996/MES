class Node:
    def __init__(self, x, y, t):
        self.x = x
        self.y = y
        self.t = t

    def print(self):
        print("{%(x)d, %(y)d}" % {'x': self.x, 'y': self.y})


class Element:
    def __init__(self, nodes):
        self.nodes = nodes

    def print(self):
        print("Element:")
        for node in self.nodes:
            node.print()


class Grid:
    def __init__(self, nodes, elements):
        self.nodes = nodes
        self.elements = elements
