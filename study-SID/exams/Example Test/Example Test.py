# Zadanie 1

"""
def createMatrix(n, text):
  matrix = []
  for i in range(n):
    wiersz = []
    for j in range(n):
      if i == j or i + j == n - 1:
        wiersz.append(text)
      else:
        wiersz.append((i+j) ** 2)
    matrix.append(wiersz)
  return(matrix)

n = int(input("Podaj rozmiar macierzy n x n: "))
text = input("Podaj napis który ma być wyświetlany w przekątnych macierzy: ")

matrix = createMatrix(n, text)

for wiersz in matrix:
  print(wiersz)
"""

# Zadanie 2

"""
def isPasswordStrong(password):

  if len(password) >= 8:
    return 'Hasło jest silne'
  else:
    return 'Hasło jest słabe'
  
isUserLogged = False

while not isUserLogged:
  password = input("Podaj hasło: ")
  password2 = input("Podaj ponownie hasło: ")
  if password == password2:
    print("Gratulacje zostałeś zalogowany, teraz zostanie zweryfikowana siła twojego hasła.")
    isUserLogged = True
  else:
    print("Hasła różnią się od siebie, spróbuj ponownie.")

strongOfPassword = isPasswordStrong(password)
print("Oto wynik weryfikacji siły twojego hasła: " + strongOfPassword)
"""

# Zadanie 3

"""
def marks():
  marks = {
    'niedostateczny': 2,
    'dostateczny': 3,
    'dostatecznyplus': 3.5,
    'dobry': 4,
    'dobryplus': 4.5,
    'bardzodobry': 5
  }

  listOfMarks = []

  for ocena in range(3):
    while True:
      wpis = input("Podaj słownie ocene: ").lower()
      if wpis in marks:
        listOfMarks.append(marks[wpis])
        break
      else:
        print("Wprowadzona niepoprawną nazwę oceny, spróbuj ponownie.\n Dostępne nazwy to [niedostateczny, dostateczny, dostatecznyplus, dobry, dobryplus, bardzodobry]")
  highestMark = max(listOfMarks)
  print("Lista ocen:", listOfMarks)
  print("Najwyższa ocena:", highestMark)   

marks()
"""

# Zadanie 4

"""
def oddAndEvenNumbers(listOfNumbers):
  sum = 0

  for number in listOfNumbers:
    if number % 2 == 0:
      smallest = number
      highest = number
      break

  for number in listOfNumbers:
    if number % 2 != 0:
      sum += number
    elif number > highest:
      highest = number
    elif number < smallest:
      smallest = number

  return sum, smallest, highest

listOfNumbers = [1, 123, 324, 120, 43, -23, -423]
sum, smallest, highest = oddAndEvenNumbers(listOfNumbers)
print(f"Najmniejsza liczba parzysta to: {smallest}, najwieksza liczba parzysta to: {highest}, suma liczb nieparzystych to {sum}")
"""

# Zadanie 5

"""
def isPalindrom(word):
  reversedWord = ""
  for char in word:
    reversedWord = char + reversedWord

  if reversedWord == word:
    return "Palindrom"
  else:
    return "Nie palindrom"
  
word = input("Podaj słowo, aby sprawdzić czy jest palindromem: ")
result = isPalindrom(word)
print("Wynik to: " + result)
"""

# Zadanie 6

names = []
lengths = {}

count = int(input("Ile imion chcesz podać? "))

for i in range(count):
    name = input("Podaj imię: ")
    names.append(name)

for name in names:
    lengths[name] = len(name)

longest = names[0]

for name in names:
    if lengths[name] > lengths[longest]:
        longest = name

file = open("wynik.txt", "w")

for name in lengths:
    file.write(name + " - " + str(lengths[name]) + "\n")

file.write("Najdłuższe imię: " + longest)
file.close()