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
			[dndksi[i](*point) for point in self.p] for i in range(4)
		]
		dndeta = dNdEta()
		self.pdNdEta = [
			[dndeta[i](*point) for point in self.p] for i in range(4)
		]

	def generate_matrice_J(self, element):
		dKsi = [
			[
				sum([
					element.nodes[k].coord[j] * self.pdNdKsi[k][i] for k in range(4)
				]) for i in range(4)
			] for j in range(2)
		]
		dEta = [
			[
				sum([
					element.nodes[k].coord[j] * self.pdNdEta[k][i] for k in range(4)
				]) for i in range(4)
			] for j in range(2)
		]
		self.jakobian = dKsi + dEta
		self.detJ = [
			self.jakobian[0][i] * self.jakobian[3][i] - self.jakobian[1][i] * self.jakobian[2][i] for i in range(4)
		]
		dN1dX = [
			self.jakobian[3][i] / self.detJ[i] for i in range(4)
		]
		dN2dX = [
			- self.jakobian[1][i] / self.detJ[i] for i in range(4)
		]
		dN3dX = [
			self.jakobian[2][i] / self.detJ[i] for i in range(4)
		]
		dN4dX = [
			self.jakobian[0][i] / self.detJ[i] for i in range(4)
		]
		self.dNdX = [dN1dX, dN2dX, dN3dX, dN4dX]