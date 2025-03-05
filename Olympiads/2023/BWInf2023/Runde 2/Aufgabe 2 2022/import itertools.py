import numpy as np
import matplotlib.pyplot as plt
import math

def import_coordinates(file):
    # Funktion zum Importieren der Koordinaten aus der txt-Datei
    coordinates = []
    with open(file, 'r') as file:
        for line in file:
            x, y = map(float, line.split())
            coordinates.append([x, y])
    return np.array(coordinates)

def calculate_distance(p1, p2):
    # Funktion zur Berechnung der Distanz zwischen zwei Punkten
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def calculate_angle(p1, p2, p3):
    a = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    b = math.sqrt((p2[0] - p3[0])**2 + (p2[1] - p3[1])**2)
    c = math.sqrt((p1[0] - p3[0])**2 + (p1[1] - p3[1])**2)
    if a == 0 or b == 0:
        return 90
    angle = math.degrees(math.acos((a**2 + b**2 - c**2) / (2*a*b)))
    return angle

def tsp(coordinates):
    # Hauptfunktion für das TSP-Problem
    n = len(coordinates)
    route = [0]
    for i in range(1, n):
        min_distance = float('inf')
        next_point = 0
        for j in range(1, n):
            if j not in route:
                p1 = coordinates[route[-1]]
                p2 = coordinates[j]
                if calculate_distance(p1, p2) < min_distance:
                    p3 = coordinates[route[-2]] if len(route) > 1 else p1
                    angle = calculate_angle(p3, p1, p2)
                    if angle >= 90:
                        min_distance = calculate_distance(p1, p2)
                        next_point = j
        route.append(next_point)
    route.append(0)
    return route

def plot_route(coordinates, route):
    # Funktion zum Ploten der Route
    x = coordinates[:, 0]
    y = coordinates[:, 1]
    route_x = [coordinates[i][0] for i in route]
    route_y = [coordinates[i][1] for i in route]
    plt.plot(x, y, 'o')
    plt.plot(route_x, route_y, '-')
    plt.show()

if __name__ == '__main__':
    file = 'X:\coordinates4.txt'
    coordinates = import_coordinates(file)
    route = tsp(coordinates)
    plot_route(coordinates, route)








