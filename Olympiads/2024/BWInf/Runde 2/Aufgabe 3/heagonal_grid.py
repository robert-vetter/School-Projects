import os
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from shapely.geometry import Polygon, Point
import numpy as np
import time
import random
import math
from shapely.ops import nearest_points
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
from matplotlib.patches import Polygon as MplPolygon



all_inserted_points = []

def euclidean_distance(point1, point2):
    return ((point1.x - point2.x)**2 + (point1.y - point2.y)**2)**0.5


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


def filter_points_inside_polygon(points, polygon):
    return [p for p in points if polygon.contains(Point(p[0], p[1]))]


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
    plt.fill(x, y, alpha=0.4, color='green')  # Filling the polygon
    plt.scatter(*zip(*coordinates), color='black', marker='o')  # Polygon vertices

    if points:
        # Points inside the polygon
        plt.scatter([p[0] for p in points], [p[1] for p in points], color='red', marker='x')
        # Drawing small circles around each point
        for p in points:
            circlePoints = Circle((p[0], p[1]), 10, color='black', alpha=0.05)
            plt.gca().add_patch(circlePoints)

    if circle_center and circle_radius:
        # Optional larger circle
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


def read_coordinates(file):
    with open(file, "r") as f:
        lines = f.readlines()
        num_points = int(lines[0].strip())
        coordinates = []
        for line in lines[1:]:
            x, y = map(float, line.strip().split())
            coordinates.append((x, y))
    return coordinates

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

    def animate(self, frames=1000, interval=20):
        fig, ax = plt.subplots()
        # Plot polygon
        polygon_patch = MplPolygon(self.polygon_coordinates, fill=None, edgecolor='green')
        ax.add_patch(polygon_patch)

        scat = ax.scatter([p.position[0] for p in self.particles], 
                          [p.position[1] for p in self.particles], 
                          color='blue')

        ax.scatter(*self.target, color='red', s=100, label='Target')
        ax.legend()

        def update(frame):
            for p in self.particles:
                p.update(self.particles, self.target)
            
            scat.set_offsets([p.position for p in self.particles])
            return [scat]

        ani = FuncAnimation(fig, update, frames=frames, interval=interval, blit=True)
        plt.show()

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

    all_inserted_points = best_grid

    print(len(all_inserted_points))

    #ps = ParticleSwarm(all_inserted_points, coordinates)
    #ps.animate()

    visualise_polygon(coordinates, all_inserted_points)