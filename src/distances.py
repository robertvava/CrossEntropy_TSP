import math

# Assign planar or euclidean distance from a to b
def planar_dist(a,b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
def euclidean_dist(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2) ** 0.5

def total_euclidean_distance(points):
    return sum([euclidean_dist(point, points[index + 1]) for index, point in enumerate(points[:-1])])
def total_planar_distance(points):
    return sum([planar_dist(point, points[index + 1]) for index, point in enumerate(points[:-1])])