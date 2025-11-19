# Napisać program, który pobiera od użytkownika ciąg liczb całkowitych. Pobieranie danych
#  kończone jest podaniem wartości 0 (nie wliczana do danych). W następnej kolejności 
# program powinien wyświetlić sumę największej oraz najmniejszej z podanych liczb oraz ich
#  średnią arytmetyczną. Przykład: Użytkownik podał ciąg: 1, -4, 2, 17, 0. 
# Wynik programu: 13 // suma min. i maks. 6.5 // średnia

suma = 0
liczba = -1
maks = None
minim = None
ilosc = 0

while liczba != 0:
    liczba = int(input("Podaj liczbę całkowitą (0 kończy wprowadzanie): "))
    if liczba != 0:
        suma += liczba
        ilosc += 1
        if maks is None or maks < liczba:
            maks = liczba
        if minim is None or minim > liczba:
            minim = liczba
if ilosc > 0:
    srednia = suma / ilosc
    print("Suma największej i najmniejszej liczby wynosi:", maks + minim)
    print("Średnia arytmetyczna podanych liczb wynosi:", srednia)
else:
    print("Nie podano żadnych liczb oprócz 0.")