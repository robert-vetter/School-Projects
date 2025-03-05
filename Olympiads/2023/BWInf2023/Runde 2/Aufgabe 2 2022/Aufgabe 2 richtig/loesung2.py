import matplotlib.pyplot as plt
import random
import math

def load_points(filename):
    points = []
    with open(filename) as f:
        for line in f:
            x, y = map(float, line.strip().split())
            points.append((x, y))
    return points

def plot_points_and_route(points, route):
    xs, ys = zip(*points)
    plt.plot([xs[i] for i in route + [route[0]]], [ys[i] for i in route + [route[0]]])
    plt.show()

def nearest_neighbor_tsp(points):
    start = random.randint(0, len(points) - 1)
    route = [start]
    unvisited = set(range(len(points)))
    unvisited.remove(start)
    while unvisited:
        closest = None
        if len(route) == 1:
            closest = min(unvisited, key=lambda i: euclidean_distance(points[route[0]], points[i]))
        else:
            for i in unvisited:
                angle = calc_angle(points[route[-1]], points[i], points[route[-2]])
                if closest is None or (euclidean_distance(points[route[-1]], points[i]) < euclidean_distance(points[route[-1]], points[closest]) and angle >= 90):
                    closest = i
        route.append(closest)
        unvisited.remove(closest)
    return route

def calc_angle(p1, p2, p3):
    v1 = (p2[0] - p1[0], p2[1] - p1[1])
    v2 = (p3[0] - p2[0], p3[1] - p2[1])
    dot = v1[0] * v2[0] + v1[1] * v2[1]
    det = v1[0] * v2[1] - v1[1] * v2[0]
    return math.degrees(math.atan2(det, dot))

def euclidean_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

if __name__ == '__main__':
    points = load_points('X:\coordinates3.txt')
    route = nearest_neighbor_tsp(points)
    plot_points_and_route(points, route)
