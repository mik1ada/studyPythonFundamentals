# Napisać program, który oblicza wartość współczynnika BMI (ang. body mass
#index) wg. wzoru: waga / wzrost^2 . Jeżeli wynik jest w przedziale (18,5 - 24,9) to wypisuje
#”waga prawidłowa”, jeżeli poniżej to ”niedowaga”, jeżeli powyżej ”nadwaga”.

waga = float(input("Podaj swoją wagę w kilogramach: "))
wzrost = float(input("Podaj swój wzrost w metrach: "))
bmi = waga / (wzrost ** 2)
if 18.5 <= bmi <= 24.9:
    print("Waga prawidłowa")
elif bmi < 18.5:
    print("Niedowaga")
else:
    print("Nadwaga")