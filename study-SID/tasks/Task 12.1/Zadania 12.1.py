import datetime
import math
import json
import re

# Zadanie 1
"""
def daysSinceBirthday(birthDate):
    try:
        birthDate = datetime.datetime.strptime(birthDate, "%Y-%m-%d")
        currentDate = datetime.datetime.now()
        daysSinceBirthday = (currentDate - birthDate).days
        return(f"Liczba dni od daty urodzenia: {daysSinceBirthday}")
    except ValueError:
        return("Nieprawidłowy format daty. Użyj formatu YYYY-MM-DD.")
    

birthDate = input("Podaj date urodzenia w formacie YYYY-MM-DD: ")
print(daysSinceBirthday(birthDate))
"""

# Zadanie 2
"""
currentDate = datetime.datetime.now()
n = int(input("Podaj liczbe dni n: "))
previousDate = (currentDate - datetime.timedelta(days=n)).strftime('%Y-%m-%d')
futureDate = (currentDate + datetime.timedelta(days=n)).strftime('%Y-%m-%d')
print(f"Data dzisiejsza: {currentDate.strftime('%Y-%m-%d')}\nData sprzed {n} dni: {previousDate}\nData za {n} dni: {futureDate}")
"""

# Zadanie 3
""""
radius = float(input("Podaj promień koła: "))
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print(f"Pole koła wynosi: {area}, obwód kołą wynosi: {circumference}")
"""

# Zadanie 4
"""
x = float(input("Podaj wartość x: "))

if x < 0:
    print("Błąd, x musi być większe bądź równe 0")
else:
    xSqrt = math.sqrt(x)
    print(f"Pierwiastek kwadratowy z {x} wynosi: {xSqrt}")
"""

# Zadanie 5
"""
name = input("Podaj imię: ")
age = int(input("Podaj wiek: "))

jsonData = {
    "name": name,
    "age": age
}
with open('profil.json', 'w') as jsonFile:
    json.dump(jsonData, jsonFile)
    jsonFile.close()
"""

# Zadanie 6
"""
try:
    with open('profil.json', 'r') as jsonFile:
        jsonData = json.load(jsonFile)
        print(f"Użytkownik {jsonData['name']} ma {jsonData['age']} lat.")
        jsonFile.close()
except FileNotFoundError:
    print("Plik profil.json nie istnieje.")
"""

# Zadanie 7
"""
postalCode = input("Podaj kod pocztowy w formacie XX-XXX: ")
pattern = r'\d{2}-\d{3}'

if re.fullmatch(pattern, postalCode):
    print("OK")
else:
    print("BŁĄD")
"""

# Zadanie 8
"""
phrase = input("Podaj zdanie: ")
numbers = re.findall(r'-?\d+', phrase)

for number in numbers:
    print(number)
"""

# Zadanie 9
"""
listOfNames = ["Anna", "Krzysztof", "Monika", "Tomasz", "Zofia", "Jan"]
iterator = iter(listOfNames)

while True:
    try:
        name = next(iterator)
        print(name)
    except StopIteration:
        break
"""

# Zadanie 10

def Iterator(n):
    while n >= 0:
        yield n
        n -= 1

for liczba in Iterator(10):
    print(liczba)