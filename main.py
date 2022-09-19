import numpy as np
import random
from matplotlib import pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
from sys import maxsize
from itertools import permutations
import time
import torch.nn.functional as f
from scipy import optimize
from src.distances import *
from src.plots import *


def tsp_env(n = 10, m = 100, distance = 'Euclidean'):
    points = [[random.randint(0,m), random.randint(0,m)] for i in range(n)]
    tour = random.sample(range(n),n)
    tour_dict = {'Node ' + str(i): points[i] for i in range(n)}
    if distance == 'Planar':
        distances = [[planar_dist(points[i], points[j]) for i in range(n)] for j in range(n)]
    elif distance == 'Euclidean':
        distances = [[euclidean_dist(points[i], points[j]) for i in range(n)] for j in range(n)]
    return points, tour, tour_dict, distances, n


def brute_force(points, start = None):
    if start is None:
        start = points[0]
    return min([perm for perm in permutations(points) if perm[0] == start], key=total_planar_distance)


n, m = 9, 100  # Total nodes, or cities, in the graph, and the maximum distance between two cities. 

points, tour, tour_dict, distances, n = tsp_env(n, m)

print (tour_dict)
print (tour)
print (points)
start = time.perf_counter()
bf = brute_force(points)
end = time.perf_counter()
print (f"\n Brute_force time for {n} Nodes: {end-start} seconds. \n")
print (bf)



plot_network(points, tour, n)
plot_best_path(bf, points, tour, n, start = None)
plt.show()