import os
import heapq
import itertools
import time
from concurrent.futures import ProcessPoolExecutor
from functools import lru_cache
import random



def read_pancakes_from_file(filename):
    with open(filename, "r") as file:
        num_pancakes = int(file.readline())
        pancakes = [int(line.strip()) for line in file.readlines()]
    return pancakes

# Funktion zum Überprüfen, ob der Stapel sortiert ist. Die Funktion gibt True zurück, wenn der Stapel sortiert ist, andernfalls False.
def is_sorted(stack):
    # 'all' gibt True zurück, wenn alle Elemente in der iterierbaren Liste (in diesem Fall einer Generator-Ausdruck) True sind.
    # Die Schleife prüft, ob jedes Element im Stapel kleiner oder gleich dem nächsten Element ist.
    return all(stack[i] <= stack[i + 1] for i in range(len(stack) - 1))

# Heuristik, die die Anzahl der ungeordneten Paare in einem Stapel berechnet. Die Heuristik gibt eine Schätzung der verbleibenden Schritte zurück, die benötigt werden, um den Stapel zu sortieren.
def heuristic(stack):
    # 'sum' berechnet die Summe der Elemente in der iterierbaren Liste (in diesem Fall einer Generator-Ausdruck).
    # Die Schleife zählt, wie oft ein Element im Stapel größer ist als das nächste Element.
    return sum(1 for i in range(len(stack) - 1) if stack[i] > stack[i+1])

# Funktion zum Generieren von Nachfolgern (möglichen Schritten) für einen gegebenen Stapel. Die Funktion gibt eine Sequenz von Stapeln zurück, die durch Anwenden einer Wendeoperation auf den gegebenen Stapel erzeugt wurden.
def successors(stack):
    # Die Schleife iteriert über alle möglichen Wendepunkte im Stapel.
    for i in range(1, len(stack) + 1):
        # Der Wendevorgang wird auf den Teil des Stapels bis zum i-ten Element (ausschließlich) angewendet und dann mit dem Rest des Stapels kombiniert.
        flipped_stack = stack[:i][::-1][1:] + stack[i:]
        # Das Ergebnis des Wendevorgangs wird zurückgegeben (yield wird verwendet, um eine Generatorfunktion zu erstellen).
        yield flipped_stack

# Funktion zur Rekonstruktion des Pfades von A*-Suche. Die Funktion gibt eine Liste von Stapeln zurück, die den Pfad von der Startposition zur Zielsortierung repräsentiert.
def reconstruct_path(came_from, current):
    # Eine Liste, um den Pfad vom Anfang bis zum aktuellen Stapel zu speichern.
    path = [current]
    # Solange der aktuelle Stapel im 'came_from' Dictionary ist (d.h. er ist nicht der Startstapel), wird der Pfad rückwärts rekonstruiert.
    while current in came_from:
        # Der aktuelle Stapel wird auf den Vorgängerstapel gesetzt, der im 'came_from' Dictionary gespeichert ist.
        current = came_from[current]
        # Der Vorgängerstapel wird dem Pfad hinzugefügt.
        path.append(current)
    # Da der Pfad rückwärts rekonstruiert wurde, wird er umgedreht, um die korrekte Reihenfolge zu erhalten.
    return path[::-1]


# A*-Suche zur Sortierung von Pancake-Stapeln
def a_star_pancake_sort(stack):
    # Konvertiere den Eingabestapel in ein Tupel, um ihn unveränderlich zu machen
    start = tuple(stack)

    # Initialisiere die offene Menge mit dem Startknoten und seiner Heuristik
    open_set = [(heuristic(start), 0, start)]
    # Wörterbuch zum Speichern der Vorgänger-Knoten
    came_from = {}
    # Wörterbuch zum Speichern der g-Scores (tatsächliche Kosten vom Start zum Knoten)
    g_score = {start: 0}

    # Solange es Knoten in der offenen Menge gibt, führe die Schleife aus
    while open_set:
        # Entferne den Knoten mit dem niedrigsten f-Score (g-Score + Heuristik) aus der offenen Menge
        _, current_g_score, current = heapq.heappop(open_set)

        # Wenn der aktuelle Knoten sortiert ist, rekonstruiere den Pfad und gib ihn zurück
        if is_sorted(current):
            return reconstruct_path(came_from, current)

        # Generiere Nachbarknoten für den aktuellen Knoten
        for neighbor in successors(current):
            # Berechne den vorläufigen g-Score für den Nachbarknoten
            vorlaeufiger_g_score = current_g_score + 1

            # Wenn der vorläufige g-Score niedriger ist als der bisherige g-Score des Nachbarn oder der Nachbar noch keinen g-Score hat
            if vorlaeufiger_g_score < g_score.get(neighbor, float('inf')):
                # Aktualisiere den Vorgänger-Knoten des Nachbarn
                came_from[neighbor] = current
                # Aktualisiere den g-Score des Nachbarn
                g_score[neighbor] = vorlaeufiger_g_score
                # Berechne den f-Score des Nachbarn
                f_score = vorlaeufiger_g_score + heuristic(neighbor)
                heapq.heappush(open_set, (f_score, vorlaeufiger_g_score, neighbor))

    return None


