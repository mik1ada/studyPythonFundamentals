# Zadanie 1

liczby = [12, 7, 5, 18, 9]

conditions = [
    any(number > 15 for number in liczby),
    any(number < 0 for number in liczby)
]

if any(conditions):
    print("Lista zawiera liczbe spelniajaca jeden z warunkow")
else:
    print("Brak liczb spelniajacych warunek")