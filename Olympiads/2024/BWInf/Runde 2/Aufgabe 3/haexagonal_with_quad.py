import os
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from shapely.geometry import Polygon, Point
import numpy as np
import time
import random
import math
from shapely.ops import nearest_points
from shapely.geometry import LineString
from matplotlib.patches import Polygon as MplPolygon
from matplotlib.animation import FuncAnimation


all_inserted_points = []

def euclidean_distance(point1, point2):
    if isinstance(point1, tuple):
        x1, y1 = point1
    else:
        x1, y1 = point1.x, point1.y

    if isinstance(point2, tuple):
        x2, y2 = point2
    else:
        x2, y2 = point2.x, point2.y

    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def get_points_on_edge(edge, min_distance, all_inserted_points):
    """Generate points along an edge at intervals of min_distance, avoiding overlaps."""
    edge_length = edge.length
    points = []
    dist = 0
    while dist < edge_length:
        point = edge.interpolate(dist)
        if is_valid_edge_point(point, min_distance, all_inserted_points):
            points.append(point)
        # Move to the next point at min_distance interval
        dist += min_distance
    return points

def is_valid_edge_point(point, min_distance, all_inserted_points):
    """Check if a point is valid considering the minimum distance from other points."""
    for other_point in all_inserted_points:
        if euclidean_distance(point, other_point) < min_distance:
            return False
    return True

def place_points_on_vertices_and_edges_maximized(polygon, min_distance):
    """Place points on the vertices and as many points as possible on the edges of a polygon, considering the min_distance."""
    all_inserted_points.clear()
    
    # Add points at each vertex of the polygon
    for vertex in polygon.exterior.coords[:-1]:  # Exclude the last point as it's the same as the first
        vertex_point = Point(vertex)
        if is_valid_edge_point(vertex_point, min_distance, all_inserted_points):
            all_inserted_points.append(vertex_point)

    # Now place points on the edges
    for i in range(len(polygon.exterior.coords) - 1):
        edge = LineString([polygon.exterior.coords[i], polygon.exterior.coords[i + 1]])
        edge_points = get_points_on_edge(edge, min_distance, all_inserted_points)
        all_inserted_points.extend(edge_points)

def is_point_valid_for_new_circle(point, radius, existing_circles, polygon):
    new_circle = Point(point.x, point.y).buffer(radius)
    if not polygon.contains(new_circle):
        return False
    
    for circle in existing_circles:
        existing_circle_point = Point(circle.x, circle.y)
        if 2 * existing_circle_point.distance(new_circle) < 2 * radius:
            return False
    return True

def add_circle_at_intersection(circle1, circle2, radius, existing_circles, polygon):
    intersection_coords = get_intersections(circle1.x, circle1.y, circle2.x, circle2.y, radius)
    valid_points = []

    if intersection_coords:
        for coord in intersection_coords:
            point = Point(coord[0], coord[1])
            if is_point_valid_for_new_circle(point, radius, existing_circles, polygon):
                valid_points.append(point)
    
    return valid_points


def get_intersections(x0, y0, x1, y1, radius):
    """Calculate the intersection points of two circles with the same radius."""
    radius *= 2
    d = math.sqrt((x1 - x0)**2 + (y1 - y0)**2)

    # Non-intersecting circles or one circle within the other
    if d > 2 * radius or d == 0:
        return None
    else:
        a = (radius**2 - radius**2 + d**2) / (2 * d)
        h = math.sqrt(radius**2 - a**2)
        x2 = x0 + a * (x1 - x0) / d   
        y2 = y0 + a * (y1 - y0) / d   
        x3 = x2 + h * (y1 - y0) / d     
        y3 = y2 - h * (x1 - x0) / d 

        x4 = x2 - h * (y1 - y0) / d
        y4 = y2 + h * (x1 - x0) / d
        
        return ((x3, y3), (x4, y4))

def get_circles_in_proximity(circle, existing_circles, proximity_radius=20):
    return [c for c in existing_circles if euclidean_distance(circle, c) <= proximity_radius]


