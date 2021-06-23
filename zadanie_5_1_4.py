with open('baza_danych/zawodnicy.csv', 'r', encoding='UTF-8') as file:
    from collections import defaultdict

    file.seek(0)
    nationality = [x.split(';')[2] for x in file.readlines()]

    file.seek(0)
    weight = defaultdict(int)
    for i in file.readlines():
        weight[i.split(';')[2]] += int(i.split(';')[4])

    file.seek(0)
    for i in set(nationality):
        print(f'{i}: {weight[i] / nationality.count(i):.2f}')