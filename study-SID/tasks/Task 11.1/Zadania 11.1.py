"""
# Zadanie 11

with open ('tekst.txt', 'w') as sourceFile:
    sourceFile.write("Ala ma kOTA i OSIEMNASCIE psow")

with open('tekst.txt', 'r') as sourceFile:
    text = sourceFile.read()
with open('tekst_kopia.txt', 'w') as file:
    file.write(text)

# Zadanie 12

with open('tekst.txt', 'r') as file:
    text = file.read()
slowa = text.split()
iloscSlow = len(slowa)
print(iloscSlow)
"""
"""
# Zadanie 13

with open('dane.txt', 'w') as file:
    file.write("Przykladowe\ndane\n\n\nlosowy\ntekst")

with open('dane.txt', 'r') as input_file, open('dane_bez_pustych.txt', 'w') as output_file:
    for linia in input_file:
        if linia.strip():
            output_file.write(linia)
"""
"""
# Zadanie 14

with open('produkty.csv', 'w') as file:
    file.write("Jablko,4.00\n")
    file.write("Jajka,4.50\n")
    file.write("Maka,3.00\n")
    file.write("Mleko,2.00\n")
    file.write("Brzoskwinia,9.00\n")
    file.write("Agrest,5.00\n")

print("Produkty droższe niż 4 zł")

with open('produkty.csv', 'r') as file:
    for linia in file:
        nazwa, cena = linia.strip().split(",")
        cena = float(cena)
        if cena > 4.0:
            print(f"{nazwa}, {cena} zl")
"""
"""
# Zadanie 15

with open('kwadraty.txt', 'w') as file:
    for liczba in range(1,21):
        kwadrat = liczba ** 2
        file.write(str(kwadrat) + "\n")
"""
"""
# Zadanie 16

def wczytajDane(fileName = "config.txt"):
    config = {}

    with open(fileName, "r") as file:
        for linia in file:
            print(linia.strip())

wczytajDane('config.txt')
"""
"""
# Zadanie 17

with open('plik1.txt', 'r') as fileOne, \
     open('plik2.txt', 'r') as fileTwo,  \
     open('polaczony.txt', 'w') as finalFile:
    finalFile.write(fileOne.read())
    finalFile.write("\n")
    finalFile.write(fileTwo.read())
"""
"""
# Zadanie 18

def wczytajPlikBezpiecznie(fileName):
    try:
        with open(fileName, "r") as file:
            return file.read()
    except FileNotFoundError:
        return f"Blad: Plik {fileName} nie istnieje"
    except IOError:
        return f"Blad: problem z odczytem pliku {fileName}"

fileName = "testowyPlik.txt"
print(wczytajPlikBezpiecznie(fileName))
"""
"""
# Zadanie 19
# Dopisz do pliku notatki.txt linię z numeracją: N: tekst.

with open('notatki.txt', 'w') as file:
    file.write("Przykladowe\nnotatki\nznajdujace\nsie\nw\npliku")

with open('notatki.txt', 'r') as file:
    linie = file.readlines()

with open('notatki.txt', 'w') as file:

    numerLinii = 1
    for linia in linie:
        file.write(f"{numerLinii}: {linia}")
        numerLinii += 1
"""
# Zadanie 20

with open('oceny.txt', 'w') as file:
    file.write("4.0, Maciek\n2.0, Michal\n3.0, Bogdan\n5.0, Szymon\n3.5, Zbyszek")

osoby = []
oceny = []

with open('oceny.txt', 'r') as file:
    for linia in file:
        linia = linia.strip()
        ocena, osoba = linia.split(", ")
        oceny.append(float(ocena))
        osoby.append(osoba)
srednia = sum(oceny) / len(oceny)
print(f"Srednia ocen wynosi: {srednia}")

print("Osoby z ocena wyzsza niz 3.0 to:")
for i in range(len(osoby)):
    if oceny[i] > 3.0:
        print(f"{osoby[i]}: {oceny[i]}")