"""### Zadanie 5.3 | Policz wszystkie słowa (trudne) (2 godz.)

Podstawowa funkcjonalność:
Napisz program, który czyta plik tekstowy i wylicza oraz wypisuje bez powtórzeń wszystkie słowa występujące w pliku
wraz z informacją ile razy dane słowo występuje. Na przykład w ten sposób:
```
Zosia -> 34
Asesor -> 35
dwóch -> 35
Tadeusz -> 107
```
Ewentualne uproszczenie (w razie problemów z wypisywaniem): wypisz tylko jedno najczęściej występujące słowo.
Dalsze rozszerzenia (opcjonalnie):
- posortuj wypisywane słowa
- oprócz liczby poszczególnych słów policz i wypisz także liczbę wszystkich słów, łączną liczbę wszystkich znaków."""

import urllib.request

targetURL = 'https://students.alx.pl/~pgradzinski/kpython/pan-tadeusz.txt'
with urllib.request.urlopen(targetURL) as file:
    text = (file.read().decode("utf-8").strip())
    cleaned_text = {}
    cleaned_word = ''
    for char in text:
        if char not in [',', '.', '<', '>', ':', ';', '?', ' ', '—', '\r', '\n', '(', ')', '«', '»', '…', '!', '*', '/']:
            cleaned_word += char
        else:
            if cleaned_word:
                if cleaned_word in cleaned_text:
                    cleaned_text[cleaned_word] += 1
                else:
                    cleaned_text[cleaned_word] = 1
                cleaned_word = ''

    for word, number in sorted(cleaned_text.items()):
        print(f'{word} -> {number}')
    print(f'Wszystkie słowa: {sum(cleaned_text.values())}')

    counter = 0
    for char in text:
        if char != ' ':
            counter += 1
    print(f'Wszystkich znaków: {counter}')
