from utils import *
from structures.universal_element import *


class Grid:
	def __init__(self, nodes, elements, k):
		self.nodes = nodes
		self.elements = elements
		self.k = k

		self.H = [[0] * len(self.nodes) for i in range(len(self.nodes))]
		self.C = [[0] * len(self.nodes) for i in range(len(self.nodes))]
		self.P = [0] * len(self.nodes)

		self.read_file()
		self.initialize_universal_elements()
		self.map_matrices()

		#self.show(0)

	def initialize(self):
		t0 = [node.t for node in self.nodes]
		for i in range(int(self.time/self.step)):
			cdtp = [
				x + p for p, x in zip(self.P, multiply_matrix_vector(self.CDT, t0))
			]
			t1 = solve(self.HCT, cdtp)
			print("----------Iteration {}----------".format(i + 1))
			#print(t1)
			print("Min: {}, max: {}".format(min(t1), max(t1)))
			self.update_temperatures(t1)
			self.draw_grid(t1)
			t0 = t1

	def initialize_universal_elements(self):
		self.universal_elements = list()
		for element in self.elements:
			universal_element = UniversalElement(element, self.ro, self.c, self.alfa, self.tot)
			self.universal_elements.append(universal_element)

	def map_matrices(self):
		for element, universal_element in zip(self.elements, self.universal_elements):
			for i in range(4):
				self.P[element.nodes[i].id] += universal_element.P[i]
				for j in range(4):
					self.H[element.nodes[i].id][element.nodes[j].id] += universal_element.H[i][j]
					self.C[element.nodes[i].id][element.nodes[j].id] += universal_element.C[i][j]
		self.CDT = [
			[c / self.step for c in C] for C in self.C
		]
		self.HCT = [
			[
				h + c for h, c in zip(H, CDT)
			] for H, CDT in zip(self.H, self.CDT)
		]
		self.t0 = [
			node.t for node in self.nodes
		]

	def update_temperatures(self, t1):
		for node, t in zip(self.nodes, t1):
			node.t = t

	def read_file(self):
		json = read_json_from_file('./data.json')
		self.nH = json["nH"]
		self.nL = json["nL"]
		self.c = json["specific_heat"]
		self.k = json["conductivity"]
		self.t = json["initial_temperature"]
		self.tot = json["ambient_temperature"]
		self.alfa = json["alfa"]
		self.ro = json["density"]
		self.time = json["time"]
		self.step = json["step"]

	def show(self, iteration):
		print("----------Iteration {}----------".format(iteration))
		pprint("H", self.H)
		pprint("C", self.C)

	def draw_grid(self, array):
		draw_grid(array, self.nL, self.nH)
