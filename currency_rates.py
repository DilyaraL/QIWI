import argparse
import requests
from bs4 import BeautifulSoup
from datetime import datetime


def parse_date(date_str):
    """
       Проверяет валидность строки-даты. В случае ошибки выбрасывает исключение.
    """
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        return date.strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Некорректный формат даты, должно быть YYYY-MM-DD")


def currency_rates(code, date):
    """
        Пытается получить курсы валюты по указанному коду и дате.
        Возвращает словарь с информацией о валюте или None, если валюта не найдена.
    """
    formatted_date = parse_date(date)

    try:
        response = requests.get(f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={formatted_date}')
        response.raise_for_status()  # Проверяем, что ресурс найден
    except requests.HTTPError as http_err:
        print(f"Ошибка HTTP: {http_err}")
    except Exception as err:
        print(f"Произошла ошибка: {err}")
    else:
        soup = BeautifulSoup(response.content, 'xml')
        for currency in soup.find_all('Valute'):
            if currency.CharCode.string == code:
                return {"code": code, "name": currency.Name.string, "value": currency.Value.string}

    print("Валюта не найдена")
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--code", type=str, required=True, help="Код валюты в формате ISO 4217")
    parser.add_argument("--date", type=str, required=True, help="Дата в формате YYYY-MM-DD")
    args = parser.parse_args()

    result = currency_rates(args.code, args.date)
    if result:
        print(result['code'] + ' (' + result['name'] + '): ' + result['value'])
