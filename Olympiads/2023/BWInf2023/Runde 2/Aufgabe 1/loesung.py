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
    global one_route
    all_routes = []
    one_route = False
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
        if len(visited) == len(coordinates):
            one_route = True
            return overall_best_route
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
        remaining.remove(point)
    return remaining

# gibt alle Routen in den verbleibenden Punkten zurück
def remaining_cluster(coordinates, route):
    remaining_cl_route = greedy_approach(remaining_points(coordinates, route))
    return remaining_cl_route

# checkt, ob man zwei Routen verbinden kann 
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
    remaining_cl_route = remaining_cluster(coordinates, route)
    if one_route:
        return combining_algorithm(route, remaining_cl_route)
    if not one_route:
        for remaining_route in remaining_cl_route:
            new_route = combining_algorithm(route, remaining_route)
            if new_route is not None:
                return new_route
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
    file = 'X:\wenigerkrumm7.txt'
    coordinates = read_coordinates(file)
    start_time = time.time()
    all_routes = greedy_approach(coordinates)

    if one_route:
        print("Die Länge der Route beträgt ", route_length(all_routes), " km.")
        end_time = time.time()
        print("Dauer: ", end_time - start_time, " Sekunden")
        plot_route(np.array(coordinates), all_routes)
    else:
        for i in range(len(all_routes)):
            new_route = all_routes[i]
            while len(remaining_points(coordinates, new_route)) > 0:
                new_route = combine(coordinates, new_route)
                if new_route is None:
                    break
                else:
                    if len(remaining_points(coordinates, new_route)) == 0:
                        print("Die Länge der Route beträgt ", route_length(new_route), " km.")
                        end_time = time.time()
                        print("Dauer: ", end_time - start_time, " Sekunden")
                        plot_route(np.array(coordinates), new_route)
                        exit()
                    



'''#dfs
def build_graph(coordinates):
    graph = defaultdict(list)
    for i, (x1, y1) in enumerate(coordinates):
        for j, (x2, y2) in enumerate(coordinates):
            if i == j:
                continue
            graph[i].append(j)
    return graph

def check_angle1(v1, v2):
    angle = np.math.atan2(*v2[::-1]) - np.math.atan2(*v1[::-1])
    return abs(angle) < np.pi / 2

def dfs(graph, node, visited, route, shortest_route):
    if len(visited) == len(graph):
        if not shortest_route or len(route) < len(shortest_route):
            shortest_route[:] = list(route)
        return

    for neighbor in graph[node]:
        if neighbor in visited:
            continue
        v1 = np.array(coordinates[neighbor]) - np.array(coordinates[node])
        if check_angle1(v1, np.array(route[-2]) - np.array(route[-1]) if len(route) > 1 else np.array([1, 0])):
            continue
        route.append(coordinates[neighbor])
        visited.add(neighbor)
        dfs(graph, neighbor, visited, route, shortest_route)
        route.pop()
        visited.remove(neighbor)

def dfs_search_approach(coordinates):
    graph = build_graph(coordinates)
    shortest_route = []
    for node in graph:
        route = [coordinates[node]]
        visited = {node}
        dfs(graph, node, visited, route, shortest_route)
    return shortest_route

#backtrack

def find_route(points):
    def distance(p1, p2):
        return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
    
    def angle(p1, p2, p3):
        a = distance(p1, p2)
        b = distance(p2, p3)
        c = distance(p1, p3)
        return math.degrees(math.acos((b**2 + c**2 - a**2) / (2*b*c)))

    def backtrack(route, remaining):
        if not remaining:
            return route
        for i, point in enumerate(remaining):
            new_route = route + [point]
            if len(new_route) > 2:
                prev_point = new_route[-3]
                curr_point = new_route[-2]
                next_point = new_route[-1]
                if angle(prev_point, curr_point, next_point) <= 90:
                    continue
            result = backtrack(new_route, remaining[:i] + remaining[i+1:])
            if result:
                return result
        return None
    print("Backtracking fertig")
    if backtrack([points[0]], points[1:]) is None:
        return
    return backtrack([points[0]], points[1:])
    
def improve_route(route, coordinates):
    remaining = remaining_points(coordinates, route)
    route_remaining = greedy_approach(remaining)
    route_remaining_first_and_last = []
    route_remaining_first_and_last += tuple([route_remaining[0]])
    route_remaining_first_and_last += tuple([route_remaining[-1]])
    new_route = []
    for i in range(2, len(route)-1):
        for point in route_remaining_first_and_last:
            if calculate_angle(route[i-2], point, route[i-1]) >= 90 and calculate_angle(route[i+1], point, route[i]) >= 90:
                new_route += route[:i-1]
                part = route[i:]
                new_route += part[::-1]
                print(new_route[-1])
                print(route_remaining[0])
                print(route_remaining[1])
                print(calculate_angle(new_route[-1], route_remaining[1], route_remaining[0]))
                if 180 - calculate_angle(route_remaining[1], new_route[-1], route_remaining[0]) >= 90:
                    new_route += route_remaining
                    return new_route
    
    
    # def greedy_approach(coordinates):
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
                # Vektor 1
                v1 = np.array(route[-1]) - np.array(point)
                if len(route) > 1:
                    # Vektor 2
                    v2 = np.array(route[-2]) - np.array(route[-1])

                else:
                    v2 = np.array([1, 0])
                if check_angle(v1, v2):
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
        if len(route) > len(overall_best_route):
                overall_best_route = route
        if len(visited) == len(coordinates):
            return overall_best_route
    return overall_best_route

    def check_angle(v1, v2):
    cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    if cos_angle > 1:
        cos_angle = 1
    elif cos_angle < -1:
        cos_angle = -1
    angle = math.acos(cos_angle)
    return abs(angle) <= math.pi / 2 
    '''


