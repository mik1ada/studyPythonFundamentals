# Zadanie 1
"""
imiona = ["Marek", "Janek", "Ola", "Basia", "Kasia"]
print(imiona[0])
print(imiona[-1])
print(len(imiona))
"""
# Zadanie 2

"""
liczby = [3, 7, 2, 10, 5]
suma = 0

for liczba in liczby:
    suma += liczba

print(suma)
"""

# Zadanie 3

"""
liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9]
listaParzyste = []

for liczba in liczby:
    if liczba % 2 == 0:
        listaParzyste.append(liczba)
print(listaParzyste)
"""

# Zadanie 4

"""
liczby = []
print("Podaj 5 liczb")
licznik = 0
sumaLiczb = 0

while licznik < 5:
    liczba = input("Podaj liczbe: ")
    if liczba.isnumeric():
        liczby.append(liczba)
        sumaLiczb += float(liczba)
        licznik += 1

srednia = sumaLiczb / len(liczby)
print(srednia)
"""

# Zadanie 5

def maksimum(lista_liczb):
    najwieksza = lista_liczb[0]
    for liczba in lista_liczb:
        if liczba > najwieksza:
            najwieksza = liczba
    return najwieksza

lista_liczb = [12, 13, 1230, 1, 0, -2]
print(maksimum(lista_liczb))