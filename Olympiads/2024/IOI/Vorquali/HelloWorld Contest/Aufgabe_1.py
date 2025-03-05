names = []

t = int(input("").strip())

while not (1 <= t <= 20):
    print("Beachte: 1 <= t <= 20")
    t = int(input("").strip())

for i in range(0, t):
    s = input().strip()
    while not (1 <= len(s) <= 100) or not s.isalpha():
        print("Beachte: Name muss mindestens einen und darf maximal 100 Groß- und Kleinbuchstaben beinhalten.")
        s = input().strip()
    names.append(s)

for i in range(0, len(names)):
    print(f"Case #{i+1}: Hello {names[i]}!")

