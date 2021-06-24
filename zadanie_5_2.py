"""### Zadanie 5.2 | Policz wybrane słowo (1 godz.)

Plik z utworem "Pan Tadeusz" do pobrania: https://students.alx.pl/~pgradzinski/kpython/pan-tadeusz.txt
Niech program dla podanej nazwy pliku tekstowego i dla podanego słowa policzy ile razy to słowo występuje w pliku (np. Tadeusz w pliku `pan-tadeusz.txt`)."""

import urllib.request

targetURL = 'https://students.alx.pl/~pgradzinski/kpython/pan-tadeusz.txt'
with urllib.request.urlopen(targetURL) as file:
    text = (file.read().decode("utf-8").strip())
    cleaned_text = []
    cleaned_word = ''
    for char in text:
        if char not in [',', '.', '<', '>', ':', ';', '?', ' ', '—', '\r', '\n', '(', ')', '«', '»', '…', '!', '*', '/']:
            cleaned_word += char
        else:
            if cleaned_word:
                cleaned_text.append(cleaned_word)
                cleaned_word = ''

    searching = input('Searching word: ')
    print(f'{searching} -> {cleaned_text.count(searching)}')