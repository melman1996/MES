from utils import *

from math import sqrt
from operator import add


class UniversalElement:
	def __init__(self, element, ro, c, alfa):
		self.element = element
		self.p = [
			(-1 / sqrt(3), -1 / sqrt(3)),
			(1 / sqrt(3), -1 / sqrt(3)),
			(1 / sqrt(3), 1 / sqrt(3)),
			(-1 / sqrt(3), 1 / sqrt(3))
		]
		self.ro = ro
		self.c = c
		self.alfa = alfa
		self.length = [0, 0, 0, 0]

		self.generate_matrices()
		self.generate_matrix_J()
		self.generate_matrix_H()
		self.generate_matrix_C()
		self.generate_matrix_bc_H()
		self.generate_vector_P()

	def generate_matrices(self):
		dndksi = dNdKsi()
		self.pdNdKsi = [
			[dndksi[i](*point) for point in self.p] for i in range(4)
		]
		dndeta = dNdEta()
		self.pdNdEta = [
			[dndeta[i](*point) for point in self.p] for i in range(4)
		]

	def generate_matrix_J(self):
		dKsi = [
			[
				sum([
					self.element.nodes[i].coord[k] * self.pdNdKsi[i][j] for i in range(4)
				]) for j in range(4)
			] for k in range(2)
		]
		dEta = [
			[
				sum([
					self.element.nodes[i].coord[k] * self.pdNdEta[i][j] for i in range(4)
				]) for j in range(4)
			] for k in range(2)
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
				self.jxxx[0][j] * self.pdNdKsi[i][j] + self.jxxx[1][j] * self.pdNdEta[i][j] for i in range(4)
			] for j in range(4)
		]
		self.dNdY = [
			[
				self.jxxx[2][j] * self.pdNdKsi[i][j] + self.jxxx[3][j] * self.pdNdEta[i][j] for i in range(4)
			] for j in range(4)
		]

	def generate_matrix_H(self):
		self.dNdXdNdXTDetJ = [
			[
				[
					self.dNdX[k][i] * self.dNdX[k][j] * self.detJ[k] for i in range(4)
				] for j in range(4)
			] for k in range(4)
		]
		self.dNdYdNdYTDetJ = [
			[
				[
					self.dNdY[k][i] * self.dNdY[k][j] * self.detJ[k] for i in range(4)
				] for j in range(4)
			] for k in range(4)
		]
		self.Ktimes = [
			[
				[
					self.element.K * (self.dNdXdNdXTDetJ[k][j][i] + self.dNdYdNdYTDetJ[k][j][i]) for i in range(4)
				] for j in range(4)
			] for k in range(4)
		]
		self.matrixH = [
			[
				self.Ktimes[0][j][i] + self.Ktimes[1][j][i] + self.Ktimes[2][j][i] + self.Ktimes[3][j][i] for i in range(4)
			] for j in range(4)
		]

	def generate_matrix_C(self):
		n = N()
		self.Np = [
			[
				n[i](*point) for i in range(4)
			] for point in self.p
		]
		self.tmp = [
			[
				[
					self.Np[k][i] * self.Np[k][j] * self.detJ[k] * self.c * self.ro for i in range(4)
				] for j in range(4)
			] for k in range(4)
		]
		self.C = [
			[
				self.tmp[0][j][i] + self.tmp[1][j][i] + self.tmp[2][j][i] + self.tmp[3][j][i] for i in range(4)
			] for j in range(4)
		]

	def generate_matrix_bc_H(self):
		points = [
			(-1 / sqrt(3), -1),
			(1 / sqrt(3), -1),
			(1, -1 / sqrt(3)),
			(1, 1 / sqrt(3)),
			(1 / sqrt(3), 1),
			(-1 / sqrt(3), 1),
			(-1, 1 / sqrt(3)),
			(-1, -1 / sqrt(3)),
		]
		n = N()
		self.H = [[0] * 4 for i in range(4)]
		for z in range(4):
			index0, index1 = z, z+1
			if index1 >= len(self.element.nodes):
				index1 = 0
			self.length[z] = sqrt(pow(self.element.nodes[index0].coord[0] - self.element.nodes[index1].coord[0], 2) + pow(self.element.nodes[index0].coord[1] - self.element.nodes[index1].coord[1], 2))
			if self.element.nodes[index0].bc and self.element.nodes[index1].bc:
				pN = [
					[n[i](*points[z * 2]) for i in range(4)],
					[n[i](*points[z * 2 + 1]) for i in range(4)]
				]
				pc0 = [
					[
						pN[0][j] * pN[0][i] * self.alfa for i in range(4)
					] for j in range(4)
				]
				pc1 = [
					[
						pN[1][j] * pN[1][i] * self.alfa for i in range(4)
					] for j in range(4)
				]
				sum = [
					[
						(x + y) * self.length[z]/2 for x, y in zip(list1, list2)
					] for list1, list2 in zip(pc0, pc1)
				]
				self.H = [
					[
						x + y for x, y in zip(list1, list2)
					] for list1, list2 in zip(self.H, sum)
				]

	def generate_vector_P(self):
		points = [
			(-1 / sqrt(3), -1),
			(1 / sqrt(3), -1),
			(1, -1 / sqrt(3)),
			(1, 1 / sqrt(3)),
			(1 / sqrt(3), 1),
			(-1 / sqrt(3), 1),
			(-1, 1 / sqrt(3)),
			(-1, -1 / sqrt(3)),
		]
		n = N()
		self.P = [0] * 4
		for point in points:
			for i in range(4):
				self.P[i] += n[i](*point)
		for i in range(4):
			if not self.element.nodes[i].bc:
				self.P[i] = 0
			else:
				self.P[i] *= self.alfa * self.element.nodes[i].t * self.length[i] / 2