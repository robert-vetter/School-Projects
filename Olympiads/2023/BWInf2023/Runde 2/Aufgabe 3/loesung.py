import heapq
from collections import namedtuple

# Define the PancakeState namedtuple for easy access to state and associated cost
PancakeState = namedtuple("PancakeState", ["stack", "ops", "heuristic"])


def is_sorted(stack):
    return stack == tuple(range(1, len(stack) + 1))


def heuristic(stack):
    # Number of unsorted pancakes from the top
    for i, pancake in enumerate(stack):
        if pancake != i + 1:
            return len(stack) - i
    return 0


def flip_and_eat(stack, idx):
    return stack[idx + 1:][::-1] + stack[idx + 1:]


def a_star_pancake_sort(stack):
    initial_state = PancakeState(stack=tuple(stack), ops=0, heuristic=heuristic(stack))
    open_set = [initial_state]
    visited = set()

    while open_set:
        current_state = heapq.heappop(open_set)
        visited.add(current_state.stack)

        if is_sorted(current_state.stack):
            return current_state.ops

        for idx in range(len(current_state.stack) - 1):
            new_stack = flip_and_eat(current_state.stack, idx)
            if new_stack in visited:
                continue

            new_ops = current_state.ops + 1
            new_heuristic = heuristic(new_stack)
            new_state = PancakeState(stack=tuple(new_stack), ops=new_ops, heuristic=new_heuristic)

            heapq.heappush(open_set, new_state)

    return -1  # This should never happen, given the problem constraints


if __name__ == "__main__":
    pancake_stack = [3, 2, 4, 5, 1]
    min_ops = a_star_pancake_sort(pancake_stack)
    print(f"Minimum number of operations: {min_ops}")





















