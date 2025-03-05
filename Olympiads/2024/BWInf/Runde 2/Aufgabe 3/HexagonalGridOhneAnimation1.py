import os
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from shapely.geometry import Polygon, Point
import numpy as np
import math
from matplotlib.patches import Circle
from PIL import Image

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


all_inserted_points = []

def euclidean_distance(point1, point2):
    return ((point1.x - point2.x)**2 + (point1.y - point2.y)**2)**0.5

def get_grid_cell(point, grid_size):
    return (int(point.x // grid_size), int(point.y // grid_size))

def filter_points_inside_polygon(points, polygon):
    return [p for p in points if polygon.contains(Point(p[0], p[1]))]

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

def count_cities_in_circle(center, crosses, polygon, radius=85):
    if not polygon.contains(Point(center)):
        return 0
    count = 0
    for cross in crosses:
        if np.linalg.norm(np.array(center) - np.array([cross[0], cross[1]])) <= radius:
            count += 1
    return count

def find_extreme_points(polygon):
    min_x, min_y, max_x, max_y = polygon.bounds
    
    extreme_points = [
        min((p for p in coordinates if p[0] == min_x), key=lambda x: x[1]),
        max((p for p in coordinates if p[0] == max_x), key=lambda x: x[1]),
        min((p for p in coordinates if p[1] == min_y), key=lambda x: x[0]),
        max((p for p in coordinates if p[1] == max_y), key=lambda x: x[0])
    ]
    return extreme_points

def get_bounds_polygon(points):
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)
    return min_x, max_x, min_y, max_y


def visualise_polygon(coordinates, points=[], circle_center=None, circle_radius=85):
    polygon = Polygon(coordinates)
    x, y = polygon.exterior.xy

    plt.figure()
    plt.fill(x, y, alpha=0.4, color='green')
    plt.scatter(*zip(*coordinates), color='black', marker='o')

    if points:
        plt.scatter([p[0] for p in points], [p[1] for p in points], color='red', marker='x')
        for p in points:
            circlePoints = Circle((p[0], p[1]), 10, color='black', alpha=0.05)
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
    vertical_distance = math.sqrt(3) / 2 * side_length

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

class Particle:
    def __init__(self, position, polygon_coordinates, target, min_distance=10):
        self.polygon = Polygon(polygon_coordinates)
        self.position = np.array(position)
        self.velocity = np.random.randn(2) * 0.1
        self.min_distance = min_distance

    def update(self, particles, target, w=0.5, c1=0.7, c2=0.5, max_velocity=2, lateral_factor=1.5):
        r1, r2, r3 = np.random.rand(3)
        direction_to_target = target - self.position
        lateral_direction = np.array([-direction_to_target[1], direction_to_target[0]])
        lateral_movement = lateral_factor * r3 * lateral_direction

        new_velocity = (w * self.velocity +
                        c1 * r1 * direction_to_target +
                        c2 * r2 * direction_to_target +
                        lateral_movement)

        for other in particles:
            if other != self:
                distance = np.linalg.norm(other.position - self.position)
                if distance < self.min_distance:
                    repulsion = (self.position - other.position) / distance**2
                    new_velocity += repulsion * 0.1

        if np.linalg.norm(new_velocity) > max_velocity:
            new_velocity = new_velocity / np.linalg.norm(new_velocity) * max_velocity

        new_position = self.position + new_velocity

        if not self.polygon.contains(Point(new_position)):
            return

        for other in particles:
            if other != self and np.linalg.norm(new_position - other.position) < self.min_distance:
                return

        self.position = new_position
        self.velocity = new_velocity

class ParticleSwarm:
    def __init__(self, all_inserted_points, polygon_coordinates, min_distance=10, target=None):
        self.polygon_coordinates = polygon_coordinates
        self.polygon = Polygon(polygon_coordinates)
        if target is None:
            self.target = self.calculate_center_of_mass(all_inserted_points)
        else:
            self.target = target
        self.particles = [Particle(point, polygon_coordinates, self.target, min_distance) for point in all_inserted_points]

    @staticmethod
    def calculate_center_of_mass(points):
        x_coords = [p[0] for p in points]
        y_coords = [p[1] for p in points]
        center_x = sum(x_coords) / len(points)
        center_y = sum(y_coords) / len(points)
        return np.array([center_x, center_y])

    def run(self, iterations=1000):
        for _ in range(iterations):
            for p in self.particles:
                p.update(self.particles, self.target)
        
        final_positions = [p.position for p in self.particles]
        return final_positions


    
def create_grid(polygon, existing_points, cell_size):
    minx, miny, maxx, maxy = polygon.bounds
    width = int(np.ceil((maxx - minx) / cell_size))
    height = int(np.ceil((maxy - miny) / cell_size))
    grid = np.zeros((height, width), dtype=bool)

    # Markiere bestehende Punkte im Grid
    for point in existing_points:
        row = int((point[1] - miny) / cell_size)
        col = int((point[0] - minx) / cell_size)
        if 0 <= row < height and 0 <= col < width:
            grid[row, col] = True

    return grid, minx, miny, cell_size

def valid_point(x, y, grid, minx, miny, cell_size, polygon):
    if not polygon.contains(Point(x, y)):
        return False

    row = int((y - miny) / cell_size)
    col = int((x - minx) / cell_size)
    if not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]):
        return False

    # Überprüfe die Umgebung des Punkts im Grid
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            nr, nc = row + dy, col + dx
            if 0 <= nr < grid.shape[0] and 0 <= nc < grid.shape[1]:
                if grid[nr, nc]:
                    return False
    return True

