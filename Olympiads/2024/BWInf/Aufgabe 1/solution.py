# Robert Vetter
# 20.10.2023
# Aufgabe 1 des 42. BWInf

# notwendigen Bibliotheken importieren
import random
import numpy as np
from collections import namedtuple
from heapq import heappop, heappush
import time
import matplotlib.pyplot as plt
import math

# Gitter intiialisieren, 2D Array mit Nullen
def initialize_grid(N):
    return np.zeros((N, N), dtype=int)

# nimmt eine Zelle und N entgegen und gibt max. 4 mögliche Nachbarn zurück, wenn diese innerhalb des Gitters liegen
def get_neighbours(cell, N):
    # Definiere die vier Richtungen: oben, unten, links und rechts
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    # Koordinaten beachbarter Zellen
    neighbours = []

    # alle Richtungen durchgehen
    for d in directions:
        # Koordinaten beachbarter Zelle berechnen und hinzufügen
        neighbour_x = cell[0] + d[0]
        neighbour_y = cell[1] + d[1]
        neighbours.append((neighbour_x, neighbour_y))

    valid_neighbours = []
    for i, j in neighbours:
        # innerhalb der Grenzen des Gitters
        if 0 <= i < N and 0 <= j < N:
            valid_neighbours.append((i, j))

    # alle Nachbarn zurückgeben
    return valid_neighbours

# Anzahl an beachbarten Zellen, die noch leer sind
def get_empty_neighbours(grid, cell, N):
    # Liste der beachbarten Zellen
    neighbours = get_neighbours(cell, N)

    # Initialisiere den leeren Nachbarzähler auf 0
    empty_neighbour_count = 0

    # Überprüfe jeden Nachbarn
    for neighbour in neighbours:
        # wenn Wert des Nachbarn im Raster 0 ist, erhöhe den leeren Nachbarzähler um 1
        if grid[neighbour] == 0:
            empty_neighbour_count += 1

    return empty_neighbour_count

# heuristische Funktion: Manhattan-Distanz zwischen zwei Punkten
def heuristic(a, b):
    # Unterschied zwischen den x-Koordinaten der Zellen a und b
    x_difference = abs(a[0] - b[0])
    
    # Unterschied zwischen den y-Koordinaten der Zellen a und b
    y_difference = abs(a[1] - b[1])

    return x_difference + y_difference

# Hauptalgorithmus für kürzesten Weg zwischen zwei Zellen
def astar(grid, start, end, N):
    # Tupelklasse "Node" mit den Attributen "total", "cell", "cost" und "heuristic"
    Node = namedtuple("Node", ["total", "cell", "cost", "heuristic"])
    
    # Set für besuchte Zellen
    visited = set()
    
    # Prioritätswarteschlange (aufgrund von heappush und heappop) mit dem Startknoten und seiner heuristischen Entfernung zum Ziel
    queue = [Node(heuristic(start, end), start, 0, heuristic(start, end))]
    
    # Dictionary, um die Vorgängerzellen zu speichern
    came_from = {}
    
    # solange die Warteschlange nicht leer ist
    while queue:
        # Entferne und erhalte Knoten mit niedrigsten Gesamtwert aus Warteschlange
        current = heappop(queue)
        
        # Wenn aktuelle Knoten Ziel, rekonstruiere Pfad und gebe ihn zurück
        if current.cell == end:
            path = [end]
            while end in came_from:
                end = came_from[end]
                path.append(end)
            return path[::-1]
        
        # Füge aktuelle Zelle zum Set der besuchten Zellen
        visited.add(current.cell)
        
        # Gehe durch alle Nachbarn der aktuellen Zelle
        for neighbour in get_neighbours(current.cell, N):
            # Überspringe Nachbarn, wenn er bereits besucht wurde oder wenn er nicht leer ist
            if neighbour in visited or grid[neighbour] != 0:
                continue
            
            # Berechne neuen Kosten für den Nachbarn
            new_cost = current.cost + 1
            
            # Erstelle neuen Knoten für Nachbarn mit den berechneten Kosten und Heuristik
            new_node = Node(new_cost + heuristic(neighbour, end), neighbour, new_cost, heuristic(neighbour, end))
            
            # Wenn der Nachbar noch nicht besucht wurde oder ein kürzerer Pfad gefunden wurde, füge ihn zur Warteschlange hinzu und aktualisiere 'came_from'
            if neighbour not in [item.cell for item in queue]:
                came_from[neighbour] = current.cell
                heappush(queue, new_node)

    # Wenn kein Pfad gefunden, gebe eine leere Liste zurück
    return []


# astar-Methode auf zwei zufällige Zellen aufrufen
def find_path(grid, current_path, N):
    # Liste der leeren Zellen im Gitter erstellen
    empty_cells = list(zip(*np.where(grid == 0)))

    # Wenn keine leeren Zellen vorhanden sind, unverändertes Gitter zurückgeben
    if not empty_cells or len(empty_cells) == 1:
        return grid, []
    
    # Überprüfen, ob alle verbleibenden leeren Zellen keine freien Nachbarn haben
    if all(get_empty_neighbours(grid, cell, N) == 0 for cell in empty_cells):
        return grid, []

    # Start- und Endzellen zufällig auswählen
    start = random.choice(empty_cells)
    end = random.choice(empty_cells)

    # Neue Start- und Endzellen auswählen, wenn sie gleich sind oder keine leeren Nachbarn haben
    while start == end or not (get_empty_neighbours(grid, start, N) and get_empty_neighbours(grid, end, N)):
        start = random.choice(empty_cells)
        end = random.choice(empty_cells)

    # A* Algorithmus verwenden, um den Pfad zwischen Start und Ende zu finden
    path = astar(grid, start, end, N)

    # Wenn der Pfad gültig ist und >= 3, Pfad zum Gitter hinzufügen und aktuellen Pfad zuweisen
    if len(path) >= 3:
        for cell in path:
            grid[cell] = current_path
        return grid, path  # Aktualisiertes Gitter und Pfad zurückgeben

    # Wenn kein gültiger Pfad gefunden wurde, unverändertes Gitter und leere Liste zurückgeben
    return grid, []

