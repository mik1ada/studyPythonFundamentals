# Napisać program, który pobiera od użytkownika liczbę całkowitą dodatnią, a następnie 
# wyświetla na ekranie kolejno wszystkie liczby nieparzyste nie większe od podanej liczby. 
# Przykład, dla 15 program powinien wyświetlić 1, 3, 5, 7, 9, 11, 13, 15.

liczba = int(input("Podaj liczbe calkowita dodatnia:"))

for i in range(1, liczba + 1, 2):
    print(i)