def add_point(x, y, grid, minx, miny, cell_size):
    row = int((y - miny) / cell_size)
    col = int((x - minx) / cell_size)
    grid[row, col] = True

def place_points(polygon, existing_points, cell_size=1):
    grid, minx, miny, cell_size = create_grid(polygon, existing_points, cell_size)
    points = list(existing_points)  # Kopiere bestehende Punkte in die neue Liste
    for y in np.arange(miny, miny + grid.shape[0] * cell_size, cell_size):
        for x in np.arange(minx, minx + grid.shape[1] * cell_size, cell_size):
            if valid_point(x, y, grid, minx, miny, cell_size, polygon):
                points.append((x, y))
                add_point(x, y, grid, minx, miny, cell_size)
    return points


def grid_find_center(crosses, polygon, grid_size, radius=85):
    min_x, max_x, min_y, max_y = get_bounds_polygon(crosses)

    best_center = None
    max_count = 0

    for x in np.arange(min_x, max_x, grid_size):
        for y in np.arange(min_y, max_y, grid_size):
            if polygon.contains(Point(x, y)):
                count = count_cities_in_circle((x, y), crosses, polygon, radius)
                if count > max_count:
                    max_count = count
                    best_center = (x, y)

    return best_center

def find_optimal_center(crosses, initial_center, polygon, radius=85):
    step_size = 2
    center = initial_center
    max_count = count_cities_in_circle(center, crosses, polygon, radius)

    def adjust_center(center, crosses, polygon, step_size, radius=85):
        best_center = center
        max_count = count_cities_in_circle(center, crosses, polygon, radius)

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            new_center = (center[0] + dx * step_size, center[1] + dy * step_size)
            if polygon.contains(Point(new_center)):
                count = count_cities_in_circle(new_center, crosses, polygon, radius)
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
    file = os.path.join(current_directory, 'siedler4.txt')
    coordinates = read_coordinates(file)
    polygon = Polygon(coordinates)

    bounds = get_bounds_polygon(coordinates)
    extreme_points = find_extreme_points(polygon)

    best_grid = None
    max_points_inside = 0

    for vertex in coordinates:
        hexagonal_grid = generate_hexagonal_grid(bounds, 10, vertex)
        points_inside_polygon = filter_points_inside_polygon(hexagonal_grid, polygon)

        if len(points_inside_polygon) > max_points_inside:
            max_points_inside = len(points_inside_polygon)
            best_grid = points_inside_polygon

    all_inserted_points = best_grid

    print(f"Ursprüngliche Anzahl an Städten: {len(all_inserted_points)}")

    
    for point in extreme_points:
        particle_swarm = ParticleSwarm(all_inserted_points, coordinates, target=point)
        all_inserted_points = particle_swarm.run(iterations=50)

        all_inserted_points = place_points(coordinates, all_inserted_points)
        print(len(all_inserted_points))

            
    best_center = grid_find_center(all_inserted_points, polygon, 2)
    best_center = find_optimal_center(all_inserted_points, best_center, polygon)

    all_inserted_points = [tuple(point) for point in all_inserted_points]

    cities_outside = find_cities_outside_center(all_inserted_points, best_center)
    cities_inside = []
    for city in all_inserted_points:
        if tuple(city) not in cities_outside:
            cities_inside.append(city)

    all_cities = cities_inside


    

    print(f"Finale Anzahl an Städten: {len(all_cities)}")


    visualise_polygon(coordinates, all_cities, best_center)