def fill_polygon_with_circles(polygon, radius, start_circle):
    all_inserted_points.append(start_circle)  # Starting with the first circle

    new_circles_added = True

    while new_circles_added:
        new_circles_added = False
        for circle in all_inserted_points:
            proximal_circles = get_circles_in_proximity(circle, all_inserted_points, 20)

            for proximal_circle in proximal_circles:
                new_circle_points = add_circle_at_intersection(circle, proximal_circle, radius, all_inserted_points, polygon)
                if new_circle_points:
                    all_inserted_points.extend(new_circle_points)
                    print(len(all_inserted_points))
                    new_circles_added = True
                    break

            if new_circles_added:
                break  # Restart the outer loop since all_inserted_points has been updated

    return all_inserted_points

class Particle:
    def __init__(self, position, polygon_coordinates, target, min_distance=10):
        self.polygon = Polygon(polygon_coordinates)
        self.position = np.array(position)
        self.velocity = np.random.randn(2) * 0.1
        self.min_distance = min_distance

    def update(self, particles, target, w=0.5, c1=0.5, c2=0.5, max_velocity=2, lateral_factor=0.9):
        r1, r2, r3 = np.random.rand(3)
        direction_to_target = target - self.position
        lateral_direction = np.array([-direction_to_target[1], direction_to_target[0]])  # Perpendicular to the direction to target
        lateral_movement = lateral_factor * r3 * lateral_direction

        new_velocity = (w * self.velocity +
                        c1 * r1 * direction_to_target +
                        c2 * r2 * direction_to_target +
                        lateral_movement)

        # Apply repulsion from other particles if they are too close
        for other in particles:
            if other != self:
                distance = np.linalg.norm(other.position - self.position)
                if distance < self.min_distance:
                    repulsion = (self.position - other.position) / distance**2
                    new_velocity += repulsion * 0.1  # Adjust repulsion strength as needed

        # Limiting the velocity to max_velocity
        if np.linalg.norm(new_velocity) > max_velocity:
            new_velocity = new_velocity / np.linalg.norm(new_velocity) * max_velocity

        # Predict new position
        new_position = self.position + new_velocity

        if not self.polygon.contains(Point(new_position)):
            return  # Skip the update if outside the polygon

        # Check if the new position is too close to any other particle
        for other in particles:
            if other != self and np.linalg.norm(new_position - other.position) < self.min_distance:
                return  # Skip the update if too close

        # Update position and velocity
        self.position = new_position
        self.velocity = new_velocity


class ParticleSwarm:
    def __init__(self, all_inserted_points, polygon_coordinates, min_distance=10):
        self.polygon_coordinates = polygon_coordinates
        self.polygon = Polygon(polygon_coordinates)
        self.particles = [Particle(point, polygon_coordinates, None, min_distance) for point in all_inserted_points]
        self.target = self.calculate_center_of_mass(all_inserted_points)

    @staticmethod
    def calculate_center_of_mass(points):
        x_coords = [p[0] for p in points]
        y_coords = [p[1] for p in points]
        center_x = sum(x_coords) / len(points)
        center_y = sum(y_coords) / len(points)
        return np.array([center_x, center_y])

    def run_optimization(self, iterations=80):
        for _ in range(iterations):
            for particle in self.particles:
                particle.update(self.particles, self.target)

    def visualize(self):
        fig, ax = plt.subplots()
        polygon_patch = MplPolygon(self.polygon_coordinates, fill=None, edgecolor='green')
        ax.add_patch(polygon_patch)

        ax.scatter([p.position[0] for p in self.particles], 
                   [p.position[1] for p in self.particles], 
                   color='blue')
        ax.scatter(*self.target, color='red', s=100, label='Target')
        ax.legend()
        plt.show()


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

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(current_directory, 'siedler2.txt')
    coordinates = read_coordinates(file)
    polygon = Polygon(coordinates)

    min_distance = 10
    place_points_on_vertices_and_edges_maximized(polygon, min_distance)
    start_circle = Point(coordinates[0])
    _ = fill_polygon_with_circles(polygon, min_distance / 2, start_circle)

    all_inserted_points_tuples = [(point.x, point.y) for point in all_inserted_points]

    ps = ParticleSwarm(all_inserted_points_tuples, coordinates)
    ps.run_optimization()  # Run the optimization process
    ps.visualize() 
    
    # visualise_polygon(coordinates, all_inserted_points, circle_radius=min_distance / 2)
