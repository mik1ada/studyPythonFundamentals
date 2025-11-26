# Zadanie 1

"""
dni_tygodnia = ("Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela")
drugi_dzien = dni_tygodnia[1]
przedostatni_dzien = dni_tygodnia[-2]

print("Drugi dzień tygodnia:", drugi_dzien)
print("Przedostatni dzień tygodnia:", przedostatni_dzien)
"""

# Zadanie 2

"""
dane_osobowe = ("Jan", "Kowalski", 30)
imie = dane_osobowe[0]
nazwisko = dane_osobowe[1]
wiek = dane_osobowe[2]

print(f"Imie: {imie}, Nazwisko: {nazwisko}, Wiek: {wiek}")
"""

# Zadanie 3

"""
liczby = (4, 7, 1, 3, 9)
suma = 0

for liczba in liczby:
    suma += liczba

print(suma)
"""

# Zadanie 4

"""
imiona = ("Ala", "Ola", "Jan")
numer = 1

for imie in imiona:

    print(f"Imie: {imie}, numer porzadkowy imienia to: {numer}")
    numer += 1
"""

# Zadanie 5

"""
a = 5
b = 10
liczby = (5, 10)

a = liczby[1]
b = liczby[0]

print(f"Wartosc a: {a}, wartosc b: {b}")
"""

# Zadanie 6

"""
def obliczanieKwadratuOdleglosci(x, y):
    kwadratOdleglosci = x**2 + y**2
    return kwadratOdleglosci

x = float(input("Podaj wspolrzedna x: "))
y = float(input("Podaj wspolrzedna y: "))
print(obliczanieKwadratuOdleglosci(x, y))
"""

# Zadanie 7

"""
wynikiTestu = [("Ala", 80), ("Ola", 45), ("Jan", 60), ("Kasia", 30)]
for imie, wynik in wynikiTestu:
    if wynik >= 50:
        print(imie)
"""

# Zadanie 8

"""
def ktoryNajtanszy(produkty):
    najtanszy = produkty[0]

    for produkt in produkty:
        if produkt[1] < najtanszy[1]:
            najtanszy = produkt
    return najtanszy

produkty = [("chleb", 4.0), ("mleko", 3.5), ("masło", 7.0), ("ser", 6.5)]
print(ktoryNajtanszy(produkty))
"""

# Zadanie 9

"""
litery = ('b', 'a', 'n', 'a', 'n')
iloscWystapien = 0

for litera in litery:
    if 'a' == litera:
        iloscWystapien += 1
print(f"Ilosc wystapien: {iloscWystapien}")
"""

# Zadanie 10

k = (1, 2, 3)
nowaKrotka = k + (4,)
print(nowaKrotka)