# Gitter reformatieren (sodass es im Format eines zu lösenden Rätsels erscheint)
def reformat_grid(grid, paths):
    # Durchlaufe jeden Pfad in den gefundenen Pfaden
    for path in paths:

        # Bestimme Kopf und Ende des Pfades
        head, tail = path[0], path[-1]

        # Setze alle Zellen des Pfades auf 0 zurück, außer Kopf und Ende
        for pos in path[1:-1]:
            grid[pos] = 0

        # Setze Kopf und Ende gleich
        grid[head] = grid[tail]

    return grid

# grafische Ausgabe der Linienzüge
def visualize_paths(grid, paths):
    N = grid.shape[0]
    plt.figure(figsize=(10, 10))
    
    # Farbliste für die Paths
    colors = plt.cm.jet(np.linspace(0, 1, len(paths)))

    # Sortiert Pfade basierend auf der Pfad-Nummer
    paths = sorted(paths, key=lambda path: grid[path[0]])

    # Zeichnet die Zellnummern und Pfad-Nummern
    for i in range(N):
        for j in range(N):
            if grid[i, j] != 0:
                plt.text(j, N - 1 - i, str(grid[i, j]), ha='center', va='center', color=colors[grid[i,j] - 1])

    # Zeichnet Verbindungen zwischen den Zellen eines Pfades
    for idx, path in enumerate(paths):
        for i in range(len(path)-1):
            start = path[i]
            end = path[i+1]
            plt.plot([start[1], end[1]], [N - 1 - start[0], N - 1 - end[0]], '-o', color=colors[grid[path[0]] - 1])

        # markiert Kopf und Ende mit fetter Schrift
        head, tail = path[0], path[-1]
        link_number = grid[head]
        plt.text(head[1], N - 1 - head[0], str(link_number), ha='center', va='center', color='black', weight='bold', fontsize=20)
        plt.text(tail[1], N - 1 - tail[0], str(link_number), ha='center', va='center', color='black', weight='bold', fontsize=20)
    
    # plottet Pfade
    plt.xlim(-0.5, N - 0.5)
    plt.ylim(-0.5, N - 0.5)
    plt.grid(True)
    plt.xticks(np.arange(N))
    plt.yticks(np.arange(N))
    plt.show()


def main():
    # Eingabe der Größe des Gitters (N) vom Benutzer
    print("Geben Sie die Länge der Seite 'N' des Gitters an: ")
    N = int(input())
    # Überprüfung, ob N größer oder gleich 4 ist, wenn nicht, wird Benutzer zur erneuten Eingabe aufgefordert
    while N < 4:
        print("Geben Sie ein größeres N ein (N > 4): ")
        N = int(input())
    
    # Startzeit für die Zeitmessung
    start = time.time()
    # Maximale Anzahl von Pfaden, die erstellt werden können
    max_links = 3 * N

    # Initialisierung des Gitters
    grid = initialize_grid(N)
    # Initialisierung des aktuellen Flows
    current_path = 1

    # Liste zur Speicherung der Pfade
    paths = []

    if N % 2 == 0:
        limit = N / 2
    else:
        limit = math.ceil(N / 2)

    # Schleife zur Erstellung der Pfade, bis die Hälfte der Flows erreicht ist
    while current_path < limit:
        # Zurücksetzen des aktuellen Pfades und der gesamten Pfade für jede Iteration
        current_path = 1
        paths = []
        # Zurücksetzen des Gitters für jede Iteration
        grid = initialize_grid(N)
        # Schleife zur Erstellung der Pfade
        for _ in range(max_links):
            grid, path = find_path(grid, current_path, N)
            # Wenn ein gültiger Pfad gefunden wurde, wird er zur Liste der Pfade hinzugefügt und der aktuelle Pfad wird erhöht
            if path:
                paths.append(path)
                current_path += 1

    # Ausgabe der benötigten Zeit zur Erstellung der Pfade
    print("Benötigte Zeit: ", (time.time() - start), " Sekunden")

    # Ausgabe der möglichen Lösung
    print("Mögliche Lösung: \n")
    for row in grid:
        print(' '.join(map(str, row)))

    # Kopie des Gitters zur späteren Verwendung
    gridCopy = grid
    
    # Ausgabe des Puzzles nach der Umformatierung des Gitters
    print("Puzzle: \n")
    grid = reformat_grid(grid, paths)
    # Ausgabe der Größe des Gitters und der Anzahl der Pfade
    print(N)
    print(current_path-1)
    # Ausgabe des umformatierten Gitters
    for row in grid:
        print(' '.join(map(str, row)))
    # Visualisierung der vollständigen Pfade
    visualize_paths(gridCopy, paths)


if __name__ == "__main__":
    main()

