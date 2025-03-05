# weitere Ideen: Anordnung als gleichseitige Dreiecke
# ToDo: verbleibenden Punkte außerhalb des Kreises selektieren

'''
Algorithms:
Hexagonales Gitter drüberlegen
https://stackoverflow.com/questions/11178414/algorithm-to-generate-equally-distributed-points-in-a-polygon
1 Dart Throwing
Put rectangle around polygon, think about optimal configuration of point sinside rectangle (easier), just drop points that fall outside polygon
Split up in triangles using delaunay
Improvement: https://www.math.uwaterloo.ca/~ervrscay/talks/Jiang-AMMCS-CAIMS-2015.pdf (Jiggling)
Spiral packing also possible
'''

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
        plt.scatter([p.x for p in points], [p.y for p in points], color='red', marker='x')
        for p in points:
            circlePoints = Circle([p.x, p.y], 10, color='black', alpha = 0.05)
            plt.gca().add_patch(circlePoints)

    if circle_center and circle_radius:
        plt.scatter(circle_center[0], circle_center[1], color='green', marker='o')
        circle = Circle(circle_center, circle_radius, color='blue', fill=False)
        plt.gca().add_patch(circle)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('equal')
    plt.show()

class QuadTreeNode:
    def __init__(self, boundary, capacity):
        self.boundary = boundary
        self.capacity = capacity
        self.points = []
        self.divided = False

    def subdivide(self):
        x_min, y_min, x_max, y_max = self.boundary.bounds
        mid_x, mid_y = (x_min + x_max) / 2, (y_min + y_max) / 2

        nw = Polygon([(x_min, y_min), (mid_x, y_min), (mid_x, mid_y), (x_min, mid_y)])
        ne = Polygon([(mid_x, y_min), (x_max, y_min), (x_max, mid_y), (mid_x, mid_y)])
        sw = Polygon([(x_min, mid_y), (mid_x, mid_y), (mid_x, y_max), (x_min, y_max)])
        se = Polygon([(mid_x, mid_y), (x_max, mid_y), (x_max, y_max), (mid_x, y_max)])

        self.northwest = QuadTreeNode(nw, self.capacity)
        self.northeast = QuadTreeNode(ne, self.capacity)
        self.southwest = QuadTreeNode(sw, self.capacity)
        self.southeast = QuadTreeNode(se, self.capacity)
        self.divided = True


    def insert(self, point):
        if not self.boundary.contains(point):
            return False

        if len(self.points) < self.capacity:
            self.points.append(point)
            return True
        else:
            if not self.divided:
                self.subdivide()

            if self.northeast.insert(point):
                return True
            elif self.northwest.insert(point):
                return True
            elif self.southeast.insert(point):
                return True
            elif self.southwest.insert(point):
                return True

        return False
    

def insert_points_quadtree(polygon, min_distance, capacity=4):
    root = QuadTreeNode(polygon, capacity)
    grid = {}
    grid_size = min_distance / 2

    for x in range(int(polygon.bounds[0]), int(polygon.bounds[2]) + 1):
        for y in range(int(polygon.bounds[1]), int(polygon.bounds[3]) + 1):
            point = Point(x, y)
            if polygon.contains(point) and is_valid_point(point, min_distance, grid, grid_size):
                if root.insert(point):
                    cell = get_grid_cell(point, grid_size)
                    if cell not in grid:
                        grid[cell] = []
                    grid[cell].append(point)
                    all_inserted_points.append(point)
    return root



def save_image(coordinates, points):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(current_directory, "process.png")
    
    polygon = Polygon(coordinates)
    x, y = polygon.exterior.xy

    plt.figure()
    bounds = get_bounds_polygon(coordinates)
    plt.xlim(bounds[0], bounds[1])
    plt.ylim(bounds[2], bounds[3])

    plt.fill(x, y, alpha=1, color='black')
    for p in points:
        circle = Circle((p.x, p.y), 10, color='white', alpha=1)
        plt.gca().add_patch(circle)

    plt.gca().set_axis_off()
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)

    plt.savefig(filename)
    plt.close()




