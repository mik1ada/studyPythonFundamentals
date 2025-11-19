#Napisać program, który wczytuje liczby podawane przez użytkownika dotąd, dopóki nie podana 
# zostanie liczba 0. Następnie wyświetlić sumę wszystkich podanych liczb.

suma = 0
liczba = -1
while liczba != 0:
    liczba = float(input("Podaj liczbę (0 kończy wprowadzanie): "))
    suma += liczba
print("Suma podanych liczb wynosi:", suma)