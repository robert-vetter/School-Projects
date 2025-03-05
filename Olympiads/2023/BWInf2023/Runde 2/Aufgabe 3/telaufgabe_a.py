import os

def read_pancakes_from_file(filename):
    with open(filename, "r") as file:
        num_pancakes = int(file.readline())
        pancakes = [int(line.strip()) for line in file.readlines()]
    return pancakes

def sortiert(liste):
    for i in range(len(liste)-1):
        if liste[i] > liste[i+1]:
            return False
    return True

def umgedreht_sortiert(liste):
    normal = liste[::-1]
    for i in range(len(normal)-1):
        if normal[i] > normal[i+1]:
            return False
    return True

def gns_element(liste):
    '''Gibt das größte, nicht sortierte Element einer Liste zurück, die nach unten aufsteigend sortiert werden soll'''
    groesste = 0
    gns = 0
    for i in range(len(liste)):
        if liste[i] >= groesste:
            groesste = liste[i]
        else:
            if liste[i] >= gns:
                gns = liste[i]
    return gns

def umdrehen_entfernen(liste):
    '''Wendet den Stapel Pfannkuchen gemäß der Aufgabenstellung'''
    stelle_umdrehen = 0
    for i in range(len(liste)):
        if liste[i] == gns_element(liste):
            stelle_umdrehen = i
    umgedreht = liste[0:stelle_umdrehen]
    entfernt = umgedreht[::-1] + liste[stelle_umdrehen+1:]
    return entfernt 

def subgroups(liste):  
    counter = 0
    subgruppen = []
    for i in range(len(liste)):
        if i == 0:
            counter += 1
            continue
        if liste[i] > liste[i-1]:
            counter += 1
        else:
            subgruppen.append(counter)
            counter = 1
    subgruppen.append(counter)
    return subgruppen

def pancake_sort(liste):
    counter = 0
    neue_liste = liste
    steps = []
    while not sortiert(neue_liste):
        if umgedreht_sortiert(neue_liste):
            counter += 1
            steps.append((0, neue_liste[::-1][1:]))
            neue_liste = neue_liste[::-1][1:]
        else:
            neue_liste, step = pancake_sort_subgroups(neue_liste)
            steps.append(step)
            counter += 1

    return "Sortierte Liste:", neue_liste, "Schritte:", counter, "Steps:", steps

def pancake_sort_subgroups(liste):
    neue_liste = liste
    counter = 0
    summe = 0
    subgruppen = subgroups(neue_liste)
    step = None

    for i in range(len(subgruppen)-1):
        umgedrehte_subgruppen = subgruppen[::-1]
        if umgedrehte_subgruppen[i] == min(umgedrehte_subgruppen) and umgedrehte_subgruppen[i+1] > umgedrehte_subgruppen[i]:
            for j in range(len(subgruppen)):
                if j == (len(subgruppen)-i-1):
                    summe += subgruppen[j]
                    break
                summe += subgruppen[j]

            neue_liste, step = umdrehen_entfernen_stelle(neue_liste, summe-1)
            counter += 1
            break

    if counter == 0:
        neue_liste, step = umdrehen_entfernen_stelle(neue_liste, 0)

    return neue_liste, step

def umdrehen_entfernen_stelle(liste, stelle):
    umgedreht = liste[0:stelle]
    entfernt = umgedreht[::-1] + liste[stelle+1:]
    step = (stelle, entfernt)
    return entfernt, step
                        
filename = "pancake7.txt"
current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, filename)
pancake_list = read_pancakes_from_file(file_path)
print("Ursprünglicher Stapel: ", pancake_list)
print(pancake_sort(pancake_list))
