# ## 🔹 Zadanie 2

"""
def matrix(n):
    matrix = []
    for i in range(n):
        wiersze = []
        for j in range(n):
            wiersze.append(i * j)
        matrix.append(wiersze)
    print("Wynik:")
    for wiersz in matrix:
        print(wiersz)

matrix(5)
"""

#  Zadanie 3

"""
def passwordChecker(password):
    isThereANumber = False
    isThereAnUpper = False
    if len(password) < 8:
        return "Hasło nie spełnia warunków - za krótkie"
    for char in password:
        if char.isdigit():
            isThereANumber = True
        if char.isupper():
            isThereAnUpper = True
    if not isThereANumber:
        return "Hasło nie spełnia warunków - brak cyfry"
    if not isThereAnUpper:
        return "Hasło nie spełnia warunków - brak wielkiej litery"
    return "Hasło jest wystarczająco silne, przeszło wszystkie testy"

password = input("Podaj hasło do zweryfikowania: ")
print(passwordChecker(password))
"""

# Zadanie 5 

"""
def dictCreator(listOfStudents):
    exampleDict = {}

    for key, value in listOfStudents:
        exampleDict[key] = value

    average = sum(exampleDict.values()) / len(exampleDict)
    bestStudent = max(exampleDict, key=exampleDict.get)
    
    return average, bestStudent

listOfStudents = [('Marek', 5), ('Zbigniew', 3), ('Janusz', 4)]
average, bestStudent = dictCreator((listOfStudents))
print(f"Średnia ocen to: {average}\nNajlepszy uczeń to: {bestStudent}")
"""

# ## 🔹 Zadanie 6 .

"""
def duplicateRemover(someList):
    finalList = []
    alreadySeenList = []

    for text in someList:
        if text not in alreadySeenList:
            alreadySeenList.append(text)
            finalList.append(text)

    return finalList

someList = ['Kebab', 'Zbigniew', 123, 123, 123, 'Kebab', 'mArEk', 112, 123, 138]
print(duplicateRemover(someList))
"""

### 🔹 Zadanie 7

"""
listOfNumbers = []
sum = 0

while True:
    number = input("Wprowadz kolejna liczbe, albo q aby zakonczyc: ")
    if number == "q":
        break
    else:
        number = float(number)
        listOfNumbers.append(number)
        sum += number
average = sum / len(listOfNumbers)
minNumber = min(listOfNumbers)
maxNumber = max(listOfNumbers)
print(f"Suma wynosi: {sum}\n Srednia wynosi: {average}\n Minimum wynosi: {minNumber}\n Maksimum wynosi: {maxNumber}")
"""

"""
# ## 🔹 Zadanie 10 

exampleList = []

while True:
    action = int(input("Podaj akcje, ktora chcesz wykonac [1 - aby dodac slowo do listy, 2 - aby wyswietlic liste, 3 - aby zakonczyc program]\n"))
    if action == 3:
        break
    elif action == 2:
        print(exampleList)
    elif action == 1:
        text = input("Podaj hasło, które chcesz dodać do listy: ")
        exampleList.append(text)
"""

# ## 🔹 Zadanie 20

"""
def marks():
    dictOfMarks = {
        'bdb': 5,
        'db': 4,
        'dost': 3,
        'dst': 2,
        'ndst': 1
    }
    listOfMarks = []
    for mark in range(3):
        while True:
            grade = input(f"Podaj ocene nr {mark+1} którą chcesz wprowadzic: ").lower()
            if grade in dictOfMarks:
                valueOfMark = dictOfMarks[grade]
                listOfMarks.append(valueOfMark)
                break
            else:
                print("Niepoprawna nazwa oceny, dostępne warianty to [bdb, db, dost, dst, ndst]")
    print(f"Lista wprowadzonych ocen to: {listOfMarks}")

marks()
"""

# Zadanie z GenAI

"""
def function():
    try:
        imie = input("Podaj imię: ")
        wiek = input("Podaj wiek (liczba całkowita): ")

        # Sprawdzenie poprawności wieku
        wiek = int(wiek)

        # Zapis do pliku
        with open("dane_uzytkownika.txt", "w", encoding="utf-8") as plik:
            plik.write(f"Imię: {imie}\n")
            plik.write(f"Wiek: {wiek}\n")

        print("Dane zostały zapisane do pliku.")

    except ValueError:
        print("Błąd: Wiek musi być liczbą całkowitą!")
        return

    # Odczyt pliku
    try:
        with open("dane_uzytkownika.txt", "r", encoding="utf-8") as plik:
            zawartosc = plik.read()
            print("\nZawartość pliku:")
            print(zawartosc)

    except FileNotFoundError:
        print("Błąd: Plik nie istnieje, nie można go odczytać.")

function()
"""