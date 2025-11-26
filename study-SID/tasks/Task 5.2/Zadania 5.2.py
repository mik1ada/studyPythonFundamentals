#  Zadanie 1

"""
oceny = [3, 4, 5, 2, 5]

sumaOcen = 0
for ocena in oceny:
    sumaOcen += ocena

srednia = sumaOcen / len(oceny)
print(srednia)
if(srednia < 3.0):
    print("Uczen ma slabe wyniki")
elif(srednia < 4.5):
    print("Uczen ma dobre wyniki")
else:
    print("Uczen ma bardzo dobre wyniki")
"""

# Zadanie 2

"""
ksiazka = {
    "tytul": "Jadro ciemnosci",
    "autor": "Jan Brzoza",
    "liczba_stron": 20
}

print(f"Tytul: {ksiazka['tytul']}, Autor: {ksiazka['autor']}, Liczba stron: {ksiazka['liczba_stron']}")
"""

#  Zadanie 3

"""
uzytkownik = {
     "login": "admin",
     "haslo": "tajne",
     "aktywny": True
 }

if uzytkownik['aktywny'] == True:
    print("Uzytkownik jest aktywny")
else:
    print("Uzytkownik jest zablokowany")
"""

# Zadanie 4

"""
def pole_kola(r):
    pi = 3.14
    pole = pi * r ** 2
    return pole

r = 5
print(pole_kola(r))
"""

# Zadanie 5

"""
tekst = input("Podaj tekst: ")
licznikLiter = 0

for char in tekst:
    if char == 'e':
        licznikLiter += 1
print(licznikLiter)
"""

# Zadanie 6

"""
liczby = [3, -1, 0, 5, -2, 10]
liczbyDodatnie = 0
liczbyUjemne = 0
zera = 0


for liczba in liczby:
    if liczba > 0:
        liczbyDodatnie += 1
    elif liczba < 0:
        liczbyUjemne += 1
    else:
        zera =+ 1
print(f"Liczby dodatnie: {liczbyDodatnie}, liczby ujemne:{liczbyUjemne}, zera:{zera}")
"""

# Zadanie 7

"""
def obliczanieCenyBrutto(produkt):
    cenaNetto = produkt['cena_netto']
    vat = produkt['vat']
    cenaBrutto = cenaNetto * (1 + vat)
    return cenaBrutto

produkt = {
     "nazwa": "Monitor",
     "cena_netto": 1000.0,
     "vat": 0.23
 }

cenaBrutto = obliczanieCenyBrutto(produkt)

print(f"Produkt: {produkt['nazwa']}, cena brutto: {cenaBrutto}")
"""

# Zadanie 8

"""
napis = input("Podaj tekst do odwrocenia: ")
odwroconyNapis = ""

for char in napis:
    odwroconyNapis = char + odwroconyNapis
print(odwroconyNapis)    
"""

#  Zadanie 9

"""
liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for liczba in liczby:
    if liczba % 5 == 0 and liczba % 3 == 0:
        print("FizzBuzz")
    elif liczba % 3 == 0:
        print("Fizz")
    elif liczba % 5 == 0:
        print("Buzz")
    else:
        print(liczba)
"""

# Zadanie 10

uczniowie = [
     {"imie": "Ala", "wiek": 15},
     {"imie": "Bartek", "wiek": 17},
     {"imie": "Ola", "wiek": 16},
     {"imie": "Jan", "wiek": 18}
 ]

for uczen in uczniowie:
    if uczen['wiek'] >= 17:
        print(uczen['imie'])