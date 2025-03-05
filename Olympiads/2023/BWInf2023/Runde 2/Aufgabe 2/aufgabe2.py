import os

# Funktion zum importieren der Datei
def importFile(file):
    slices = []
    with open(file, "r") as f:
        lines = f.readlines()
        number_of_slices = float(lines[0])
        for line in range(1, len(lines)):
            slices.append(lines[line].strip().split(" "))
        for i in range(0, len(slices)):
            for j in range(0,2):
                slices[i][j] = float(slices[i][j])
    return number_of_slices, slices

# Hauptfunktion zum ermitteln der Lösung
def backtracking(file):
    # Importieren der Datei und deklarierung der Variabel slices, die alle Scheiben enthält und number_of_slices, die die Anzahl der Scheiben speichert
    imported = importFile(file)
    number_of_slices = imported[0]
    slices = imported[1]
    print(slices)
    
    # neuer Käse wird initiiert
    cheese = cheeseBlock()
    # erstes Element der scheibenliste wird zu dem Käse hinzugefügt und aus der Scheibenliste entfertn
    cheese.addSlice(slices[0], "FRONT")
    slices.pop(0)
    # Liste, die für jeden Schritt speichert, welche Scheiben bereits überprüft wurden
    checkedSlices = [[], []]
    # wiederhole solange noch nicht alle Scheiben dem Käse hinzugefügt wurden
    while len(cheese.addedSlices) < number_of_slices:
        # nächste scheibe, die hinzugefügt wird, wird ausgewählt (muss an den Käse passen und darf nicht in den bereits überprüften der letzten Ebene sein)
        nextSlice = None
        for slice in slices:
            if cheese.checkSlice(slice) != None and slice not in checkedSlices[-1]:
                nextSlice = slice
                break
        # falls keine scheibe gefunden wurde
        if nextSlice == None:
            # füge die letzte Scheibe wieder zu der Scheibenliste hinzu
            slices.append(cheese.addedSlices[-1])
            # entferne den letzten Eintrag aus der Überprüfungsliste
            checkedSlices.pop()
            # Füge die Scheibe zu den bereits besuchten Scheiben der letzten Ebene hinzu
            checkedSlices[-1].append(cheese.addedSlices[-1])
            # Entferne die Scheibe vom Käse
            cheese.removeSlice()
            # Falls der Käse keine Scheiben mehr hat, wähle eine neue Start-Scheibe, die nicht in den bereits überprüften Scheibe ist
            if cheese.addedSlices == []:
                for slice in slices:
                    if slice not in checkedSlices[-1]:
                        cheese.addSlice(slice, "TOP")
                        checkedSlices += [[]]
                        break
                # wenn dies nicht möglich ist, gibt es keine Lösung
                if cheese.addedSlices == []:
                    return None
        # falls eine Scheibe gefunden wurde
        else:
            # Füge eine neue Ebene zur Überprüfungsliste hinzu
            checkedSlices += [[]]
            # Füge die Scheibe dem Käse hinzu
            position = cheese.checkSlice(nextSlice)
            cheese.addSlice(nextSlice, position)
            # entferne die Scheibe aus der Liste der übrigen Scheiben
            slices.remove(nextSlice)

    # Ausgabe der Scheiben, die zum Käse hinzugefügt wurden (Umkehren der Reihenfolge entspricht Reihenfolge des Abschneidens) 
    return cheese.addedSlices

# Klasse für den Käse
class cheeseBlock():
    def __init__(self):
        # Bereits hinzugefügte Scheiben, zu Beginn leer
        self.addedSlices = []
        # Maße des Käses in Millimeter
        self.height = 0 #Höhe
        self.width = 0  #Breite
        self.length = 0 #Tiefe

    # Methode, mit der eine Scheibe an einer der drei Seiten des Käses hinzugefügt wird und die Maße entsprechend angepasst werden
    def addSlice(self, slice, position):
        if self.addedSlices == []:
            self.addedSlices += [slice]
            self.height = slice[1]
            self.width = slice[0]
            self.length += 1
        else:
            self.addedSlices += [slice]
            if position == "TOP":
                self.height += 1
            elif position == "SIDE":
                self.width += 1
            elif position == "FRONT":
                self.length += 1
    
    # Methode, die die zuletzt hinzugefügte Scheibe wieder vom Käse entfernt und die Maße des Käses anpasst
    def removeSlice(self):
        position = self.checkSlice(self.addedSlices[-1])
        self.addedSlices.pop()
        if position == "TOP":
            self.height -= 1
        elif position == "SIDE":
            self.width -= 1
        elif position == "FRONT":
            self.length -= 1

    # Methode, die bei einer gegenen Scheibe ermittelt, ob diese an den Käse passt und wenn ja an welcher Seite des Käses, wenn nein gibt sie None aus
    def checkSlice(self, slice):
        if (self.width == slice[0] and self.length == slice[1]) or (self.width == slice[1] and self.length == slice[0]):
            position = "TOP"
        elif (self.length == slice[0] and self.height == slice[1]) or (self.length == slice[1] and self.height == slice[0]):
            position = "SIDE"
        elif (self.width == slice[0] and self.height == slice[1]) or (self.width == slice[1] and self.height == slice[0]):
            position = "FRONT"
        else:
            return None
        return position

filename = "kaese1.txt"
current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, filename)
loesung = backtracking(file_path)

# Ausgabe der Lösung
if loesung == None:
    print("Aus den gegeben Scheiben kann kein Quader, der alle Scheiben enthält, zusamengesetzt werden")
else:
    loesung.reverse()
    print("In folgender Reihenfolge wurden die Scheiben von dem Käse abgschnitten:")
    for scheibe in loesung:
        print(scheibe[0], scheibe[1])