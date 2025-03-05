import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.animation as animation
import time


def read_coordinates(file):
    with open(file, "r") as f:
        lines = f.readlines()
        coordinates = []
        for line in lines:
            x, y = map(float, line.strip().split())
            coordinates.append((x, y))
    return coordinates

def calculate_distance(p1, p2):
    # Funktion zur Berechnung der Distanz zwischen zwei Punkten
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def calculate_angle(p1, p2, p3):
    # p2 ist der Scheitelwinkel
    a = calculate_distance(p1, p2)
    b = calculate_distance(p2, p3)
    c = calculate_distance(p1, p3)
    if a == 0 or b == 0:
        return 90
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
    return length

def greedy_approach(coordinates):
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
                        temp_route = route + [point]
                        temp_distance = route_length(temp_route)
                        if temp_distance < best_distance:
                            best_route = temp_route
                            best_distance = temp_distance
            if not best_route:
                break
            route = best_route
            visited.add(coordinates.index(route[-1]))
            unvisited = all_visited - visited
        if len(route) >= len(overall_best_route):
            overall_best_route = route
        all_routes.append(route)
    all_routes = sort_lists(all_routes)
    return all_routes

# sortiert Liste nach len(list) und wenn Länge gleich, dann nach route_length(list)
def sort_lists(lists):
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

# gibt alle verbleibenden Punkte zurück
def remaining_points(all_points, route):
    remaining = all_points[:] # create a copy of all points
    for point in route:
        if point in remaining:
            remaining.remove(point)
    return remaining

# gibt alle Routen in den verbleibenden Punkten zurück
def remaining_cluster(coordinates, route):
    remaining_cl_route = greedy_approach(remaining_points(coordinates, route))
    return remaining_cl_route

# checkt, ob man zwei Cluster verbinden kann 
def combining_algorithm(route, remaining_cl_route):
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

#nochmal überarbeiten
# die Methode müsste theoretisch jede mögliche Route durchgehen, die der Greedy-Algorithmus in der Liste hat
def combine(coordinates, route):
    remaining_cl_route = []
    all_combined_routes = []
    remaining_cl_route = remaining_cluster(coordinates, route)
    
    for remaining_route in remaining_cl_route:
        new_route = combining_algorithm(route, remaining_route)
        if new_route is not None:
            if len(remaining_points(coordinates, new_route)) == 0:
                all_combined_routes += new_route
            
                
    if not len(all_combined_routes) == 0:
        print(all_combined_routes)
        return all_combined_routes
    return None


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



if __name__ == "__main__":
    file = 'X:\wenigerkrumm1.txt'
    # file = 'X:\points.txt'
    possible_routes = []
    coordinates = read_coordinates(file)
    start_time = time.time()
    all_routes = greedy_approach(coordinates)

    
    for i in range(len(all_routes)):
        new_route = all_routes[i]
        if len(remaining_points(coordinates, new_route)) == 0:
            possible_routes.append(new_route)
        else:
            while len(remaining_points(coordinates, new_route)) > 0:
                new_route = combine(coordinates, new_route)
                if new_route is None:
                    break
                else:
                    possible_routes.append(new_route)
                print(possible_routes)
                    
    if not len(possible_routes) == 0:
        for i in range(len(possible_routes)):
            print(len(possible_routes[i]))
            print(route_length(possible_routes[i]))
        
        if len(possible_routes) == 1:
            shortest_route = possible_routes
        else:
            shortest_route =  min(possible_routes, key=lambda route: route_length(route))
        print("Die Länge der Route beträgt ", route_length(shortest_route), " km.")
        end_time = time.time()
        print("Dauer: ", end_time - start_time, " Sekunden")
        plot_route(np.array(coordinates), shortest_route)
        exit()
    
                    