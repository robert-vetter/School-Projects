'''
Autor: Robert Vetter
Aufgabe: 1
'''

# notwendige Module/Bibliotheken importieren
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.animation as animation
import time
import random
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import os

# Methode, um die Koordinaten aus der txt-Datei einzulesen, gibt sie als Liste von Tupeln zurück
def read_coordinates(file):
    with open(file, "r") as f:
        lines = f.readlines()
        coordinates = []
        for line in lines:
            x, y = map(float, line.strip().split())
            coordinates.append((x, y))
    return coordinates

# Funktion zur Berechnung der Distanz zwischen zwei Punkten mithilfe des S. d. Pythagoras
def calculate_distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# Methode zur Berechnung des Winkels zwischen zwei Kanten, dabei ist p2 der Scheitelpunkt
def calculate_angle(p1, p2, p3):
    # Distanzen ausrechnen
    a = calculate_distance(p1, p2)
    b = calculate_distance(p2, p3)
    c = calculate_distance(p1, p3)

    # wenn zwei Punkte übereinander liegen, ist der Winkel valide und somit größer als 90° (exemplarisch 180°)
    if a == 0 or b == 0:
        return 180
    
    # mithilfe des Kosinussatz cos(alpha) berechnen
    cos_angle = (a**2 + b**2 - c**2) / (2*a*b)
    
    # wenn numerische Ungenauigkeiten auftreten, dann runden
    if cos_angle > 1:
        cos_angle = 1
    elif cos_angle < -1:
        cos_angle = -1

    # Winkel in Grad zurückgeben
    angle = math.degrees(math.acos(cos_angle))
    return round(angle, 2)

# berechnet die Länge der Route über die Summe der Distanzen zwischen je zwei adjazenten Punkten der Route
def route_length(route):
    return round(sum(calculate_distance(route[i], route[i + 1]) for i in range(len(route) - 1)), 3)

# Hauptalgorithmus des Programms, gibt alle gefundenen Routen zurück
def greedy_algorithm(coordinates):
    # all_routes und alle zu besuchenden Knoten initialisieren
    all_routes = []
    all_visited = set(range(len(coordinates)))

    # alle Startknoten durchgehen
    for start in range(len(coordinates)):
        # bisherige Route
        route = [coordinates[start]]
        # schon besuchte Punkte
        visited = {start}
        # noch unbesuchte Punkte
        unvisited = all_visited - visited
        # solange es immer noch unbesuchte Knoten gibt
        while unvisited:
            best_route = None
            best_distance = float("inf")
            # jeden möglichen nächsten Knoten durchgehen
            for i in unvisited:
                point = coordinates[i]
                # Winkel berechnen
                if len(route) > 1:
                    angle = calculate_angle(route[-2], route[-1], point)
                else:
                    # vom ersten Punkt kann zu jedem möglichen Punkt Kante gezogen werden
                    angle = 100
                if angle >= 90:
                    # wählt Punkt aus, bei dem der Winkel passt und der am nähesten dran ist
                    temp_distance = calculate_distance(route[-1], point)  
                    # wenn neuer nähester Punkt, bei dem der Winkel passt, dann füge ihn zur Route hinzu
                    if temp_distance < best_distance:
                        best_route = route + [point]
                        best_distance = temp_distance
            
            # wenn keine beste Route gefunden wurde, dann unterbreche
            if not best_route:
                break

            # lege die gefundene Route als die beste Route fest
            route = best_route

            # füge zu den bisher besuchten Punkten den letzten neu hinzugekommenen Punkt der Route hinzu und aktualisiere 'unvisited'
            visited.add(coordinates.index(route[-1]))
            unvisited = all_visited - visited
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


# gibt alle verbleibenden Punkte zurück, die noch nicht in einer Route inkludiert wurden
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

