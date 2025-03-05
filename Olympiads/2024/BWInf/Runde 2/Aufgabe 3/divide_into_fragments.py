import os
import concurrent.futures
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point
from shapely.strtree import STRtree
import numpy as np
import time

all_inserted_points = []

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

def visualise_polygon(coordinates, points=[]):
    polygon = Polygon(coordinates)
    x, y = polygon.exterior.xy
    plt.figure()
    plt.fill(x, y, alpha=0.4, color='green')
    plt.scatter(*zip(*coordinates), color='black', marker='o')
    if points:
        plt.scatter([p.x for p in points], [p.y for p in points], color='red', marker='x')
    plt.xlabel('x')
    plt.ylabel('y')
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

        # Create sub-quadrants
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
    
def is_valid_point(point, min_distance):
    return all(point.distance(other) >= min_distance for other in all_inserted_points)

def insert_points_quadtree(polygon, min_distance, capacity=4):
    root = QuadTreeNode(polygon, capacity)

    for x in range(int(polygon.bounds[0]), int(polygon.bounds[2]) + 1):
        for y in range(int(polygon.bounds[1]), int(polygon.bounds[3]) + 1):
            point = Point(x, y)
            if polygon.contains(point) and is_valid_point(point, min_distance):
                if root.insert(point):
                    all_inserted_points.append(point)
    return root


if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(current_directory, 'siedler5.txt')
    coordinates = read_coordinates(file)
    polygon = Polygon(coordinates)
    
    min_distance = 10

    start = time.time()
    quadtree_root = insert_points_quadtree(polygon, min_distance)

    nodes = [quadtree_root]
    while nodes:
        node = nodes.pop()
        if node.divided:
            nodes.extend([node.northeast, node.northwest, node.southeast, node.southwest])

    end = time.time()
    print("Anzahl der Städte: ", len(all_inserted_points))
    print("Benötigte Zeit: ", round(end-start, 2), " Sekunden")
    visualise_polygon(coordinates, all_inserted_points)
