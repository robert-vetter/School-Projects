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
        push_leaves = 0.1 * self.grid[nx, ny]
        
        self.grid[x, y] -= leaves_to_move + left_leaves + right_leaves
        self.grid[nx, ny] += leaves_to_move - push_leaves

        dx, dy = nx - x, ny - y
        if dx != 0:
            lateral_left = (nx, ny-1)
            lateral_right = (nx, ny+1)
            front = (nx + dx, ny)
        else:
            lateral_left = (nx-1, ny)
            lateral_right = (nx+1, ny)
            front = (nx, ny + dy)
        # Adjust leaves dispersal at boundaries
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

    def display_grid(self):
        column_width = 10

        formatter = lambda x: f"{x: {column_width}.3f}"

        np.set_printoptions(precision=3, suppress=True, linewidth=200, formatter={'float_kind': formatter})
        print(self.grid)
        total_leaves = np.sum(self.grid)
        print(f"Total leaves in grid: {total_leaves:.3f}")




    
def determine_best_moves(size, initial_leaves):
    moves = []
    middle  = size // 2

    for i in range(size-1, 0, -1):
        for j in range(size):
            moves.append([(i, j), 'up'])

    if size % 2 != 0:
        for spalte in range(middle - 1):
            for _ in range(2 * initial_leaves):
                moves += [[(0, spalte), 'right']]
                moves += [[(1, spalte + 1), 'up']]
        
        for spalte in range(size-1, middle + 1, -1):
            for _ in range(2 * initial_leaves):
                moves += [[(0, spalte), 'left']]
                moves += [[(1, spalte - 1), 'up']]
        
        moves += [[(0, middle), 'down']]
        moves += [[(1, middle + 1), 'left']]
        moves += [[(1, middle - 1), 'up']]
        moves += [[(2, middle), 'left']]
        
        for _ in range(1):
            # Sammlung in Reihe 0
            for i in range(50):
                moves += [[(2, middle), 'left']]
                for i in range(4, 0, -1):
                    for j in range(0, middle):
                        moves += [[(i, j), 'up']]
            
            # Sammlung in (0, middle-1)
            for spalte in range(middle - 1):
                for _ in range(2 * initial_leaves):
                    moves += [[(0, spalte), 'right']]
                    moves += [[(1, spalte + 1), 'up']]
            
            '''
            for spalte in range(size-1, middle + 1, -1):
                for _ in range(2 * initial_leaves):
                    moves += [[(0, spalte), 'left']]
                    moves += [[(1, spalte - 1), 'up']]
            
            for spalte in range(middle - 1):
                for _ in range(2 * initial_leaves):
                    moves += [[(0, spalte), 'right']]
                    moves += [[(1, spalte + 1), 'up']]
            '''




    
    #moves += [[(0, 2), 'down']]
    #moves += [[(1, 3), 'left']]
    #moves += [[(1, 1), 'right']]


    return moves



n = 11
initial_leaves = 100
sim = LeafBlowerSimulation(size=n, initial_leaves=initial_leaves)
print("Initial grid:")
sim.display_grid()
# best_moves = [[(0, 1), 'left'], [(0, 4), 'down']]
best_moves = determine_best_moves(n, initial_leaves)


sim.blow_leaves(best_moves)
