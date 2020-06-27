from network import *

with open("coordinates.csv", "r") as cords:
    lines = cords.readlines()
coordinates = []
lines = [line.strip() for line in lines]
for line in lines:
    if line != 'x,y':
        single_cords = line.split(',')
        coordinates.append((single_cords[0], single_cords[1]))
cases = [coordinates[:50], coordinates[50:90], coordinates[90:120], coordinates[120:140], coordinates[140:]]
nodes = []
for cords in cases[4]:
    nodes.append(Node(float(cords[0]), float(cords[1]), cases[4].index(cords)))
config = [20, 25, 30, 20, 25]

caseNetwork = Network(nodes, config[4])
print(caseNetwork.adjacency_matrix)
print(caseNetwork.neighbor_list)