# checkt, ob man zwei Routen verbinden kann, in diesem Fall also eine Hauptroute (route) und eine Route im verbleibenden Cluster (remaining_cl_route)
def check_for_combining(route, remaining_cl_route):
    possible_routes = []

    # Start- und Endpunkte der Routen als Variablen abspeichern
    remaining_cl_route_start, remaining_cl_route_end = remaining_cl_route[0], remaining_cl_route[-1]
    cl_route_start, cl_route_end = route[0], route[-1]

    # wenn Länge der Route größer 1 ist
    if len(remaining_cl_route) > 1:
        # alle möglichen Verbindungen überprüfen, Bedingungen der Verbindungen werden in Liste abgespeichert
        # Möglichkeit 1: Start des ursprünglichen Clusters verbindet sich mit Start des remaining_clusters
        # Möglichkeit 2: Start des ursprünglichen Clusters verbindet sich mit Ende des remaining_clusters
        # Möglichkeit 3: Ende des ursprünglichen Clusters verbindet sich mit Start des remaining_clusters 
        # Möglichkeit 4: Ende des ursprünglichen Clusters verbindet sich mit Ende des remaining_clusters   
        route_conditions = [
            (calculate_angle(remaining_cl_route[1], remaining_cl_route_start, cl_route_start) >= 90 and
             calculate_angle(route[1], cl_route_start, remaining_cl_route_start) >= 90, route[::-1], remaining_cl_route),
            (calculate_angle(remaining_cl_route[-2], remaining_cl_route_end, cl_route_start) >= 90 and
             calculate_angle(route[1], cl_route_start, remaining_cl_route_end) >= 90, route[::-1], remaining_cl_route[::-1]),
            (calculate_angle(remaining_cl_route[1], remaining_cl_route_start, cl_route_end) >= 90 and
             calculate_angle(route[-2], cl_route_end, remaining_cl_route_start) >= 90, route, remaining_cl_route),
            (calculate_angle(remaining_cl_route[-2], remaining_cl_route_end, cl_route_end) >= 90 and
             calculate_angle(route[-2], cl_route_end, remaining_cl_route_end) >= 90, route, remaining_cl_route[::-1])
        ]
    else:
        # Route besteht aus einem Punkt -> dieser kann sich mit Start oder Ende der anderen Route verbinden
        route_conditions = [
            (calculate_angle(remaining_cl_route[0], cl_route_start, route[1]) >= 90, route[::-1], remaining_cl_route),
            (calculate_angle(remaining_cl_route[0], cl_route_end, route[-2]) >= 90, route, remaining_cl_route)
        ]

    # durch Bedingungen durch iterieren und wenn erfüllt, zusammengefügte Route zu possible_routes hinzufügen
    for condition, part1, part2 in route_conditions:
        if condition:
            possible_routes.append(part1 + part2)

    # Route mit minimaler Routenlänge zurückgeben
    if possible_routes:
        return min(possible_routes, key=lambda r: route_length(r))
    else:
        return None


# Methode, die alle ursprünglich gefundenen Routen durchgeht und die Methode 'connect_routes' aufruft, welche alle möglichen Verbindungen der Ursprungsroute mit anderen probiert
def find_complete_route(coordinates, num_routes_to_check=10):
    # initial_routes sind die im Graphen ursprünglich gefundenen Routen
    initial_routes = greedy_algorithm(coordinates)
    best_complete_route = None
    best_complete_route_length = float("inf")

    # in dieser for-Schleife wird jede ursprünglich gefundene Route durchgegangen
    for initial_route in initial_routes:
        complete_route, complete_route_length = connect_routes(coordinates, initial_route, best_complete_route_length, num_routes_to_check)
        # wenn neue Route gefunden wurde, die kürzer als die bisher kürzeste gefundene Route ist, dann aktualisiere die bisher kürzeste gefundene Route
        if complete_route and complete_route_length < best_complete_route_length:
            best_complete_route = complete_route
            best_complete_route_length = complete_route_length

    return best_complete_route

# Methode, die über Rekursion alle möglichen Routenkombinationen durchzugehen
def connect_routes(coordinates, main_route, min_route_length=float("inf"), num_routes_to_check = 10):
    # verbleibenden Punkte berechnen
    remaining = remaining_points(coordinates, main_route)

    # wenn es keine gibt, ist Route vollständig und kann zurückgegeben werden
    if not remaining:
        return main_route, route_length(main_route)

    # sonst suche Routen in den verbleibenden Punkten
    remaining_routes = remaining_cluster(coordinates, main_route)[:num_routes_to_check]
    best_route = None
    best_route_length = min_route_length

    # versuche, die Ursprungsroute solange mit anderen verbleibenden Routen zu verbinden, bis alle Punkte Teil der Route sind
    for remaining_route in remaining_routes:
        combined_route = check_for_combining(main_route, remaining_route)
        if combined_route:
            # rekursiver Aufruf, um möglichst viele Punkte in der Route zu inkludieren
            final_route, final_route_length = connect_routes(coordinates, combined_route, min_route_length=best_route_length, num_routes_to_check=num_routes_to_check)
            # wenn neue beste Route gefunden, dann speichere sie ab
            if final_route and final_route_length < best_route_length:
                best_route = final_route
                best_route_length = final_route_length

    return best_route, best_route_length


