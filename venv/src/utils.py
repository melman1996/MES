import json


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