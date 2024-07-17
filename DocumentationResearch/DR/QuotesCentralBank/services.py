import requests
import xml.etree.ElementTree as Etree
from datetime import datetime
from DR.settings import EXTERNAL_URLS


# Получаем котировки ЦБ для заполнения БД
def get_quotes() -> list[dict[str, str | int | float]] | None:
    # Ассоциативный словарь для столбцов БД
    keys: dict[str, str | int | float] = {"Name": 'name',
                                          'Nominal': 'nominal',
                                          'NumCode': 'num_code',
                                          'CharCode': 'char_code',
                                          'VunitRate': 'vunit_rate'
                                          }
    # Получаем актуальные данные
    today = datetime.now().strftime('%d/%m/%Y')
    response = requests.get(f'{EXTERNAL_URLS["quotes_cbfr"]}{today}')

    try:
        if response.status_code != 200:
            raise requests.RequestException()
    except requests.RequestException:
        print(f'Ошибка инициализации котировок. Сайт Центробанка недоступен. Статус код: {response.status_code}')
        return None

    root = Etree.fromstring(response.text)

    quotes: list[dict[str, str | int | float]] = []

    # Заполняем quotes информацией о котировках
    for item in root.findall('Valute'):
        quote: dict[str, str | int | float] = {}
        for element in item:
            if element.tag in keys:
                if element.tag == 'VunitRate':
                    quote[keys[element.tag]] = float(element.text.replace(",", "."))
                elif element.tag == 'Nominal':
                    quote[keys[element.tag]] = int(element.text)
                else:
                    quote[keys[element.tag]] = element.text

        quotes.append(quote)

    return quotes