# Methode zur visuellen Anzeige der Route
def plot_route(coordinates, route, cluster = False):
    # x- und y-Koordinaten festlegen
    x_coo = coordinates[:, 0]
    y_coo = coordinates[:, 1]
    x = [p[0] for p in route]
    y = [p[1] for p in route]

    fig, ax = plt.subplots()
    
    # wenn selbstständig Punkte generiert werden sollen (also auch K-Means angewendet wird)
    if cluster and len(route) > 10:
        # führe K-Means auf Koordinaten aus und bestimme den Punkt, der dem jeweiligen Zentrum am nähesten liegt
        optimal_clusters = determine_number_of_clusters(coordinates)
        labels, cluster_centers = k_means_cluster(coordinates, optimal_clusters)
        closest_points = find_closest_points_to_centers(coordinates, cluster_centers)
        print("Die Reise dauert voraussichtlich ungefähr ", time_of_travel(coordinates, route, closest_points), " Tage.")

        # Grenzen für Plot festlegen
        min_val = min(min(x_coo), min(y_coo)) - 50
        max_val = max(max(x_coo), max(y_coo)) + 50
        ax.set_xlim(min_val, max_val)
        ax.set_ylim(min_val, max_val)
        
        # Cluster points
        ax.scatter(x_coo, y_coo, c=labels, cmap='viridis', alpha=0.4)
        # Closest points
        ax.scatter(closest_points[:, 0], closest_points[:, 1], c='blue', marker='o', s=60, label='Zentrale Stadt')
        line, = ax.plot(x[:1], y[:1], '-', color='orange')
    else:
        ax.plot(x_coo, y_coo, 'o')
        line, = ax.plot(x[:1], y[:1], '-')

    # zeichnet die Route Stück für Stück in KOS, aktualisiert somit visuelle Darstellung 
    def update(num):
        num += 1
        if num >= len(x) + 1:
            ani.event_source.stop()
            return line,
        line.set_data(x[:num], y[:num])
        return line,

    ani = animation.FuncAnimation(fig, update, frames=len(x)+1, interval=150, blit=False)

    # hier werden spezifische Parameter zur grafischen Darstellung festgelegt
    if cluster and len(route) > 10:
        ax.plot(x[0], y[0], 'go', zorder=5)
        ax.plot(x[-1], y[-1], 'ro', zorder=6)
        plt.legend()
    else:
        ax.plot(x[0], y[0], 'go')
        ax.plot(x[-1], y[-1], 'ro')

    plt.show()


def time_of_travel(coordinates, route, closest_points):
    # Flugzeug fliegt mit 800 km/h, Annahme: Reisender hält sich 1 Tag in gewöhnlicher Stadt und 2 Tage in zentral gelegener Stadt auf
    # -> tges = tFlug + tZentral + tGewöhnlich
    return round((route_length(route) / 800) / 24 + 1 * (len(coordinates) - len(closest_points)) + 2 * len(closest_points), 2)

# führt KMeans-Clustering mithilfe von sklearn durch
def k_means_cluster(coordinates, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, n_init=10).fit(coordinates)
    cluster_centers = kmeans.cluster_centers_
    return kmeans.labels_, cluster_centers

# sucht Punkt mit geringster Entfernung zum Zentrum des Clusters
def find_closest_points_to_centers(coordinates, cluster_centers):
    closest_points = []
    # gehe alle cluster_center durch und berechne die Entfernung der Punkte zum Cluster -> füge nähesten zu closest_points hinzu
    for center in cluster_centers:
        distances = np.linalg.norm(coordinates - center, axis=1)
        closest_point_idx = np.argmin(distances)
        closest_points.append(coordinates[closest_point_idx])
    return np.array(closest_points)

