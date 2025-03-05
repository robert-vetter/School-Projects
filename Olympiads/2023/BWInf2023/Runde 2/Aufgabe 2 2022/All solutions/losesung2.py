import math
import matplotlib.pyplot as plt

def read_points(filename):
    with open(filename) as f:
        points = []
        for line in f:
            x, y = map(float, line.split())
            points.append((x, y))
    return points

def greedy_route(points):
    path = [0]
    current = 0
    angle = None
    for i in range(1, len(points)):
        # Berechne den Winkel
        dx = points[i][0] - points[current][0]
        dy = points[i][1] - points[current][1]
        new_angle = math.atan2(dy, dx)
        # Überprüfen Sie, ob der Winkel kleiner als 90 Grad ist
        if angle is None or new_angle - angle >= math.pi / 2:
            angle = new_angle
            current = i
            path.append(current)
    return path

def plot_route(points, path):
    x = [points[i][0] for i in path]
    y = [points[i][1] for i in path]
    plt.plot(x, y)
    plt.show()

def main():
    points = read_points("X:\coordinates1.txt")
    path = greedy_route(points)
    plot_route(points, path)

if __name__ == "__main__":
    main()





