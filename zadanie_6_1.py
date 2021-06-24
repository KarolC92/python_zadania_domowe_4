"""### Zadanie 6.1 | Pobieranie informacji z API metaweather

Napisz program wyświetlający pogodę dla wskazanej przez użytkownika lokalizacji.
Skorzystaj z modułu urllib.request, json oraz API MetaWeather."""

from json.decoder import JSONDecodeError

import requests

try:
    location = input('Location WOEID: ')
    response = requests.get('https://www.metaweather.com/api/location/' + location + '/')
    result = response.json()
    file = result['consolidated_weather'][len(result['consolidated_weather'])-1]
    for i in file:
        print(f'{i} - {file[i]}')
except JSONDecodeError:
    print('Value Error')
except KeyError:
    print('Incorrect Value')