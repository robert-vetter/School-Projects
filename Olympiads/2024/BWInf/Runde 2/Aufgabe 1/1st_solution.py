import numpy as np

class LeafBlowerSimulation:
    def __init__(self, size, initial_leaves):
        self.grid = np.full((size, size), float(initial_leaves), dtype=float)
        self.size = size

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
            print(f"After moving {direction} from ({x}, {y}):")
            self.display_grid()

    def _is_valid_move(self, x, y, direction):
        dx, dy = self._get_direction_delta(direction)
        nx, ny = x + dx, y + dy
        return 0 <= nx < self.size and 0 <= ny < self.size

    def _get_direction_delta(self, direction):
        directions = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }
        return directions.get(direction, (0, 0))

    def _move_leaves(self, x, y, nx, ny):
        leaves_to_move = 0.8 * self.grid[x, y]
        left_leaves = 0.1 * self.grid[x, y]
        right_leaves = 0.1 * self.grid[x, y]
        
        # Berechne den Anteil, der nach vorne geschoben wird, bevor die Hauptmenge aktualisiert wird
        push_leaves = 0.1 * self.grid[nx, ny]

        # Subtrahiere die Blätter von der aktuellen Position
        self.grid[x, y] -= leaves_to_move + left_leaves + right_leaves
        # Addiere die Hauptmenge der Blätter zur neuen Position
        self.grid[nx, ny] += leaves_to_move

        # Update die benachbarten Felder
        dx, dy = nx - x, ny - y
        if dx != 0:
            lateral_left = (nx, ny-1)
            lateral_right = (nx, ny+1)
            front = (nx + dx, ny)
        else:
            lateral_left = (nx-1, ny)
            lateral_right = (nx+1, ny)
            front = (nx, ny + dy)

        # Stelle sicher, dass Seiten- und Vorwärtsverluste korrekt gehandhabt werden
        if 0 <= lateral_left[1] < self.size:
            self.grid[lateral_left] += left_leaves
        if 0 <= lateral_right[1] < self.size:
            self.grid[lateral_right] += right_leaves
        if 0 <= front[0] < self.size:
            self.grid[front] += push_leaves

        # Korrigiere kleine Werte nach jeder Verschiebung
        self.grid[self.grid < 1e-6] = 0.0


    def display_grid(self):
        rounded_grid = np.round(self.grid, 3)  # Rundet das Gitter auf drei Nachkommastellen
        print(rounded_grid)
        total_leaves = np.sum(self.grid)
        print(f"Total leaves in grid: {total_leaves:.3f}")

    
def determine_best_moves(size):
    moves = []
    target_column = size // 2

    # Schritt 1: Herausbildung von zwei Reihen
    # Bewege alle Reihen oberhalb der Mitte nach unten
    for i in range(size // 2 - 1):
        for j in range(size):
            moves.append([(i, j), 'down'])
    # Bewege alle Reihen unterhalb der Mitte nach oben
    for i in range(size - 1, size // 2, -1):
        for j in range(size):
            moves.append([(i, j), 'up'])

    # Schritt 2: Sammlung aller Blätter in Reihe 0
    lower_row = size // 2
    for i in range(lower_row, 0, -1):
        for j in range(size):
            moves.append([(i, j), 'up'])

    # Schritt 3: Maximierung der Blätter auf dem Zielfeld
    for j in range(target_column + 1):
        moves.append([(0, j), 'right'])
    for j in range(size - 1, target_column, -1):
        moves.append([(0, j), 'left'])
    for j in range(target_column + 1):
        moves.append([(1, j), 'right'])
    for j in range(size - 1, target_column, -1):
        moves.append([(1, j), 'left'])
    
    #for j in range(size):
    #    moves.append([(2, j), 'up'])
    moves.append([(2, 0), 'up'])
    moves.append([(2, 1), 'up'])
    # wo ist das Problem mit dieser Zeile Code bei diesem Gitter ?
    moves.append([(0, 2), 'left'])

    '''
    [[   0.       0.       7.181   57.206 4793.273  109.748    0.       0.   ]
    [   0.       0.       0.      12.891 1121.916    0.       0.       0.   ]
    [   0.       0.       7.181   19.421  161.435  109.748    0.       0.   ]
    [   0.       0.       0.       0.       0.       0.       0.       0.   ]
    [   0.       0.       0.       0.       0.       0.       0.       0.   ]
    [   0.       0.       0.       0.       0.       0.       0.       0.   ]
    [   0.       0.       0.       0.       0.       0.       0.       0.   ]
    [   0.       0.       0.       0.       0.       0.       0.       0.   ]]
    '''




    return moves



n = 8
sim = LeafBlowerSimulation(size=n, initial_leaves=100)
print("Initial grid:")
sim.display_grid()
# best_moves = [[(0, 1), 'left'], [(0, 4), 'down']]
best_moves = determine_best_moves(n)
# best_moves = [[(0, 0), 'right']]
sim.blow_leaves(best_moves)