def find_black_pixel_and_place_city(image_path, plot_x_range, plot_y_range, x_min, y_min, last_position, tolerance=10):
    with Image.open(image_path) as img:
        pixels = img.load()

        x_scale = plot_x_range / img.width
        y_scale = plot_y_range / img.height

        last_x, last_y = last_position

        for y in range(last_y, img.height):
            for x in range(last_x if y == last_y else 0, img.width):
                r, g, b = pixels[x, y][:3]
                if not all(255 - tolerance <= channel <= 255 for channel in (r, g, b)):

                    a = x / img.width
                    scaled_x = a * plot_x_range + x_min

                    b = y / img.height
                    scaled_y = b * plot_y_range
                    return Point(scaled_x, scaled_y), (x, y)
            last_x = 0

    return None, (last_x, last_y)



def process_and_save_image(coordinates, points, filename, last_position=(0, 0)):
    min_x, max_x, min_y, max_y = get_bounds_polygon(coordinates)
    plot_x_range = abs(max_x-min_x)
    plot_y_range = abs(max_y-min_y)
    new_pixel, new_position = find_black_pixel_and_place_city(filename, plot_x_range, plot_y_range, min_x, min_y, last_position)
    polygon = Polygon(coordinates)
    if new_pixel:
        transformed_y = max_y - new_pixel.y - 1
        
        transformed_pixel = Point(new_pixel.x, transformed_y)
        
        points.append(transformed_pixel)
        save_image(coordinates, points)
        return True, new_position
    return False, last_position


def grid_find_center(crosses, polygon, grid_size, radius=85):
    min_x, max_x, min_y, max_y = get_bounds(crosses)

    best_center = None
    max_count = 0

    for x in np.arange(min_x, max_x, grid_size):
        for y in np.arange(min_y, max_y, grid_size):
            if polygon.contains(Point(x, y)):
                count = count_crosses_in_circle((x, y), crosses, polygon, radius)
                if count > max_count:
                    max_count = count
                    best_center = (x, y)

    return best_center



def find_optimal_center(crosses, initial_center, polygon, radius=85):
    step_size = 2
    center = initial_center
    max_count = count_crosses_in_circle(center, crosses, polygon, radius)

    def adjust_center(center, crosses, polygon, step_size, radius=85):
        best_center = center
        max_count = count_crosses_in_circle(center, crosses, polygon, radius)

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            new_center = (center[0] + dx * step_size, center[1] + dy * step_size)
            if polygon.contains(Point(new_center)):
                count = count_crosses_in_circle(new_center, crosses, polygon, radius)
                if count > max_count:
                    max_count = count
                    best_center = new_center

        return best_center, max_count

    while True:
        new_center, new_count = adjust_center(center, crosses, polygon, step_size, radius)
        if new_count <= max_count:
            break
        center, max_count = new_center, new_count

    return center

def find_cities_outside_center(all_cities, center_coords):
    center = Point(center_coords)
    outside_cities = []

    for city in all_cities:
        city_point = Point(city)
        if city_point.distance(center) > 85:
            outside_cities.append(city)

    return outside_cities

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(current_directory, 'siedler2.txt')
    coordinates = read_coordinates(file)
    polygon = Polygon(coordinates)


    min_distance = 10
    grid_size = 2

    start = time.time()
    quadtree_root = insert_points_quadtree(polygon, min_distance)
    
    save_image(coordinates, all_inserted_points)
    
    
    last_position = (0, 0)
    while True:
        result, last_position = process_and_save_image(coordinates, all_inserted_points, os.path.join(current_directory, 'process.png'), last_position)
        if not result:
            break

    
    best_center = grid_find_center(all_inserted_points, polygon, grid_size)
    best_center = find_optimal_center(all_inserted_points, best_center, polygon)

    cities_outside = find_cities_outside_center(all_inserted_points, best_center)
    
    end = time.time()
    print("Anzahl der Städte: ", len(all_inserted_points))
    print("Benötigte Zeit: ", round(end-start, 2), " Sekunden")

    visualise_polygon(coordinates, all_inserted_points, best_center)






