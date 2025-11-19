#W sklepie ze sprzętem AGD oferowana jest sprzedaż ratalna. Napisz program
#umożliwiający wyliczenie wysokości miesięcznej raty za zakupiony sprzęt. Danymi
#wejściowymi dla programu są: cena towaru (od 100 zł do 10 tyś. zł), liczba rat (od 6 do 48).
#Kredyt jest oprocentowany w zależności od liczby rat: od 6–12 wynosi 2.5% ,od 13–24 wynosi 5%,
# od 25–48 wynosi 10%. Obliczona miesięczna rata powinna zawierać również odsetki. 
# Program powinien sprawdzać, czy podane dane mieszczą się w określonych powyżej zakresach, a
#  w przypadku błędu pytać prosić użytkownika ponownie o podanie danych.

cenaTowaru = float(input("Podaj cenę towaru (100 - 10000 zł): "))
while cenaTowaru < 100 or cenaTowaru > 10000:
    cenaTowaru = float(input("Błędna wartość. Podaj cenę towaru (100 - 10000 zł): "))

liczbaRat = int(input("Podaj liczbę rat (6 - 48): "))
while liczbaRat < 6 or liczbaRat > 48:
    liczbaRat = int(input("Błędna wartość. Podaj liczbę rat (6 - 48): "))

if 6 <= liczbaRat <= 12:
    oprocentowanie = 0.025
elif 13 <= liczbaRat <= 24:
    oprocentowanie = 0.05
else:
    oprocentowanie = 0.1

miesiecznaRata = (cenaTowaru * (1 + oprocentowanie)) / liczbaRat
print("Miesięczna rata wynosi:", miesiecznaRata, "zł")