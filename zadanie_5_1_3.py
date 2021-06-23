with open('baza_danych/zawodnicy.csv', 'r', encoding='UTF-8') as file:
    file.seek(0)
    from collections import Counter

    raport = [i.split(';')[2] for i in file.readlines()]
    for i, j in Counter(raport).items():
        print(f'{i} - {j}')
