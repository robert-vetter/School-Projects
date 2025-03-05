import os

def read_pancakes_from_file(filename):
    with open(filename, "r") as file:
        num_pancakes = int(file.readline())
        pancakes = [int(line.strip()) for line in file.readlines()]
    return pancakes

# ist Liste aufsteigend sortiert
def sortiert(liste):
    for i in range(len(liste)-1):
        if liste[i] > liste[i+1]:
            return False
    return True

#ist Liste in umgedrehter Reihenfolge sortiert
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
    return (entfernt, stelle_umdrehen+1) 

def pancake_sort(liste):
    counter = 0
    neue_liste = liste
    schritte = []

    for i in range(len(liste)):
        if sortiert(neue_liste) == True:
            return ("Sortierte Liste:", neue_liste, "Schritte:", counter, "Umformungsschritte:", schritte)

        if umgedreht_sortiert(neue_liste) == True:
            counter += 1
            neue_liste = neue_liste[::-1]
            schritte.append((0, neue_liste[:])) 
            return ("Sortierte Liste:", neue_liste[1:], "Schritte:", counter, "Umformungsschritte:", schritte)

        else:
            neue_liste, pos = umdrehen_entfernen(neue_liste)
            schritte.append((pos, neue_liste[:])) 
        counter += 1

filename = "pancake0.txt"
current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, filename)
pancake_list = read_pancakes_from_file(file_path)
print("Ursprünglicher Stapel: ", pancake_list)
print(pancake_sort(pancake_list))
