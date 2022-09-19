import matplotlib.pyplot as plt

def plot_network(points, tour, n):
    plt.figure(figsize = (10, 8))
    plt.plot([points[tour[i % n]][0] for i in range(n+1)], [points[tour[i % n]][1] for i in range(n+1)], 'xb--')

def plot_best_path(bf, points, tour, n, start = None):
    if start is None:
        start = points[0]
    plt.figure(figsize = (10, 8))
    plt.title('Best path')
    plt.plot([bf[tour[i % n]][0] for i in range(n+1)], [bf[tour[i % n]][1] for i in range(n+1)], 'xb--')
    for i in range(len(tour)):
        plt.scatter(bf[i][0], bf[i][1], s = 100, c = 'g')
        plt.text(bf[i][0], bf[i][1], 'Node ' + str(i+1))
    plt.scatter(start[0], start[1], s = 200, c = 'r')