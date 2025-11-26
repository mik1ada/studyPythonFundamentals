def obliczaniePowierzchni(promien):
    pi = 3.14
    pole = pi * promien ** 2
    return pole

listaPol = []
print('Podaj dla ilu promieni chcesz policzyc pole powierzchni kola: ')
iloscPromieni = range(int(input()))

for i in iloscPromieni:
    print('Podaj dlugosc promienia: ')
    promien = float(input())
    if promien <= 0:
        print('Promien powinien byc wartoscia dodatnia')
    else:
        pole = obliczaniePowierzchni(promien)
        print('Pole dla podanego promienia wynosi: ')
        print(pole)
        if pole > 10:
            listaPol.append(pole)
print(listaPol)