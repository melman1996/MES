from tabulate import tabulate
import json
import numpy as np


#pretty print matrice
def pprint(name, matrix):
	print(name + ":")
	print(tabulate(matrix))

#czytanie pliku
def read_json_from_file(path):
	with open(path) as file:
		data = json.load(file)
	return data


#funkcje ksztaltu
def N():
	return [
		lambda ksi, eta: 0.25 * (1 - ksi) * (1 - eta),
		lambda ksi, eta: 0.25 * (1 + ksi) * (1 - eta),
		lambda ksi, eta: 0.25 * (1 + ksi) * (1 + eta),
		lambda ksi, eta: 0.25 * (1 - ksi) * (1 + eta)
	]

def dNdKsi():
	return [
		lambda ksi, eta: -0.25 * (1 - eta),
		lambda ksi, eta: 0.25 * (1 - eta),
		lambda ksi, eta: 0.25 * (1 + eta),
		lambda ksi, eta: -0.25 * (1 + eta)
	]


def dNdEta():
	return [
		lambda ksi, eta: -0.25 * (1 - ksi),
		lambda ksi, eta: -0.25 * (1 + ksi),
		lambda ksi, eta: 0.25 * (1 + ksi),
		lambda ksi, eta: 0.25 * (1 - ksi)
	]


#matrices and vectors
def multiply_matrices(m1, m2):
	x = np.array(m1)
	y = np.array(m2)
	return x.dot(y)


def multiply_matrix_vector(m1, v1):
	x = np.array(m1)
	y = np.array(v1)
	return np.matmul(x, y)
