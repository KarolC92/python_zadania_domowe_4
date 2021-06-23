with open('baza_danych/zawodnicy.csv', 'r', encoding='UTF-8') as file:
    country = input('Country: ')
    sum_of_weight = sum([int(x[5]) for x in list(filter(lambda x: x[2] == country, [x.split(';') for x in file.readlines()]))])
    print(f'Sum weights of {country} representatives = {sum_of_weight}')
