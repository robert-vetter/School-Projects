import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.animation as animation
import time
import random

def read_coordinates(file):
    with open(file, "r") as f:
        lines = f.readlines()
        coordinates = []
        for line in lines:
            x, y = map(float, line.strip().split())
            coordinates.append((x, y))
    return coordinates

def calculate_distance(p1, p2):
    # Funktion zur Berechnung der Distanz zwischen zwei Punkten, Pythagoras
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def calculate_angle(p1, p2, p3):
    # p2 ist der Scheitelwinkel
    a = calculate_distance(p1, p2)
    b = calculate_distance(p2, p3)
    c = calculate_distance(p1, p3)
    if a == 0 or b == 0:
        return 90
    # Kosinussatz
    cos_angle = (a**2 + b**2 - c**2) / (2*a*b)
    
    if cos_angle > 1:
        cos_angle = 1
    elif cos_angle < -1:
        cos_angle = -1
    angle = math.degrees(math.acos(cos_angle))
    return round(angle, 2)


def route_length(coordinates):
    length = 0
    for i in range(len(coordinates) - 1):
        length += np.linalg.norm(np.array(coordinates[i]) - np.array(coordinates[i + 1]))
    return round(length, 3)

def greedy_algorithm(coordinates):
    all_routes = []
    all_visited = set(range(len(coordinates)))
    overall_best_route = []
    for start in range(len(coordinates)):
        route = [coordinates[start]]
        visited = {start}
        unvisited = all_visited - visited
        while unvisited:
            best_route = None
            best_distance = float("inf")
            for i in unvisited:
                point = coordinates[i]
                if len(route) > 1:
                    angle = calculate_angle(route[-2], route[-1], point)
                else:
                    # vom ersten Punkt kann zu jedem möglichen Punkt Kante gezogen werden
                    angle = 100
                if angle >= 90:
                    # wählt Punkt aus, der am nähesten dran ist
                    temp_distance = calculate_distance(route[-1], point)  
                    if temp_distance < best_distance:
                        best_route = route + [point]
                        best_distance = temp_distance
            if not best_route:
                break
            route = best_route
            visited.add(coordinates.index(route[-1]))
            unvisited = all_visited - visited
        if len(route) >= len(overall_best_route):
            overall_best_route = route
        all_routes.append(route)

    # sortiert Liste nach len(list) und wenn Länge gleich, dann nach route_length(list)
    def sort_all_routes(lists):
        lists.sort(key=len, reverse=True)
        result = []
        lengths = []
        for lst in lists:
            if len(lst) not in lengths:
                lengths.append(len(lst))
                result.append([lst])
            else:
                for i in range(len(result)):
                    if len(result[i][0]) == len(lst):
                        result[i].append(lst)
                        break
        for group in result:
            group.sort(key=route_length)
        return [item for sublist in result for item in sublist]
    
    all_routes = sort_all_routes(all_routes)
    return all_routes


# gibt alle verbleibenden Punkte zurück
def remaining_points(all_points, route):
    remaining = all_points[:]
    for point in route:
        if point in remaining:
            remaining.remove(point)
    return remaining

# gibt alle Routen in den verbleibenden Punkten zurück
def remaining_cluster(coordinates, route):
    remaining_cl_route = greedy_algorithm(remaining_points(coordinates, route))
    return remaining_cl_route

# checkt, ob man zwei Routen verbinden kann 
def check_for_combining(route, remaining_cl_route):
    new_route = []
    remaining_cl_route_start, remaining_cl_route_end = remaining_cl_route[0], remaining_cl_route[-1]
    cl_route_start, cl_route_end = route[0], route[-1]
    if len(remaining_cl_route) > 1:
        # Start des ursprünglichen Clusters verbindet sich mit Start des remaining_clusters
        if calculate_angle(remaining_cl_route[1], remaining_cl_route_start, cl_route_start) >= 90 and calculate_angle(route[1], cl_route_start, remaining_cl_route_start) >= 90:
            new_route += route[::-1] + remaining_cl_route
        # Start des ursprünglichen Clusters verbindet sich mit Ende des remaining_clusters
        elif calculate_angle(remaining_cl_route[-2], remaining_cl_route_end, cl_route_start) >= 90 and calculate_angle(route[1], cl_route_start, remaining_cl_route_end) >= 90:
            new_route += route[::-1] + remaining_cl_route[::-1]
        # Ende des ursprünglichen Clusters verbindet sich mit Start des remaining_clusters    
        elif calculate_angle(remaining_cl_route[1], remaining_cl_route_start, cl_route_end) >= 90 and calculate_angle(route[-2],  cl_route_end, remaining_cl_route_start) >= 90:
            new_route += route + remaining_cl_route
        # Ende des ursprünglichen Clusters verbindet sich mit Ende des remaining_clusters
        elif calculate_angle(remaining_cl_route[-2], remaining_cl_route_end, cl_route_end) >= 90 and calculate_angle(route[-2],  cl_route_end, remaining_cl_route_end) >= 90:
            new_route += route + remaining_cl_route[::-1]
        else:
            return None
    else:
        if calculate_angle(remaining_cl_route[0], cl_route_start, route[1]) >= 90:
            new_route += route[::-1] + remaining_cl_route

        elif calculate_angle(remaining_cl_route[0], cl_route_end, route[-2]) >= 90:
            new_route += route + remaining_cl_route
        else:
            return None
    return new_route

