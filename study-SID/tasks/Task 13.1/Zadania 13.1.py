# Zadanie 1

"""
firstNumber = float(input("Podaj pierwsza liczbe:"))
secondNumber = float(input("Podaj druga liczbe:"))

try:
    division = firstNumber / secondNumber
    print("Wynik dzielenia to", division)
except ZeroDivisionError:
    print("Błąd - nie można dzielić przez zero")
"""

# Zadanie 2
"""
try:
    number = float(input("Podaj liczbe:"))
    print("Podana liczba to:", number)
except ValueError:
    print("Błąd - podano tekst nie będący liczbą.")
"""
# Zadanie 3

"""
nameOfFile = input("Podaj nazwe pliku ktory chcesz otworzyc:")

try:
    with open(nameOfFile, 'r') as file:
        content = file.read()
        print("Zawartosc pliku to:", content)
except FileNotFoundError:
    print("Błąd - plik o nazwie", nameOfFile, "nie zostal znaleziony")
"""
# Zadanie 4
"""
listOf5Elements = [0, 13, -213, "losowa tresc", True]

try:
    index = int(input("Podaj numer indeksu ktory chcesz wczytac:"))
    print(listOf5Elements[index])
except ValueError:
    print("Blad - podana wartosc to nie jest liczba calkowita")
except IndexError:
    print("Blad - proba wczytania indeksu poza zasiegiem listy (od 0 do 4)")
"""
#  Zadanie 5

"""
try:
    firstNumber = float(input("Podaj pierwsza liczbe:"))
    secondNumber = float(input("Podaj druga liczbe:"))

    division = firstNumber / secondNumber
    print("Wynik dzielenia to", division)
except ZeroDivisionError:
    print("Błąd - nie można dzielić przez zero")
except ValueError:
    print("Blad - podane wartosci to nie sa liczby")
"""

# Zadanie 6

"""
try:
    number = float(input("Podaj liczbe:"))

    squareOfNumber = number ** 2
    print("Kwadrat podanej liczby to:", squareOfNumber)
except (ValueError, TypeError) as e:
    print("Błąd: Podano niewłaściwą wartość! Upewnij się, że podałeś liczbę.")
"""

#  Zadanie 7

"""
def checkAge(wiek):
    if wiek < 0:
        raise ValueError("wiek nie moze byc mniejszy niz 0")
    else:
        print("Twoj wiek to", wiek, "lat")

try:
    wiek = int(input("Podaj swoj wiek jako wartosc calkowita:"))
    checkAge(wiek)
except ValueError as e:
    print("Błąd -", e)
"""

# Zadanie 8

"""
try:
    firstNumber = float(input("Podaj pierwsza liczbe:"))
    secondNumber = float(input("Podaj druga liczbe:"))

    division = firstNumber / secondNumber
    print("Wynik dzielenia to", division)
except ZeroDivisionError:
    print("Błąd - nie można dzielić przez zero")
except ValueError:
    print("Blad - podane wartosci to nie sa liczby")
finally:
    print("Dziekuje za skorzystanie z kalkulatora dzielenia dwoch liczb")
"""

#  Zadanie 9

""""
nameOfFile = input("Podaj nazwe pliku do wczytania: ")

try:
    with open(nameOfFile, 'r') as file:
        number = file.read()
        number = int(number)
        print("Typ po skonwertowaniu to:", type(number), "a liczba to:", number)

except FileNotFoundError:
    print("Blad - plik nie znaleziony")
except ValueError:
    print("Blad - wartosc w pliku nie jest liczba")
"""

# Zadanie 10

try:
    password = input("Wprowadz haslo: ")
    if(len(password) < 8):
        raise Exception("password too short (at least 8 chars)")
    else:
        print("Haslo zostalo wprowadzone do systemu")
except Exception as e:
    print("Blad -", e)