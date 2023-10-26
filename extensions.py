# Классы для обработки исключений и проведения конвертации валют
import json
import requests
from config import currencies

# класс для обработки исключений с пояснением ошибки со стороны пользователя
class APIException(Exception):
    pass

# класс для проведения конвертации
class Converter:
    @staticmethod
    def get_price(base: str, quote: str, amount: float):

        try:
            base_key = currencies[base.lower()]
        except KeyError:
            raise APIException(f"Валюта '{base}' не найдена!")

        try:
            quote_key = currencies[quote.lower()]
        except KeyError:
            raise APIException(f"Валюта '{quote}' не найдена!")

        if base_key == quote_key:
            raise APIException(f"Вы хотите сконвертировать {base} в {base}. Это невозможно! Валюты не должны быть одинаковыми.")

        try:
            amount = float(amount.replace(",", "."))
        except ValueError:
            raise APIException(f"Не удалось обработать количество {amount}!")

        # Получение данных о курсах валют по данным ЦБ РФ
        response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
        data = json.loads(response.content)
        # В файле daily_json.js есть данные только для двух валют - доллара и евро по отношению к 1 рублю,
        # рубль всегда = 1.0
        if base == 'рубль':
             return round(amount / (data['Valute'][quote_key]['Value']), 4)
        if quote == 'рубль':
             return round((data['Valute'][base_key]['Value']) * amount, 4)

        return round((data['Valute'][base_key]['Value']) / (data['Valute'][quote_key]['Value']) * amount, 4)
