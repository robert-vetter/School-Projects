import os
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from shapely.geometry import Polygon, Point
import numpy as np
import time
import random
from PIL import Image
from scipy.spatial import Voronoi, voronoi_plot_2d
import math
from shapely.ops import nearest_points


all_inserted_points = []

def euclidean_distance(point1, point2):
    return ((point1.x - point2.x)**2 + (point1.y - point2.y)**2)**0.5

def calculate_total_distance(cities):
    total_distance = 0
    num_cities = len(cities)

    for i in range(num_cities):
        min_distance = float('inf')
        for j in range(num_cities):
            if i != j:
                distance = euclidean_distance(cities[i], cities[j])
                min_distance = min(min_distance, distance)
        total_distance += min_distance

    return total_distance

def get_grid_cell(point, grid_size):
    return (int(point.x // grid_size), int(point.y // grid_size))

def is_valid_point(point, min_distance, grid, grid_size):
    cell = get_grid_cell(point, grid_size)
    search_radius = 2
    adjacent_cells = [(x, y) for x in range(cell[0] - search_radius, cell[0] + search_radius + 1)
                              for y in range(cell[1] - search_radius, cell[1] + search_radius + 1)]

    for c in adjacent_cells:
        if c in grid:
            for other_point in grid[c]:
                if point.distance(other_point) < min_distance:
                    return False
    return True

def count_crosses_in_circle(center, crosses, polygon, radius=85):
    if not polygon.contains(Point(center)):
        return 0
    count = 0
    for cross in crosses:
        if np.linalg.norm(np.array(center) - np.array((cross.x, cross.y))) <= radius:
            count += 1
    return count

def get_bounds(points):
    min_x = min(p.x for p in points)
    max_x = max(p.x for p in points)
    min_y = min(p.y for p in points)
    max_y = max(p.y for p in points)
    return min_x, max_x, min_y, max_y

def get_bounds_polygon(points):
    min_x = min(p[0] for p in points)  # Erhalte das Minimum von x
    max_x = max(p[0] for p in points)  # Erhalte das Maximum von x
    min_y = min(p[1] for p in points)  # Erhalte das Minimum von y
    max_y = max(p[1] for p in points)  # Erhalte das Maximum von y
    return min_x, max_x, min_y, max_y

# Einlesen der Koordinaten
def read_coordinates(file):
    with open(file, "r") as f:
        lines = f.readlines()
        num_points = int(lines[0].strip())
        coordinates = []
        for line in lines[1:]:
            x, y = map(float, line.strip().split())
            coordinates.append((x, y))
    return coordinates


def visualise_polygon(coordinates, points=[], circle_center=None, circle_radius=85):
    polygon = Polygon(coordinates)
    x, y = polygon.exterior.xy

    plt.figure()
    plt.fill(x, y, alpha=0.4, color='green')
    plt.scatter(*zip(*coordinates), color='black', marker='o')

    if points:
        plt.scatter([p[0] for p in points], [p[1] for p in points], color='red', marker='x')
        for p in points:
            circlePoints = Circle((p[0], p[1]), 10, color='black', alpha=0.05)  # Corrected here
            plt.gca().add_patch(circlePoints)

    if circle_center and circle_radius:
        plt.scatter(circle_center[0], circle_center[1], color='green', marker='o')
        circle = Circle(circle_center, circle_radius, color='blue', fill=False)
        plt.gca().add_patch(circle)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('equal')
    plt.show()

def generate_hexagonal_grid(bounds, side_length, offset):
    min_x, max_x, min_y, max_y = bounds
    vertical_distance = math.sqrt(3) / 2 * side_length  # Vertical distance between rows

    points = []
    y = min_y - offset[1]
    while y <= max_y:
        x_offset = (0 if (round(y / vertical_distance) % 2 == 0) else side_length / 2) - offset[0]
        x = min_x + x_offset
        while x <= max_x:
            points.append((x, y))
            x += side_length
        y += vertical_distance

    return points

def filter_points_inside_polygon(points, polygon):
    return [p for p in points if polygon.contains(Point(p[0], p[1]))]



if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(current_directory, 'siedler2.txt')
    coordinates = read_coordinates(file)
    polygon = Polygon(coordinates)

    side_length = 10  # Side length of the hexagon
    bounds = get_bounds_polygon(coordinates)

    max_points_inside = 0
    best_grid = None

    for vertex in coordinates:
        hexagonal_grid = generate_hexagonal_grid(bounds, side_length, vertex)
        points_inside_polygon = filter_points_inside_polygon(hexagonal_grid, polygon)

        if len(points_inside_polygon) > max_points_inside:
            max_points_inside = len(points_inside_polygon)
            best_grid = points_inside_polygon

    print("Anzahl der Städte: ", max_points_inside)

    visualise_polygon(coordinates, best_grid)