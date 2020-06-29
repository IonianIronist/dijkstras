from network import *
from time import time
from matplotlib import pyplot as plt
import dijkstra_matrix
import dijkstra_list

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
configs = [20, 25, 30, 20, 25]
times = []
times2 = []
for case, config in zip(cases, configs):
    for cords in case:
        nodes.append(Node(float(cords[0]), float(cords[1]), case.index(cords)))
    caseNetwork = Network(nodes, config)
    costs = []
    start = time()
    for s in range(len(caseNetwork.nodes)):
        dijkstra_matrix.dijkstra_matrix(caseNetwork, s)
    end = time()
    delta = end - start
    times.append(delta)
    start2 = time()
    for s in range(len(caseNetwork.nodes)):
        dijkstra_list.dijkstra_list(caseNetwork, s)
    end2 = time()
    delta2 = end2 - start2
    times2.append(delta2)
    nodes.clear()
times.reverse()
times2.reverse()
x = [len(i) for i in cases]
x.reverse()
print(times)
print(x)
plt.scatter([x for x in times], [n for n in x], s=10)
plt.scatter([x for x in times2], [n for n in x], s=10)
plt.show()