def find_complete_route(coordinates, num_routes_to_check=10):
    initial_routes = greedy_algorithm(coordinates)
    best_complete_route = None
    best_complete_route_length = float("inf")

    for initial_route in initial_routes:
        complete_route, complete_route_length = connect_routes(coordinates, initial_route, best_complete_route_length, num_routes_to_check)
        if complete_route and complete_route_length < best_complete_route_length:
            best_complete_route = complete_route
            best_complete_route_length = complete_route_length

    return best_complete_route


def connect_routes(coordinates, main_route, min_route_length=float("inf"), num_routes_to_check=10):
    remaining = remaining_points(coordinates, main_route)
    if not remaining:
        return main_route, route_length(main_route)

    remaining_routes = remaining_cluster(coordinates, main_route)[:num_routes_to_check]
    best_route = None
    best_route_length = min_route_length

    for remaining_route in remaining_routes:
        combined_route = check_for_combining(main_route, remaining_route)
        if combined_route:
            final_route, final_route_length = connect_routes(coordinates, combined_route, min_route_length=best_route_length, num_routes_to_check=num_routes_to_check)
            if final_route and final_route_length < best_route_length:
                best_route = final_route
                best_route_length = final_route_length

    return best_route, best_route_length

def plot_route(coordinates, route):
    x_coo = coordinates[:, 0]
    y_coo = coordinates[:, 1]
    x = [p[0] for p in route]
    y = [p[1] for p in route]
    fig, ax = plt.subplots()
    ax.plot(x_coo, y_coo, 'o')
    line, = ax.plot(x[:1], y[:1], '-')

    def update(num):
        num += 1
        if num >= len(x) + 1:
            ani.event_source.stop()
            return line,
        line.set_data(x[:num], y[:num])
        return line,

    ani = animation.FuncAnimation(fig, update, frames=len(x)+1, interval=150, blit=False)
    ax.plot(x[0], y[0], 'go')
    ax.plot(x[-1], y[-1], 'ro')
    plt.show()

def create_points_with_right_angles(num_points, scale=500):
    points = []
    angle = 0
    x, y = 0, 0

    for _ in range(num_points):
        angle += math.pi / 2 + random.uniform(0, math.pi / 2)
        dx, dy = math.cos(angle), math.sin(angle)
        x, y = x + dx * scale, y + dy * scale
        points.append((x, y))

    return points

def write_points_to_file(filename, points):
    with open(filename, 'w') as f:
        for point in points:
            f.write(f"{point[0]} {point[1]}\n")



if __name__ == "__main__":
    decision = int(input("Möchten Sie neue Koordinaten generieren (1) oder schon vorbereitete Punkte verwenden? (2)"))

    if decision == 1:
        number_points = int(input("Wie viele Punkte möchten Sie generieren?"))
        created_coordinates = create_points_with_right_angles(number_points)
        print("Die Länge der erstellten Route beträgt: " + route_length(created_coordinates))
    file = 'X:\points.txt'
    possible_routes = []
    coordinates = read_coordinates(file)
    start_time = time.time()
    complete_route = find_complete_route(coordinates)

    print("Die Länge der mit dem Algorithmus berechneten Route beträgt ", route_length(complete_route), " km.")
    end_time = time.time()
    print("Laufzeit: ", round(end_time - start_time, 2), " Sekunden")

    plot_route(np.array(coordinates), complete_route)

   

'''
Nicht mehr lösungsrelevant, nur zum probieren
Greedy-Backtracking-Algorithmus mit sehr hoher Laufzeit
'''

def find_shortest_route(coordinates):
    def greedy_backtracking(route=None, visited=None):
        if route is None:
            route = []
        if visited is None:
            visited = set()

        if len(route) == len(coordinates):
            return route

        unvisited = set(range(len(coordinates))) - visited
        next_points = []

        for i in unvisited:
            point = coordinates[i]
            if len(route) > 1:
                angle = calculate_angle(route[-2], route[-1], point)
            else:
                angle = 100

            if angle >= 90:
                next_points.append((i, calculate_distance(route[-1], point)))

        next_points.sort(key=lambda x: x[1])

        for i, _ in next_points:
            point = coordinates[i]
            new_visited = visited.copy()
            new_visited.add(i)
            new_route = greedy_backtracking(route=route + [point], visited=new_visited)
            if new_route:
                return new_route

        return None

    shortest_route = None
    shortest_route_length = float("inf")

    for i in range(len(coordinates)):
        route = greedy_backtracking(route=[coordinates[i]], visited={i})
        if route:
            route_len = route_length(route)
            if route_len < shortest_route_length:
                shortest_route = route
                shortest_route_length = route_len

    return shortest_route