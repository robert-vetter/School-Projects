import os
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from shapely.geometry import Polygon, Point
import numpy as np
import time
import random

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

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(current_directory, 'siedler5.txt')
    coordinates = read_coordinates(file)
    polygon = Polygon(coordinates)
    
    min_distance = 10
    grid_size = 2

    start = time.time()
    quadtree_root = insert_points_quadtree(polygon, min_distance)

    
    best_center = grid_find_center(all_inserted_points, polygon, grid_size)
    best_center = find_optimal_center(all_inserted_points, best_center, polygon)

    end = time.time()
    print("Anzahl der Städte: ", len(all_inserted_points))
    print("Benötigte Zeit: ", round(end-start, 2), " Sekunden")
    visualise_polygon(coordinates, all_inserted_points, best_center)














# population_size = 100
    # generations = 200
    # mutation_rate = 0.1
    # all_inserted_points = run_genetic_algorithm(all_inserted_points, population_size, generations, mutation_rate)
# Optimierung der gefundenen Punkte - macht eigentlich keinen Unterschied
def create_initial_population(all_points, population_size, mutation_rate):
    population = [all_points.copy() for _ in range(population_size)]
    for individual in population:
        if random.random() < mutation_rate:
            mutate(individual)
    return population

def fitness(individual):
    return len(individual)

def select(population):
    population.sort(key=fitness, reverse=True)
    return population[:len(population)//2]

def crossover(parent1, parent2):
    cut = random.randint(0, len(parent1))
    child = parent1[:cut] + parent2[cut:]
    return child

def mutate(individual):
    mutation_type = random.choice(['add', 'remove', 'move'])
    if mutation_type == 'add':
        pass
    elif mutation_type == 'remove':
        if individual:
            individual.pop(random.randint(0, len(individual) - 1))
    elif mutation_type == 'move':
        if individual:
            idx = random.randint(0, len(individual) - 1)
            individual[idx] = move_point(individual[idx])
    return individual

def move_point(point):
    return point

def run_genetic_algorithm(all_points, population_size, generations, mutation_rate):
    population = create_initial_population(all_points, population_size, mutation_rate)

    for _ in range(generations):
        selected = select(population)
        offspring = []
        while len(offspring) < population_size:
            parent1, parent2 = random.sample(selected, 2)
            child = crossover(parent1, parent2)
            if random.random() < mutation_rate:
                child = mutate(child)
            offspring.append(child)
        population = offspring

    best_solution = max(population, key=fitness)
    return best_solution


def move_point_closer(point1, point2, step_size, min_distance, grid, grid_size):
    direction = Point(point2.x - point1.x, point2.y - point1.y)
    direction_length = euclidean_distance(point1, point2)
    if direction_length == 0 or direction_length <= min_distance:
        return point1  # Either overlapping or too close to move

    # Normalize direction and calculate new position
    normalized_direction = Point(direction.x / direction_length, direction.y / direction_length)
    new_position = Point(point1.x + normalized_direction.x * step_size, 
                         point1.y + normalized_direction.y * step_size)

    if is_valid_point(new_position, min_distance, grid, grid_size):
        return new_position
    return point1

def improve_distances(cities, iterations, step_size, min_distance, grid_size):
    grid = {}

    # Populate the initial grid
    for city in cities:
        cell = get_grid_cell(city, grid_size)
        if cell not in grid:
            grid[cell] = []
        grid[cell].append(city)

    for _ in range(iterations):
        city_index = random.randint(0, len(cities) - 1)
        closest_city_index = min(range(len(cities)), key=lambda i: euclidean_distance(cities[city_index], cities[i]) if i != city_index else float('inf'))

        # Move the city closer to its nearest neighbor, respecting minimum distance
        new_position = move_point_closer(cities[city_index], cities[closest_city_index], step_size, min_distance, grid, grid_size)

        # Update the grid
        if new_position != cities[city_index]:
            old_cell = get_grid_cell(cities[city_index], grid_size)
            new_cell = get_grid_cell(new_position, grid_size)
            grid[old_cell].remove(cities[city_index])
            if new_cell not in grid:
                grid[new_cell] = []
            grid[new_cell].append(new_position)
            cities[city_index] = new_position

    return cities
