import sys
sys.setrecursionlimit(10**6)



# Import txt script:
file = "X:\kaese3.txt" #Script in dem die Kaesestuecken sich befinden (relativer Pfad zu solveKaese2.py)
with open(file, "r") as f:
    text = f.read()
    text = text.split("\n")

number = int(text[0])  # Anzahl der Kaesestuecken
quader1 = []  # Kaesestuecken mit Maßen
for i in text[1:]:
    if i == '':
        break
    i = i.split(" ")
    quader1.append(sorted([int(i[0]), int(i[1])])) #Sortiert die Liste der Maße der Stuecken aufsteigend
print("Quader: ",quader1)

quader2 = [[2, 4], [2, 4], [2, 4], [2, 4], [3, 4], [3,4],[4,4], [4,6]]

def findQuader(q): #Anfangstueck finden und die Funktion tryQuader aufrufen
    quader = sorted(q.copy())
    
    row = 2 #Tiefe des Startblockes
    if quader[0] == quader[1]:
       kaese = quader[0]
       quader = quader[2:] 
    else:
        kaese = quader.pop(1) + [1]
        for row in quader[0]:
            #index des ersten elementes finden
            for i in range(row):
                pass
    
    kaese.append(row)
    quader, kaeseOut = tryquader(kaese.copy(),quader.copy())
    return [kaese[:2]]*2 + quader, kaeseOut


def findQuader2(q): #Anfangstueck finden und die Funktion tryQuader aufrufen
    quader = sorted(q.copy())
    
    for start in findMatches(quader):
        kaese = quader[start].copy()
        quader2 = quader.copy()
        # print("Start: ",kaese)
        quader2.remove(kaese)
        quader2.remove(kaese)
        kaese.append(2)
        out = tryquader(kaese.copy(),quader2.copy())
        # print("Out",out)
        if out == False: continue
        quader, kaeseOut = out
        return [kaese[:2]]*2 + quader, kaeseOut
    return False


def findMatches(quader):
    out = []
    old = [0,0]
    for i in range(0,len(quader),2):
        if quader[i] != old and (quader[i] == quader[i-1] or quader[i] == quader[i+1]):
            out.append(i)    
        old = i
    return out
            


def tryquader(kaese,quader):#Zsuammensetzen des Kaesequaders durch Rekursiven selbstaufruf
    for i in found(kaese, quader):#Liste aller passenden Stuecken durchgehen
        # Kaesequader kaese um gefundenes Stueck erweitern
        index = 2
        for g in range(2):
            if kaese[g] not in i:
                index = g
                break
        kaese[index] += 1

        quader2 = quader.copy()
        quader2.remove(i)

        # Abbruchbedingung: wenn alle Kaesetuecken verbraucht sind
        if len(quader2) == 0:
            return quader2+[i], kaese

        # Rueckgabe
        out = tryquader(kaese.copy(), quader2)
        if out == False:
            continue
        quaderOut, kaeseOut = out #Rueckgabe der Ausgabe des naechsten Rekursionsschrittes
        quaderOut.insert(0, i)
        return quaderOut, kaeseOut #Rueckgabe bisheriger Schritte

    
    return False

def found(kaese, quader):
    kaese = sorted(kaese.copy())
    out = []
    if kaese[:2] in quader: #kleinstes Stueck
        out.append(kaese[:2].copy())
    if [kaese[0], kaese[2]] in quader: #naechst kleinste Stueck
        out.append([kaese[0], kaese[2]])
    elif kaese[1:] in quader: #falls nur 1 passendes Stueck vorhande fuege groeßtes Stueck hinzu
        out.append(kaese[1:].copy())
    return out

#out, q= findQuader(quader1.copy())
sequence2, q2 = findQuader2(quader1.copy())
#print("1: ",out,"  q: ",q)
print("Reihenfolge: ",sequence2,"  q2: ",q2)

