from math import sqrt


class Node:
    def __init__(self, x, y, t):
        self.x = x
        self.y = y
        self.t = t

    def show(self):
        print("{%(x)d, %(y)d}" % {'x': self.x, 'y': self.y})


class Element:
    def __init__(self, nodes):
        self.nodes = nodes

    def show(self):
        print("Element:")
        for node in self.nodes:
            node.show()


class Grid:
    def __init__(self, nodes, elements):
        self.nodes = nodes
        self.elements = elements


class UniversalElement:
    def __init__(self):
        self.p = [
            (-1 / sqrt(3), -1 / sqrt(3)),
            (1 / sqrt(3), -1 / sqrt(3)),
            (1 / sqrt(3), 1 / sqrt(3)),
            (-1 / sqrt(3), 1 / sqrt(3))
        ]
        dndksi = dNdKsi()
        self.pdNdKsi = [
            [dndksi[i](*point) for point in self.p] for i in range(4)
        ]
        dndeta = dNdEta()
        self.pdNdEta = [
            [dndeta[i](*point) for point in self.p] for i in range(4)
        ]

#funkcje ksztaltu
def dNdKsi():
    return [
        lambda ksi, eta: -0.25 * (1 - eta),
        lambda ksi, eta: 0.25 * (1 - eta),
        lambda ksi, eta: 0.25 * (1 + eta),
        lambda ksi, eta: -0.25 * (1 - eta)
    ]

def dNdEta():
    return [
        lambda ksi, eta: -0.25 * (1 - ksi),
        lambda ksi, eta: -0.25 * (1 + ksi),
        lambda ksi, eta: 0.25 * (1 + ksi),
        lambda ksi, eta: 0.25 * (1 - ksi)
    ]