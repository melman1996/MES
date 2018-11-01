from utils import *

from math import sqrt


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