# bestimme optimales k für K-Means
def determine_number_of_clusters(coordinates):
    max_clusters = min(10, len(coordinates))
    best_silhouette_score = -1
    best_n_clusters = 2

    # mithilfe dieser for-Schleife werden verschiedene k ausprobiert und mithilfe des Shilhouette-Scores bewertet, das k mit dem höchsten Silhouette-Score wird zurückgegeben
    for n_clusters in range(2, max_clusters + 1):
        labels, cluster_centers = k_means_cluster(coordinates, n_clusters)
        score = silhouette_score(coordinates, labels)

        if score > best_silhouette_score:
            best_silhouette_score = score
            best_n_clusters = n_clusters

    return best_n_clusters

# erstelle eine Test-Route, in welcher die Winkelbedingung eingehalten wird   
def create_points_with_right_angles(num_points, limit=1200):
    points = []
    x, y = random.uniform(-limit, limit), random.uniform(-limit, limit)

    # die for-Schleife erzeugt num_points-Punkte im Bereich -limit bis limit
    for _ in range(num_points):
        angle = random.uniform(0, 2 * math.pi)
        scale = random.uniform(0, limit)  

        # generiere die Position des nächsten Punktes
        dx, dy = math.cos(angle) * scale, math.sin(angle) * scale
        new_x, new_y = x + dx, y + dy

        # solange der Punkt noch außerhalb des Bereichs liegt
        while new_x < -limit or new_x > limit or new_y < -limit or new_y > limit:
            scale = random.uniform(0, limit / 2)
            dx, dy = math.cos(angle) * scale, math.sin(angle) * scale
            new_x, new_y = x + dx, y + dy

        # füge Punkt zu points hinzu
        x, y = new_x, new_y
        points.append((x, y))

    return points

# Test-Route wird in einer txt-Datei abgespeichert
def write_points_to_file(filename, points):
    with open(filename, 'w') as f:
        for point in points:
            f.write(f"{point[0]} {point[1]}\n")

if __name__ == "__main__":
    valid = False

    # solange keine gültige Eingabe eingelesen wurde, Frage erneut
    while not valid:
        decision = int(input("Möchten Sie neue zufällige Koordinaten generieren (1) oder schon vorbereitete Punkte verwenden? (2) "))

        if decision == 1:
            number_points = int(input("Wie viele Punkte möchten Sie generieren? "))
            complete_route = None
            start_time = time.time()
            # es wird nicht immer eine Route gefunden -> probiere solange, bis eine gefunden wird
            while not complete_route:
                created_coordinates = create_points_with_right_angles(number_points)
                # speichere "points.txt" in aktuellem Verzeichnis
                current_directory = os.path.dirname(os.path.abspath(__file__))
                file = os.path.join(current_directory, 'points.txt')
                write_points_to_file(file, created_coordinates)
                coordinates = read_coordinates(file)
                # wenn Anzahl Punkte höher als 70, suche mit geringerem Schwellenwert -> senkt Laufzeit
                if number_points > 70:
                    complete_route = find_complete_route(coordinates, num_routes_to_check=2)
                else:
                    complete_route = find_complete_route(coordinates)
            print("Die Länge der zufällig generierten Route beträgt ", route_length(coordinates), " km.")
            break

        elif decision == 2:
            file_found = False
            # solange kein gültiger Dateiname eingegeben wurde
            while not file_found:
                file_name = str(input("Geben Sie die Bezeichnung der txt-Datei mit den Koordinaten an (Bsp.: wenigerkrumm1.txt). \nDie Datei muss sich dafür in demselben Verzeichnis wie dieses Skript befinden.: "))
                # Datei im aktuellen Verzeichnis finden
                current_directory = os.path.dirname(os.path.abspath(__file__))
                file_path = os.path.join(current_directory, file_name)
                
                # Überprüfen, ob die Datei existiert
                if os.path.isfile(file_path):
                    file_found = True
                else:
                    print("Datei nicht gefunden. Bitte geben Sie einen gültigen Dateinamen ein.")

            coordinates = read_coordinates(file_path)
            start_time = time.time()
            complete_route = find_complete_route(coordinates)
            break
        else:
            print("Die Eingabe war ungültig. Geben Sie entweder eine 1 oder eine 2 ein.")
    
    print("Die Länge der mit dem Algorithmus berechneten Route beträgt ", route_length(complete_route), " km.")
    end_time = time.time()
    print("Laufzeit: ", round(end_time - start_time, 2), " Sekunden")

    # Route plotten
    if decision == 1:
        plot_route(np.array(coordinates), complete_route, cluster=True)
    if decision == 2:
        plot_route(np.array(coordinates), complete_route, cluster=False)
    
    
    
   

