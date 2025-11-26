
# Zadanie 1

"""
tekst = input("Podaj tekst: ")
iloscOstatnichZnakow = tekst.count(tekst[-1])
print("Ostatni znak powtarza sie:", iloscOstatnichZnakow, "razy")
"""

# Zadanie 2

"""
tekst = input("Podaj tekst: ")
tekst = tekst.replace(" ", "").lower()

if(tekst == tekst[::-1]):
    print("Tekst jest palindromem")
else:
    print("Tekst nie jest palindromem")
"""

# Zadanie 3

"""
tekst = input("Podaj tekst: ")
suma_cyfr = 0

for znak in tekst:
    if znak.isdigit():
        suma_cyfr += int(znak)

print("Suma cyfr w tekscie wynosi:", suma_cyfr)
"""

# Zadanie 4
"""
tekst = input("Podaj tekst do zaszyfrowania: ")
n = int(input("Podaj klucz szyfrowania (liczbe calkowita): "))
zaszyfrowanyTekst = ""

for znak in tekst:
    poczatekAlfabetu = ord('a')
    znak_ascii = ord(znak)
    zakodowany_znak = chr(poczatekAlfabetu + (znak_ascii - poczatekAlfabetu + n) % 26)
    zaszyfrowanyTekst += zakodowany_znak
print("Zaszyfrowany tekst:", zaszyfrowanyTekst)
"""

# Zadanie 5

"""
def strToInt(str):
    znakLiczby = 1
    wynik = 0
    dlugoscTekstu = len(str)
    i = 0

    if str == "" or str[0] == "-":
        znakLiczby = -1
        i = 1
    elif str[0] == "+":
        i = 1

    while i < len(str) and str[i].isdigit():
        if(str[i].isdigit()):
            wynik = wynik * 10 + int(str[i])
            i += 1

    if i < dlugoscTekstu and str[i] == 'e':
        i += 1

        if i < dlugoscTekstu and str[i] == '-':
            return 0

        if i < dlugoscTekstu and str[i].isdigit():
            wykladnik = 0
            while i < dlugoscTekstu and str[i].isdigit():
                wykladnik = wykladnik * 10 + int(str[i])
                i += 1
            wynik *= 10 ** wykladnik

    return wynik * znakLiczby

tekst = input("Podaj tekst: ")
print(strToInt(tekst))
"""







