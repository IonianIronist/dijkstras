import math
import random


def calculate_distance(a, b):
    return math.sqrt((a.coordinates[0] - b.coordinates[0])**2 + (a.coordinates[1] - b.coordinates[1])**2)


class Network:
    def __init__(self, nodes, radius):
        self.nodes = nodes  # A list of objects of class Node
        self.radius = radius  # nodes' radius for connection
        self.neighbor_list = []
        self.adjacency_matrix = [[0]*len(nodes)]*len(nodes)
        self.calculate_neighbors()
        self.set_neighbor_list()
        self.set_adjacency_matrix()

    def calculate_neighbors(self):
        for node in self.nodes:
            for other_node in self.nodes:
                distance = calculate_distance(node, other_node)
                if distance <= self.radius and node.pointer != other_node.pointer:
                    cost = random.uniform(0, 100)
                    node.add_neighbor(other_node, cost)
                    other_node.add_neighbor(node, cost)

    def set_neighbor_list(self):
        for node in self.nodes:
            self.neighbor_list.append(list(node.neighbors.keys()))

    def set_adjacency_matrix(self):
        for node in self.nodes:
            for i in range(len(self.nodes)):
                if i in self.neighbor_list[node.pointer]:
                    self.adjacency_matrix[node.pointer][i] = 1


class Node:
    def __init__(self, x, y, pointer):
        self.pointer = pointer
        self.coordinates = (x, y)
        self.neighbors = {}

    def add_neighbor(self, neighbor, cost):
        if neighbor.pointer not in self.neighbors:
            self.neighbors[neighbor.pointer] = cost