# Funktion zum Erstellen einer Liste von Schritten und resultierenden Stapeln aus einem geordneten Pfad (von A*-Suche).
def print_steps(sorted_path):
    steps = []
    # Iteriere über den sortierten Pfad (außer dem letzten Element).
    for i in range(len(sorted_path) - 1):
        prev_state, next_state = sorted_path[i], sorted_path[i + 1]
        # Finde den Wendepunkt, der zur Umwandlung des vorherigen Stapels in den nächsten Stapel verwendet wurde.
        flipped_index = next(i for i in range(len(prev_state)) if prev_state[:i+1][::-1][1:] + prev_state[i+1:] == next_state) + 1
        # Füge den Wendepunkt und den resultierenden Stapel der Schritte hinzu.
        steps.append((flipped_index, list(next_state)))
    return steps

# Funktion zum Generieren aller möglichen Permutationen eines Stapels der Größe n.
def generate_permutations(n):
    # itertools.permutations erzeugt alle möglichen Permutationen einer Sequenz von Zahlen von 1 bis n.
    return itertools.permutations(range(1, n + 1))

# Memoisierte A* Pancake-Sortierfunktion. Die Funktion verwendet das Python-Dekorator @lru_cache, um Berechnungen zu speichern und die Leistung zu verbessern.
@lru_cache(maxsize=None)
def memoized_a_star_pancake_sort(stack):
    # Die Anzahl der Schritte wird berechnet, indem die Länge des sortierten Pfades um 1 reduziert wird (um den Startstapel nicht mitzuzählen).
    return len(a_star_pancake_sort(stack)) - 1

# Funktion zum Finden der PWUE-Nummer für n Pfannkuchen unter Verwendung von Symmetrieausnutzung, Memoisierung
def find_pwue_number(n, previous_pwue_number=None):
    max_operations = -1
    max_example = None

    stacks = list(itertools.permutations(range(1, n + 1)))

    # nutze Multithreading
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(memoized_a_star_pancake_sort, stack) for stack in stacks]

        for i, future in enumerate(futures):
            steps = future.result()
            # falls höhere A(S) gefunden wurde, aktualisiere PWUE
            if steps > max_operations or max_example is None:
                max_operations = steps
                max_example = stacks[i]
            if steps == 7:
                break
            # Abbruchbedingung, wenn die PWUE-Zahl von PWUE(n) um 1 größer als die PWUE-Zahl von PWUE(n-1) ist
            # if previous_pwue_number is not None and max_operations >= previous_pwue_number + 1:
            #     break

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



def generate_random_stack(n):
    pancake_sizes = list(range(1, n+1))
    random.shuffle(pancake_sizes)
    return pancake_sizes

def main():
    pancake_list = []
    decision = int(input("Möchten Sie die minimale Anzahl an Wende-Und-Ess-Operationen für einen Stapel ausgeben (1) oder stattdessen die PWUE-Zahl berechnen?(2) "))
    if decision == 1:
        bwinf_or_own = int (input("Möchten Sie für ein eigenes Beispiel die Anzahl an Wende-Und-Ess-Operationen berechnen (1) oder für ein BWInf-Beispiel? (2) "))
        if bwinf_or_own == 1:
            random_or_own = int (input("Möchten Sie zufällig einen Stapel generieren lassen (1) oder stattdessen einen Eigenen erstellen? (2) "))
            if random_or_own == 1:
                numbers = int(input("Wie viele Pfannkuchen soll ihr Stapel besitzen? "))
                pancake_list = generate_random_stack(numbers)
            else:
                numbers = int(input("Wie viele Pfannkuchen soll ihr Stapel besitzen? "))
                for i in range(1, numbers + 1):
                    number = int(input(str("Geben Sie Zahl " + str(i) + " ein: ")))
                    pancake_list.append(number)
        if bwinf_or_own == 2:

            file_found = False
            # solange kein gültiger Dateiname eingegeben wurde
            while not file_found:
                file_name = str(input("Geben Sie die Bezeichnung der txt-Datei mit den Pancakes an (Bsp.: pancake0.txt). \nDie Datei muss ich dafür in demselben Verzeichnis wie dieses Skript befinden.: "))
                # Datei im aktuellen Verzeichnis finden
                current_directory = os.path.dirname(os.path.abspath(__file__))
                file_path = os.path.join(current_directory, file_name)
                
                # Überprüfen, ob die Datei existiert
                if os.path.isfile(file_path):
                    pancake_list = read_pancakes_from_file(file_path)
                    file_found = True
                else:
                    print("Datei nicht gefunden. Bitte geben Sie einen gültigen Dateinamen ein.")         
        print("Ursprünglicher Stapel: ", pancake_list)
        start = time.time()
        sorted_path = a_star_pancake_sort(pancake_list)
        if sorted_path:
            steps = print_steps(sorted_path)
            print("Schritte:", len(steps))
            print("Kurzform: ", steps)
            for i, (flip_index, resulting_stack) in enumerate(steps, start=1):
                print(f"Schritt {i}: Der Pfannenwender wird unter den {flip_index}ten Pfannkuchen geschoben, umgedreht und der oberste gegessen. Resultierender Stapel: {resulting_stack}")
        else:
            print("Keine Lösung gefunden")
    else:
        pwue_num_start = int(input("Geben Sie die Anzahl n an Pfannkuchen an, ab der Sie die PWUE-Zahl berechnen wollen: "))
        pwue_num_end = int(input("Geben Sie die Anzahl n an Pfannkuchen an, bis zu welcher Sie die PWUE-Zahl berechnen wollen: "))
        start = time.time()
        calculate_pwue_numbers(pwue_num_start, pwue_num_end)

    end = time.time()
    duration = end - start
    print("Die Programmlaufzeit beträgt ", round(duration, 2), " Sekunden")

if __name__ == "__main__":
    main()
