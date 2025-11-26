"""
# Zadanie 1

with open('powitanie.txt', 'w') as file:
    file.write("Witaj w świecie Pythona!")

# Zadanie 2

with open('powitanie.txt', 'r') as file:
    print(file.read())

# Zadanie 3

with open('powitanie.txt', 'a') as file:
    file.write("\nDruga linijka tekstu")

# Zadanie 4
"""
"""
with open('imiona.txt', 'w') as file:
    imiona = ["Ala", "Ola", "Jan"]
    for imie in imiona:
        file.write(imie + "\n")

# Zadanie 5

liczbaLini = 0
with open('imiona.txt', 'r') as file:
    for linia in file:
        if linia.strip():
            liczbaLini += 1
    print(liczbaLini)
"""
"""
# Zadanie 6

with open('liczby.txt', 'w') as file:
    file.write("12\n14\n123\n87\n-53")

suma = 0
with open('liczby.txt', 'r') as file:
    for linia in file:
        suma += float(linia.strip())
    print(suma)
"""
"""
# Zadanie 7

filmy = []

while len(filmy) < 3:
    film = input("Podaj nazwe ulubionego filmu: ")
    filmy.append(film)

with open('filmy.txt', 'w') as file:
    for film in filmy:
        file.write(film + "\n")
"""
"""
# Zadanie 8

def dopiszLog(log, user = "Unknown"):

    dateAndTime = input("Wprowadz date i godzine logu zachowujac kolejnosc RRRR-MM-DD HH:MM:SS ")
    log = f"[{dateAndTime}] {log} [{user}]\n"
    with open('log.txt', 'a') as file:
        file.write(log)

dopiszLog("Uruchomiono komputer", "admin")
dopiszLog("Użytkownik zalogowal sie", "stefan")
dopiszLog("Blad systemu")

# Zadanie 9

with open('log.txt', 'r') as file:
    for linia in file:
        if "Użytkownik" in linia:
            print(linia.strip())
"""

# Zadanie 10

with open('tekst.txt', 'w') as file:
    file.write("AlA ma kota i TRZYNASCIE psow")

with open('tekst.txt', 'r') as file:
    text = file.read()
    textUpper = text.upper()
with open('tekst.txt', 'w') as file:
    file.write(textUpper)
