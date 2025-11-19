# Napisać program, który wczytuje od użytkownika liczbę całkowitą dodatnią n, a następnie 
# wyświetla na ekranie wszystkie potęgi liczby 2 nie większe, niż podana liczba. Przykładowo,
#  dla liczby 71 program powinien wyświetlić: 1 2 4 8 16 32 64

n = int(input("Podaj liczbę całkowitą dodatnią: "))
potega = 1
while(potega <= n):
    print(potega)
    potega *= 2