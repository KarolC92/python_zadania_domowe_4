"""### Zadanie 6.2 | Pobieranie informacji z API wykazu podatników VAT.

Napisz program, który sprawdzi w wykazie podatników VAT informacje o firmie
na podstawie jej numeru NIP.

https://www.gov.pl/web/kas/api-wykazu-podatnikow-vat"""

import requests
import datetime

nip = input("NIP: ")
try:
    response = requests.get('https://wl-api.mf.gov.pl/api/search/nip/' + nip + '?' + 'date=' + str(datetime.date.today()))
    data = response.json()

    for i in data['result']['subject']:
        print(f'{i} - {data["result"]["subject"][i]}')
except KeyError:
    print('Incorrect NIP number')
