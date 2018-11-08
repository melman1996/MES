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
        self.generate_matrices()

    def generate_matrices(self):
        dndksi = dNdKsi()
        self.pdNdKsi = [
            [dndksi[i](*point) for i in range(4)] for point in self.p
        ]
        dndeta = dNdEta()
        self.pdNdEta = [
            [dndeta[i](*point) for i in range(4)] for point in self.p
        ]

    def generate_matrice_J(self, element):
        dKsi = [
            [
                sum([
                    element.nodes[k].coord[j] * self.pdNdKsi[i][k] for k in range(4)
                ]) for i in range(4)
            ] for j in range(2)
        ]
        dEta = [
            [
                sum([
                    element.nodes[k].coord[j] * self.pdNdEta[i][k] for k in range(4)
                ]) for i in range(4)
            ] for j in range(2)
        ]
        self.jxx = dKsi + dEta
        self.detJ = [
            self.jxx[0][i] * self.jxx[3][i] - self.jxx[1][i] * self.jxx[2][i] for i in range(4)
        ]
        self.jxxx = [
            [self.jxx[3][i] / self.detJ[i] for i in range(4)],
            [-self.jxx[1][i] / self.detJ[i] for i in range(4)],
            [self.jxx[2][i] / self.detJ[i] for i in range(4)],
            [self.jxx[0][i] / self.detJ[i] for i in range(4)]
        ]
        self.dNdX = [
            [
                self.jxxx[0][j] * self.pdNdKsi[j][i] + self.jxxx[1][j] * self.pdNdEta[j][i] for i in range(4)
            ] for j in range(4)
        ]
        self.dNdY = [
            [
                self.jxxx[2][j] * self.pdNdKsi[j][i] + self.jxxx[3][j] * self.pdNdEta[j][i] for i in range(4)
            ] for j in range(4)
        ]
