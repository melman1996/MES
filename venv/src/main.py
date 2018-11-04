from structures.grid import *
from structures.universal_element import *
from utils import *


def generate_grid():
	json = read_json_from_file('./data.json')
	H = json["H"]
	L = json["L"]
	nH = json["nH"]
	nL = json["nL"]
	K = json["K"]
	t = json["t"]
	dx = L/nL
	dy = H/nH
	nodes = list()
	for i in range(0, nL):
		for j in range(0, nH):
			nodes.append(Node((i * dx, j * dy), t))

	elements = list()
	for i in range(0, nL - 1):
		for j in range(0, nH - 1):
			tmp = [nodes[i * nH + j], nodes[(i + 1) * nH + j], nodes[(i + 1) * nH + j + 1], nodes[i * nH + j + 1]]
			elements.append(Element(tmp))

	return Grid(nodes=nodes, elements=elements)


if __name__ == "__main__":
	universal_element = UniversalElement()
	grid = generate_grid()

	# check universal element
	grid.elements[0].show()
	print("dN/dKsi:")
	for tab in universal_element.pdNdKsi:
		print(tab)
	print("dN/dEta:")
	for tab in universal_element.pdNdEta:
		print(tab)
	print("Jakobian:")
	universal_element.generate_matrice_J(grid.elements[0])
	for tab in universal_element.jakobian:
		print(tab)
	print("DetJ:")
	print(universal_element.detJ)
	print("dN/dX:")
	for tab in universal_element.dNdX:
		print(tab)
