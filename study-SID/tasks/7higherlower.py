# Gra w ”Za dużo, za mało”. Komputer losuje liczbę z zakresu 1 . . . 100, a gracz (użytkownik)
# ma za zadanie odgadnąć, co to za liczba poprzez podawanie kolejnych wartości. Jeżeli podana
#  wartość jest: większa – wyświetlany jest komunikat „Podałeś za dużą wartość”, 
# mniejsza – wyświetlany jest komunikat „Podałeś za małą wartość”, 
# identyczna z wylosowaną – wyświetlany jest komunikat „Gratulacje” i gra się kończy.

import random
wylosowanaLiczba = random.randint(1, 100)
czyOdgadnieta = False
while not czyOdgadnieta:
    zgadnietaWartosc = int(input("Podaj liczbę od 1 do 100: "))
    if zgadnietaWartosc < wylosowanaLiczba:
        print("Podałeś za małą wartość")
    elif zgadnietaWartosc > wylosowanaLiczba:
        print("Podałeś za dużą wartość")
    else:
        print("Gratulacje! Odgadłeś liczbę:", wylosowanaLiczba)
        czyOdgadnieta = True
