# Zadanie 1
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def przedstaw_sie(self):
        print(f"Cześć, jestem {self.name} i mam {self.age} lat")

    def __str__(self):
    return f"Student o imieniu {self.name} w wieku {self.age} lat"

student1 = Student("Tomek", 23)
student2 = Student("Bronisław", 60)

student1.przedstaw_sie()
student2.przedstaw_sie()
"""
# Zadanie 2
"""
class Prostokat:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def pole(self):
        return self.a * self.b

    def obwod(self):
        return self.a * 2 + self.b * 2

prostokat1 = Prostokat(2, 4)
prostokat2 = Prostokat(3, 5)

print(prostokat1.pole())
print(prostokat1.obwod())
print(prostokat2.pole())
print(prostokat2.obwod())
"""

# Zadanie 3
"""
class KontoBankowe():

    def __init__(self, saldo):
        self._saldo = saldo

    def wplata(self, kwota):
        if kwota > 0:
            self._saldo += kwota
            print("Wplata zakonczona powodzeniem")
        else:
            print("Kwota wplaty nie moze byc mniejsza niz 0")

    def wyplata(self, kwota):
        if kwota < self._saldo:
            self._saldo -= kwota
            print("Wyplata zakonczona powodzeniem")
        elif kwota < 0:
            print("Kwota wyplaty mniejsza niz 0 - brak mozliwosci wyplaty")
        else:
            print("Brak wystarczajacych srodkow na koncie")

    def saldo(self):
        return self._saldo

kontoBankowe1 = KontoBankowe(10000)
print(kontoBankowe1.saldo())
kontoBankowe1.wyplata(9999)
print(kontoBankowe1.saldo())
kontoBankowe1.wplata(12000000)
print(kontoBankowe1.saldo())
"""

# Zadanie 4
"""
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

punkt1 = Punkt(0, 7)
punkt2 = Punkt(5, 7)

print(punkt1)
print(punkt2)
"""

# Zadanie 5
"""
class Zwierze:
    def glos(self):
        return "???"

class Pies(Zwierze):
    def glos(self):
        return "Hau"

class Kot(Zwierze):
    def glos(self):
        return "Miau"

listaZwierzat = [Kot(), Pies(), Zwierze()]

for zwierze in listaZwierzat:
    print(zwierze.glos())
"""

# Zadanie 6

"""
class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def __str__(self):
        return f"Imie: {self.imie}, Nazwisko: {self.nazwisko}"

class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja):
        super().__init__(imie, nazwisko)
        self.pensja = pensja

    def __str__(self):
        return super().__str__() + f", Pensja: {self.pensja} zł"

osoba1 = Osoba("Marek", "Zbyszewski")
pracownik1 = Pracownik("Zdzisław", "Boguszewicz", 5000)

print(osoba1)
print(pracownik1)
"""

# Zadanie 7

"""
class Silnik:
    def __init__(self, moc):
        self.moc = moc

    def __str__(self):
        return f"{self.moc} KM"
class Samochod:
    def __init__(self, silnik, marka):
        self.silnik = silnik
        self.marka = marka

    def opis(self):
        return f"Samochod marki {self.marka} o mocy silnika {self.silnik}"

silnik1 = Silnik(500)
wuz1 = Samochod(silnik1, "Audi")

print(wuz1.opis())
"""
"""
# Zadanie 8

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def przedstaw_sie(self):
        print(f"Cześć, jestem {self.name} i mam {self.age} lat")

    def __str__(self):
        return f"Student o imieniu {self.name} w wieku {self.age} lat"

class Druzyna:
    def __init__(self):
        self.lista = []

    def dodaj(self, student):
        self.lista.append((student))

    def wypisz(self):
        for student in self.lista:
            print(student)

student1 = Student("Maciek", 28)
student2 = Student('Magda', 85)
student3 = Student('Michał', 578)

druzyna1 = Druzyna()
druzyna1.dodaj(student1)
druzyna1.wypisz()
druzyna1.dodaj(student2)
druzyna1.dodaj(student3)
druzyna1.wypisz()
"""

# Zadanie 9
"""
import math

def obliczSumePol(listaFigur):
    sumaFigur = 0
    for figura in listaFigur:
        sumaFigur += figura.pole()
    return sumaFigur
class Figura:
    def __init__(self, wymiar):
        self.wymiar = wymiar

    def pole(self):
        self.pole_value = 0

class Kolo(Figura):
    def __init__(self, promien):
        super().__init__(promien)

    def pole(self):
        return math.pi * self.wymiar * self.wymiar

class Prostokat(Figura):
    def __init__(self, wymiar1, wymiar2):
        super().__init__(wymiar1)
        self.wymiar2 = wymiar2

    def pole(self):
        return self.wymiar * self.wymiar2

listaFigur = [Kolo(5), Kolo(7), Prostokat(6, 6)]
print(obliczSumePol(listaFigur))
"""

# Zadanie 10

class ElementZamowienia:

    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def obliczCene(self):
        if self.amount >= 5:
            return self.price * self.amount * 0.9
        else:
            return self.price * self.amount

    def __str__(self):
        return f"{self.name} | Cena: {self.price} zł | Sztuk: {self.amount}"

class Zamowienie:
    def __init__(self):
        self.elementy = []

    def dodajElement(self, element):
        self.elementy.append(element)

    def obliczCaloscCeny(self):
        suma = 0
        for element in self.elementy:
            suma += element.obliczCene()
        return suma

    def wypiszPodsumowanie(self):
        print("Podsumowanie zamowienia:")
        for element in self.elementy:
            print(element)
        print(f"Calkowity koszt zamowienia wynosi: {self.obliczCaloscCeny()} zł")

element1 = ElementZamowienia("Laptop", 2500, 3)
element2 = ElementZamowienia("Smartfon", 1500, 6)
element3 = ElementZamowienia("Tablet", 800, 1)

zamowienie = Zamowienie()
zamowienie.dodajElement(element1)
zamowienie.dodajElement(element2)
zamowienie.dodajElement(element3)

zamowienie.wypiszPodsumowanie()