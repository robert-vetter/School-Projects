import os
import heapq
import itertools
import time
from concurrent.futures import ProcessPoolExecutor
import time

def read_pancakes_from_file(filename):
    with open(filename, "r") as file:
        num_pancakes = int(file.readline())
        pancakes = [int(line.strip()) for line in file.readlines()]
    return pancakes

def is_sorted(stack):
    return all(stack[i] <= stack[i + 1] for i in range(len(stack) - 1))

def heuristic(stack):
   return sum(1 for i in range(len(stack) - 1) if stack[i] > stack[i + 1])


def successors(stack):
    for i in range(1, len(stack) + 1):
        flipped_stack = stack[:i][::-1][1:] + stack[i:]
        yield flipped_stack

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

def a_star_pancake_sort(stack):
    start = tuple(stack)
    goal = tuple(sorted(stack))

    open_set = [(heuristic(start), 0, start)]
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current_g_score, current = heapq.heappop(open_set)

        if is_sorted(current):
            return reconstruct_path(came_from, current)

        for neighbor in successors(current):
            tentative_g_score = current_g_score + 1

            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor)
                heapq.heappush(open_set, (f_score, tentative_g_score, neighbor))

    return None


def print_steps(sorted_path):
    steps = []
    for i in range(len(sorted_path) - 1):
        prev_state, next_state = sorted_path[i], sorted_path[i + 1]
        flipped_index = next(i for i in range(len(prev_state)) if prev_state[:i+1][::-1][1:] + prev_state[i+1:] == next_state) + 1
        steps.append((flipped_index, list(next_state)))
    return steps


def generate_permutations(n):
    return itertools.permutations(range(1, n + 1))

def find_pwue_number_helper(stack):
    stack = list(stack)
    sorted_path = a_star_pancake_sort(stack)
    if sorted_path:
        steps = len(sorted_path) - 1
        return steps, stack
    return 0, stack

def find_pwue_number(n, previous_pwue_number=None):
    max_operations = 0
    max_example = None

    stacks = list(generate_permutations(n))
    results = [find_pwue_number_helper(stack) for stack in stacks]

    for steps, stack in results:
        if steps > max_operations:
            max_operations = steps
            max_example = stack

        # Abbruchbedingung, wenn die PWUE-Zahl von PWUE(n) um 1 größer als die PWUE-Zahl von PWUE(n-1) ist
        if previous_pwue_number is not None and max_operations >= previous_pwue_number + 1:
            break

    return max_operations, max_example

# Funktion zum Berechnen der PWUE-Zahlen fuer Pfannkuchenstapel von der Groesse 'start' bis zur Groesse 'end
def calculate_pwue_numbers(start, end):
    pwue_numbers = {}
    previous_pwue_number = None
    for n in range(start, end + 1):
        pwue_number, example = find_pwue_number(n, previous_pwue_number)
        pwue_numbers[n] = (pwue_number, example)
        print(f"Kurzform: P({n}) = {pwue_number}, Beispiel: {example}")

        # Aktualisiere die vorherige PWUE-Zahl für die nächste Iteration
        previous_pwue_number = pwue_number

    return pwue_numbers


def main():
    decision = int(input("Möchten Sie die minimale Anzahl an Wende-Und-Ess-Operationen ausgeben (1) oder stattdessen die PWUE-Zahl berechnen?(2) "))
    start = time.time()
    if decision == 1:
        filename = "pancake7.txt"
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, filename)
        pancake_list = read_pancakes_from_file(file_path)
        print("Ursprünglicher Stapel: ", pancake_list)
        sorted_path = a_star_pancake_sort(pancake_list)
        if sorted_path:
            steps = print_steps(sorted_path)
            print("Schritte:", len(steps), "Steps:", steps)
        else:
            print("Keine Lösung gefunden")
    else:
        pwue_numbers = calculate_pwue_numbers(10, 11)

        for n, (pwue_number, example) in pwue_numbers.items():
            print(f"P({n}) = {pwue_number}, Beispiel: {example}")
    end = time.time()
    duration = end - start
    print("Die Programmlaufzeit beträgt ", duration, " Sekunden")

if __name__ == "__main__":
    main()




