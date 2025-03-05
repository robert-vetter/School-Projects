import numpy as np
import time

class LeafBlowerSimulation:
    def __init__(self, size, initial_leaves):
        self.grid = np.full((size, size), float(initial_leaves), dtype=float)
        self.size = size

    # aktualisiert Gitter, koordiniert Klasse
    def blow_leaves(self, moves):
        for move in moves:
            position, direction = move
            x, y = position
            if not self._is_valid_move(x, y, direction):
                print(f"Warning: Cannot move {direction} from ({x}, {y}) - out of bounds!")
                continue
            dx, dy = self._get_direction_delta(direction)
            nx, ny = x + dx, y + dy
            self._move_leaves(x, y, nx, ny)
        self.display_grid()

    # überprüft, ob Bewegung innerhalb des Schulhofes erfolgt
    def _is_valid_move(self, x, y, direction):
        dx, dy = self._get_direction_delta(direction)
        nx, ny = x + dx, y + dy
        return 0 <= nx < self.size and 0 <= ny < self.size

    # mögliche Bewegungsrichtungen
    def _get_direction_delta(self, direction):
        directions = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }
        return directions.get(direction, (0, 0))

    # bewegt die Blätter und berechnet die Verteilungen
    def _move_leaves(self, x, y, nx, ny):
        # grundlegende Infos, die in Aufgabenstellung gegeben waren
        leaves_to_move = 0.8 * self.grid[x, y]
        left_leaves = 0.1 * self.grid[x, y]
        right_leaves = 0.1 * self.grid[x, y]
        push_leaves = 0.1 * self.grid[nx, ny]
        
        # Blätter auf einzelnen Feldern werden berechnet
        self.grid[x, y] -= leaves_to_move + left_leaves + right_leaves
        self.grid[nx, ny] += leaves_to_move - push_leaves

        # Berechnung der Koordinaten der betroffenen Felder
        dx, dy = nx - x, ny - y
        if dx != 0:
            lateral_left = (nx, ny-1)
            lateral_right = (nx, ny+1)
            front = (nx + dx, ny)
        else:
            lateral_left = (nx-1, ny)
            lateral_right = (nx+1, ny)
            front = (nx, ny + dy)

        # Blätterverteilung an Rändern wird berechnet (eigene Regeln, siehe Lösungsidee)
        if 0 <= lateral_left[1] < self.size and 0 <= lateral_left[0] < self.size:
            self.grid[lateral_left] += left_leaves
        else:
            self.grid[nx, ny] += left_leaves
        if 0 <= lateral_right[1] < self.size and 0 <= lateral_right[0] < self.size:
            self.grid[lateral_right] += right_leaves
        else:
            self.grid[nx, ny] += right_leaves
        if 0 <= front[0] < self.size and 0 <= front[1] < self.size:
            self.grid[front] += push_leaves
        else:
            self.grid[nx, ny] += push_leaves
        # Nullify nearly zero values
        self.grid[np.abs(self.grid) < 1e-6] = 0.0

    # lediglich das Gitter anzeigen
    def display_grid(self):
        column_width = 10

        formatter = lambda x: f"{x: {column_width}.3f}"

        np.set_printoptions(precision=3, suppress=True, linewidth=200, formatter={'float_kind': formatter})
        print(self.grid)
        total_leaves = np.sum(self.grid)
        print(f"Total leaves in grid: {total_leaves:.3f}")

# Lösungsstrategie (ausführliche Erklärung in Lösungsidee)
def determine_best_moves(size, initial_leaves):
    moves = []
    
    # Sammeln aller Blätter in Reihe 0
    for i in range(size-1, 0, -1):
        for j in range(size):
            moves.append([(i, j), 'up'])
    
    # Platzierung aller Blätter in (0, 1)
    for spalte in range(1):
        for _ in range(50 * initial_leaves):
            moves += [[(0, spalte), 'right']]
            moves += [[(1, spalte + 1), 'up']]
    
    for spalte in range(size-1, 2, -1):
        for _ in range(50 * initial_leaves):
            moves += [[(0, spalte), 'left']]
            moves += [[(1, spalte - 1), 'up']]
    
    # Verdichtung in Ecke
    moves += [[(0, 1), 'down']]
    moves += [[(1, 2), 'left']]
    
    for _ in range(50 * initial_leaves):
        moves += [[(2, 1), 'left']]
        moves += [[(3, 0), 'up']]
    moves += [[(1, 0), 'up']]
    
    
    # Periodisches Abgeben der 10% zur Seite
    for _ in range(50 * initial_leaves):
        moves += [[(0, 1), 'left']]
        moves += [[(0, 0), 'down']]
        moves += [[(2, 0), 'up']]
        moves += [[(1, 0), 'up']]
    
    return moves



n = 100
initial_leaves = 100
if n == 0 or initial_leaves == 0:
    print("Stopp! Es gibt nichts zu kehren!")
if n > 3:
    sim = LeafBlowerSimulation(size=n, initial_leaves=initial_leaves)
    print("Initial grid:")
    sim.display_grid()
    start = time.time()
    # best_moves = [[(0, 1), 'left'], [(0, 4), 'down']]
    best_moves = determine_best_moves(n, initial_leaves)
    end = time.time()

    sim.blow_leaves(best_moves)
    print("Benötigte Zeit: ", end - start, " Sekunden")
else:
    print("Mindestgröße vom Schulhof sind 4x4 Felder!")
