# Currency Rates

Проект "Currency Rates" предназначен для получения курса валют по указанному коду валюты и дате из Центробанка России.


## Установка

Для использования проекта вам понадобятся Python и pip. Если они уже установлены, вы можете установить зависимости проекта с помощью следующей команды:

pip install -r requirements.txt


## Использование

Программу можно использовать с командной строки следующим образом:

python currency_rates.py --code=USD --date=2022-10-08


## Тестирование

Проект содержит базовые тесты, которые можно запустить с помощью команды:

python -m unittest


## Структура проекта

- `currency_rates.py` - основной файл программы, содержащий логику получения курсов валют.
- `test_currency_rates.py` - файл с тестами для `currency_rates.py`.
