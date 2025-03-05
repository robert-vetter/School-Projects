import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
from shapely.geometry import Point, Polygon
from matplotlib.patches import Polygon as MplPolygon
import os

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


    def update(self, particles, target, w=0.5, c1=0.5, c2=0.5, max_velocity=2, lateral_factor=0.5):
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
    def __init__(self, all_inserted_points, target, polygon_coordinates, min_distance=10):
        self.polygon_coordinates = polygon_coordinates
        self.polygon = Polygon(polygon_coordinates)
        self.particles = [Particle(point, polygon_coordinates, target, min_distance) for point in all_inserted_points]
        self.target = target

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

# coordinates = [(0, 0), (100, 0), (100, 100), (0, 100)]
current_directory = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(current_directory, 'siedler1.txt')
coordinates = read_coordinates(file)
all_inserted_points = [(50, 2), (30, 2), (50, 30)]
num_particles = len(all_inserted_points)
target = np.array([50, 50])

ps = ParticleSwarm(all_inserted_points, target, coordinates)
ps.animate()
