
# Zadanie 1
"""
class Wektor:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def dlugosc(self):
        return (self.__x**2 + self.__y**2)**0.5
    
    def normalizuj(self):
        if self.dlugosc() == 0:
            return Wektor(0, 0)
        return Wektor(self.__x / self.dlugosc(), self.__y / self.dlugosc())
    
    def wyswietl(self):
        print(f"Wektor [{self.__x}, {self.__y}] o długości {self.dlugosc()}")

    def __add__(self, w):
        return Wektor(self.__x + w.__x, self.__y + w.__y)
    
    def __sub__(self, w):
        return Wektor(self.__x - w.__x, self.__y - w.__y)
    
    def __iadd__(self, w):
        self.__x += w.__x
        self.__y += w.__y
        return self
    
    def __isub__(self, w):
        self.__x -= w.__x
        self.__y -= w.__y
        return self
    
    def __str__(self):
        return f"[{self.__x}, {self.__y}]"
    
    def __mul__(self, a):
        return Wektor(self.__x * a, self.__y * a)
    
    def __rmul__(self, a):
        return Wektor(self.__x * a, self.__y * a)
    
w1 = Wektor(2,4)
w2 = Wektor(1.5)
print("Wektor w1:", w1, "wektor w2:", w2)
print("Dł. w1 =", w1.dlugosc(), "dł. w2 =", w2.dlugosc())
print("w1+w2 =", w1+w2)
print("w1-w2 =", w1-w2)
print("w1*2 =", w1*2)
print("-3*w2 =", -3*w2)
print("w1*2-w2 =", w1*2-w2)
print("w1 po normalizacji =", w1.normalizuj())
print("w2 po normalizacji =", w2.normalizuj())
w1.wyswietl()
w2.wyswietl()
"""

# Zadanie 2

class ElementZamowienia:

    def __init__(self, nazwa, cena, liczbaSztuk):
        self.__nazwa = nazwa
        self.__cena = cena
        self.__liczbaSztuk = liczbaSztuk
    
    def __str__(self):
        return f"{self.__nazwa} {self.__cena} zł, {self.__liczbaSztuk} szt., łącznie {self.obliczKoszt()} zł"
    
    def obliczKoszt(self):
        koszt = self.__cena * self.__liczbaSztuk
        rabat = self.obliczRabat()
        return koszt - rabat
    
    def obliczRabat(self):
        if self.__liczbaSztuk >= 5:
            return self.__cena * self.__liczbaSztuk * 0.1
        return 0

class Zamowienie:

    def __init__(self, maksRozmiar):
        self.__elementy = []
        self.__rozmiar = 0
        self.__maksRozmiar = maksRozmiar

    def dodaj(self, elZam):
        if self.__rozmiar < self.__maksRozmiar:
            self.__elementy.append(elZam)
            self.__rozmiar += 1
            return True
        return False
    
    def obliczKoszt(self):
        koszt = 0
        for element in self.__elementy:
            koszt += element.obliczKoszt()
        return koszt
    
    def pisz(self):
        print("Zamowienie:")
        for indeks, element in enumerate(self.__elementy, start=1):
            print(f"{indeks}. {element}")
        kosztCalkowity = self.obliczKoszt()
        print(f"Koszt całkowity: {kosztCalkowity} zł")
        naliczonyRabat = sum(element.obliczRabat() for element in self.__elementy)
        print(f"Naliczony rabat: {naliczonyRabat} zł")

z = Zamowienie(10)
z.dodaj(ElementZamowienia("Chleb", 4.0, 2))
z.dodaj(ElementZamowienia("Mleko", 2.5, 1))
z.dodaj(ElementZamowienia("Cukier", 4.0, 5))
z.dodaj(ElementZamowienia("Puszka", 9.0, 1))
z.pisz()