"""### Zadanie 5.1 | Dane skoczków narciarskich (3 godz.)

Plik CSV z danymi: https://students.alx.pl/~pgradzinski/kpython/zawodnicy.csv
Korzystając z pliku CSV z danymi skoczków narciarskich napisz programy, które wczytują ten plik i:
1. wypisuje najwyższego, najniższego, najcięższego i najlżejszego skoczka;
gdyby kilku miało taką samą wagę lub wzrost, to wystarczy wypisać jednego z nich.
2. liczy ile łącznie ważą reprezentanci Polski (np. żeby sprawdzić czy zmieszczą się w windzie na skocznię ;)). Pozwól użytkownikowi podać kraj (niekoniecznie musi być Polska).
3. (trudniejsze) dla wszystkich krajów oblicza ilu jest zawodników z tego kraju; tzn. ma się wypisać, być może w innej kolejności:
```
AUT – 2
FIN – 3
GER – 5
NOR – 3
POL – 3
USA – 1
```
4. jak wyżej, ale liczy jeszcze dla każdego kraju średni wzrost zawodników."""


def height(open_file, operand: str):
    """
    function to get the highest or smaller 'ski-jumper'
    :param open_file: csv format file
    :param operand: if you want to get highest enter: '>', to get the smaller, enter: '<'
    :return: list with: name, surname, nationality, date_of_born, height and weight of highest or smaller ski jumper
    """
    result = []
    for i in open_file.readlines():
        if result:
            if operand == '>':
                if i.strip().split(';')[4] > result[4]:
                    result = i.strip().split(';')
            elif operand == '<':
                if i.strip().split(';')[4] < result[4]:
                    result = i.strip().split(';')
        else:
            result = i.strip().split(';')
    return result


def weight(open_file, operand: str):
    """
    function to get the heaviest or the lightest 'ski-jumper'
    :param open_file: csv format file
    :param operand: if you want to get the heaviest enter: '>', to get the lightest, enter: '<'
    :return: list with: name, surname, nationality, date_of_born, height and weight of the heaviest or the lightest ski
    jumper
    """
    result = []
    for i in open_file.readlines():
        if result:
            if operand == '>':
                if i.strip().split(';')[5] > result[5]:
                    result = i.strip().split(';')
            elif operand == '<':
                if i.strip().split(';')[5] < result[5]:
                    result = i.strip().split(';')
        else:
            result = i.strip().split(';')
    return result


with open('baza_danych/zawodnicy.csv', 'r', encoding='UTF-8') as file:
    most_h = height(file, '>')
    print(f'Highest ski jumper on the list is {most_h[0]} {most_h[1]}, his height = {most_h[4]}')
    file.seek(0)
    smallest_ski_j = height(file, '<')
    print(
        f'Smallest ski jumper on the list is {smallest_ski_j[0]} {smallest_ski_j[1]}, his height = {smallest_ski_j[4]}')
    file.seek(0)
    the_heaviest = weight(file, '>')
    print(f'The heaviest ski jumper on the list is {the_heaviest[0]} {the_heaviest[1]}, his weight = {the_heaviest[5]}')
    file.seek(0)
    the_lightest = weight(file, '<')
    print(f'The lightest ski jumper on the list is {the_lightest[0]} {the_lightest[1]}, his weight = {the_lightest[5]}')
