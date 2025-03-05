def gauss_jordan(A, b):
    for i in range(len(A)):
        A[i].append(b[i])

    m, n = len(A), len(A[0])

    for i in range(m):
        # Finde den Pivoteintrag und tausche Zeilen falls nötig.
        max_row = max(range(i, m), key=lambda r: abs(A[r][i]))
        A[i], A[max_row] = A[max_row], A[i]

        # Nullt alle Einträge unter dem Pivoteintrag.
        for j in range(i + 1, m):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]

    # Nullt alle Einträge über dem Pivoteintrag.
    for i in range(m - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]

    # Teilt jede Zeile durch den Pivoteintrag, um Einträge auf der Diagonalen zu 1 zu setzen.
    for i in range(m):
        factor = A[i][i]
        for j in range(i, n):
            A[i][j] /= factor

    # Extrahiert die Lösung aus der letzten Spalte der erweiterten Matrix.
    x = [row[-1] for row in A]
    return x

# Beispiel:
A = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
b = [8, -11, -3]

x = gauss_jordan(A, b)
print(x)  # Ausgabe: [2.0, 3.0, -1.0]
