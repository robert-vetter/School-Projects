# Bibliotheken importieren
import os
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from shapely.geometry import Polygon, Point
import numpy as np
import math
from matplotlib.patches import Circle
from PIL import Image
import time

# Einlesen der Koordinaten
def read_coordinates(file):
    with open(file, "r") as f:
        lines = f.readlines()
        coordinates = []
        for line in lines[1:]:
            x, y = map(float, line.strip().split())
            coordinates.append((x, y))
    return coordinates

# Liste, die alle Städte speichert
all_inserted_points = []

'''Hilfsfunktionen'''
def euclidean_distance(point1, point2):
    return ((point1.x - point2.x)**2 + (point1.y - point2.y)**2)**0.5

def get_grid_cell(point, grid_size):
    return (int(point.x // grid_size), int(point.y // grid_size))

# welche Punkte liegen innerhalb des Polygons?
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

# Anzahl Städte innerhalb eines Radius einer Stadt
def count_cities_in_circle(center, crosses, polygon, radius=85):
    if not polygon.contains(Point(center)):
        return 0
    count = 0
    for cross in crosses:
        if np.linalg.norm(np.array(center) - np.array([cross[0], cross[1]])) <= radius:
            count += 1
    return count

# minimale und maximale x- und y-Koordinaten des Polygons
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

'''Visualisierung'''
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


'''Definiert Partikel mit Verhaltensregeln basierend auf physikalischen "Kräften"'''
class Particle:
    def __init__(self, position, polygon_coordinates, target, min_distance=10):
        self.polygon = Polygon(polygon_coordinates)  # Polygon-Objekt für Grenzen
        self.position = np.array(position)  # Startposition
        self.velocity = np.random.randn(2) * 0.1
        self.min_distance = min_distance  # Mindestabstand zu anderen Partikeln

    # Update-Methode zur Berechnung neuer Position basierend auf Kräften
    def update(self, particles, target, w=0.5, c1=0.7, c2=0.5, max_velocity=2, lateral_factor=1.5):
        r1, r2, r3 = np.random.rand(3)
        direction_to_target = target - self.position
        lateral_direction = np.array([-direction_to_target[1], direction_to_target[0]])
        lateral_movement = lateral_factor * r3 * lateral_direction

        # Neuberechnung der Geschwindigkeit unter Berücksichtigung der verschiedenen Kräfte
        new_velocity = (w * self.velocity +
                        c1 * r1 * direction_to_target +
                        c2 * r2 * direction_to_target +
                        lateral_movement)

        # Repulsion von anderen Partikeln
        for other in particles:
            if other != self:
                distance = np.linalg.norm(other.position - self.position)
                if distance < self.min_distance:
                    repulsion = (self.position - other.position) / distance**2
                    new_velocity += repulsion * 0.1

        # Geschwindigkeitsbegrenzung
        if np.linalg.norm(new_velocity) > max_velocity:
            new_velocity = new_velocity / np.linalg.norm(new_velocity) * max_velocity

        # Berechnung der neuen Position
        new_position = self.position + new_velocity
        if not self.polygon.contains(Point(new_position)):
            return

        # Überprüfung auf zu nahe Nachbarn
        for other in particles:
            if other != self and np.linalg.norm(new_position - other.position) < self.min_distance:
                return

        # Aktualisierung von Position und Geschwindigkeit
        self.position = new_position
        self.velocity = new_velocity

'''Klasse, die eine Gruppe von Partikeln verwaltet und das Verhalten steuert'''
class ParticleSwarm:
    def __init__(self, all_inserted_points, polygon_coordinates, min_distance=10, target=None):
        self.polygon_coordinates = polygon_coordinates  # Polygon für Partikelbegrenzung
        self.polygon = Polygon(polygon_coordinates)
        self.target = target or self.calculate_center_of_mass(all_inserted_points)  # Zielzentrum
        self.particles = [Particle(point, polygon_coordinates, self.target, min_distance) for point in all_inserted_points]

    # Berechnung des Schwerpunkts der Punkte
    @staticmethod
    def calculate_center_of_mass(points):
        x_coords = [p[0] for p in points]
        y_coords = [p[1] for p in points]
        center_x = sum(x_coords) / len(points)
        center_y = sum(y_coords) / len(points)
        return np.array([center_x, center_y])

    # Ausführung der Simulation
    def run(self, iterations=1000):
        for _ in range(iterations):
            for p in self.particles:
                p.update(self.particles, self.target)

        final_positions = [p.position for p in self.particles]
        return final_positions

'''Platzierung der Städte'''
# erzeugt hexagonales Gitter, auf welchem die Städte liegen
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
    
def save_image(coordinates, points, radius=10):
    """Zeichnet das Polygon und die Punkte in einer Bilddatei."""
    filename = "process.png"
    polygon = Polygon(coordinates)
    x, y = polygon.exterior.xy

    plt.figure()
    bounds = get_bounds_polygon(coordinates)
    plt.xlim(bounds[0], bounds[1])
    plt.ylim(bounds[2], bounds[3])
    plt.fill(x, y, alpha=1, color='black')  # Polygon füllen

    for p in points:
        circle = Circle((p[0], p[1]), radius, color='white', alpha=1)
        plt.gca().add_patch(circle)  # Kreise für Punkte zeichnen

    plt.gca().set_axis_off()
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)
    plt.savefig(filename)
    plt.close()

def find_black_pixel_and_place_city(image_path, plot_x_range, plot_y_range, x_min, y_min, last_position, tolerance=10):
    """Sucht den nächsten nicht-weißen Pixel und konvertiert ihn in Koordinaten."""
    with Image.open(image_path) as img:
        pixels = img.load()
        x_scale = plot_x_range / img.width
        y_scale = plot_y_range / img.height
        last_x, last_y = last_position

        for y in range(last_y, img.height):
            for x in range(last_x if y == last_y else 0, img.width):
                r, g, b = pixels[x, y][:3]
                if not all(255 - tolerance <= channel <= 255 for channel in (r, g, b)):
                    scaled_x = x * x_scale + x_min
                    scaled_y = (img.height - y) * y_scale + y_min
                    return Point(scaled_x, scaled_y), (x, y)
            last_x = 0

    return None, (last_x, last_y)

def process_and_save_image(coordinates, points, last_position=(0, 0), radius=10):
    """Verarbeitet die Bilddatei zur Platzierung neuer Punkte und aktualisiert das Bild."""
    min_x, max_x, min_y, max_y = get_bounds_polygon(coordinates)
    plot_x_range = abs(max_x - min_x)
    plot_y_range = abs(max_y - min_y)

    save_image(coordinates, points, radius)  # Bild mit aktuellen Punkten speichern
    new_pixel, new_position = find_black_pixel_and_place_city("process.png", plot_x_range, plot_y_range, min_x, min_y, last_position)
    
    if new_pixel:  # Wenn ein neuer Punkt gefunden wurde
        points.append((new_pixel.x, new_pixel.y))  # Neuen Punkt zur Liste hinzufügen
        save_image(coordinates, points, radius)  # Bild aktualisieren
        return True, new_position
    return False, last_position



def grid_find_center(crosses, polygon, grid_size, radius=85):
    """Sucht das Zentrum mit der höchsten Dichte von Städten innerhalb eines gegebenen Radius über ein Raster"""
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
    """Passt das Zentrum an, um die höchste Anzahl von Städten in einem Kreis zu maximieren"""
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
    """Filtert Städte, die außerhalb eines bestimmten Radius um das Zentrum liegen"""
    center = Point(center_coords)
    outside_cities = []

    for city in all_cities:
        city_point = Point(city)
        if city_point.distance(center) > 85:
            outside_cities.append(city)

    return outside_cities

def find_nearest_outside_points(cities_inside, cities_outside, min_distance=20):
    """Ermittelt für jede Stadt innerhalb des Centers (Gesundheitszentrum) den nächsten Punkt außerhalb, unter Beachtung des Mindestabstands"""
    selected_points = []

    def distance(p1, p2):
        return np.linalg.norm(np.array(p1) - np.array(p2))

    def is_valid_point(point, points, min_distance):
        return all(distance(point, other) >= min_distance for other in points)

    for city_in in cities_inside:
        nearest_point = None
        min_dist = float('inf')

        for city_out in cities_outside:
            dist = distance(city_in, city_out)
            if dist < min_dist:
                min_dist = dist
                nearest_point = city_out

        if nearest_point and is_valid_point(nearest_point, selected_points, min_distance):
            selected_points.append(nearest_point)

    return selected_points

# Hauptmethode
if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(current_directory, 'siedler1.txt')
    coordinates = read_coordinates(file)
    polygon = Polygon(coordinates)

    start = time.time()

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

        last_position = (0, 0)
        points_added = True
        while points_added:
            points_added, last_position = process_and_save_image(coordinates, all_inserted_points, last_position)
            if points_added:
                print(f"Neue Stadt hinzugefügt (Abstand 10km), aktuelle Anzahl: {len(all_inserted_points)}")

            
    best_center = grid_find_center(all_inserted_points, polygon, 2)
    best_center = find_optimal_center(all_inserted_points, best_center, polygon)

    all_inserted_points = [tuple(point) for point in all_inserted_points]

    cities_outside = find_cities_outside_center(all_inserted_points, best_center)
    cities_inside = []
    for city in all_inserted_points:
        if tuple(city) not in cities_outside:
            cities_inside.append(city)
    cities_direkt_am_kreisrand = find_nearest_outside_points(cities_inside, cities_outside)

    all_cities = cities_inside + cities_direkt_am_kreisrand

    last_position = (0, 0)
    points_added = True
    while points_added:
        points_added, last_position = process_and_save_image(coordinates, all_cities, last_position, radius=20)
        if points_added:
            print(f"Neue Stadt hinzugefügt (Abstand 20km), aktuelle Anzahl: {len(all_cities)}")

    print(f"Finale Anzahl an Städten: {len(all_cities)}")
    end = time.time()
    print("Vergangene Zeit: ", end - start, " Sekunden")



    visualise_polygon(coordinates, all_cities, best_center)
