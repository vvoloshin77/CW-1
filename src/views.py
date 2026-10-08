import os
import requests
from dotenv import load_dotenv
from datetime import datetime
import pandas as pd

load_dotenv()


def get_greeting(date_time: str) -> str:
    dt = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
    hour = dt.hour
    if 6 <= hour <= 11:
        return 'Доброе утро'
    elif 12 <= hour <= 17:
        return 'Добрый день'
    elif 18 <= hour <= 22:
        return 'Добрый вечер'
    else:
        return 'Доброй ночи'


def get_card_data(transactions: pd.DataFrame) -> list[dict]:
    mask = (transactions['Статус'] == 'OK') & (transactions['Сумма операции'] < 0)
    clean = transactions[mask].dropna(subset=['Номер карты'])
    grouped = clean.groupby('Номер карты')['Сумма операции'].sum()
    result = []
    for name, total in grouped.items():
        spent = round(abs(total), 2)
        result.append({
            'last_digits': name.lstrip('*'),
            'total_spent': spent,
            'cashback': round(spent / 100, 2)
        })
    return result


def get_top_transactions(transactions: pd.DataFrame) -> list[dict]:
    mask = (transactions['Статус'] == 'OK')
    s_trans = transactions[mask].sort_values('Сумма платежа', ascending=False).head(5)
    result = []
    for _, row in s_trans.iterrows():
        result.append({
            'date': row['Дата платежа'],
            'amount': row['Сумма платежа'],
            'category': row['Категория'],
            'description': row['Описание'],
        })
    return result


def filter_by_period(transactions: pd.DataFrame, date_time: str) -> pd.DataFrame:
    end = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
    start = end.replace(day=1, hour=0, minute=0, second=0)
    dates = pd.to_datetime(transactions['Дата операции'], dayfirst=True)
    mask = (dates >= start) & (dates <= end)
    return transactions[mask]


def get_currency_rates(currencies: list[str]) -> list[dict]:
    key = os.getenv('API_KEY_CURRENCY')
    result = []
    for cur in currencies:
        try:
            url = f"https://v6.exchangerate-api.com/v6/{key}/latest/{cur}"
            data = requests.get(url, timeout=20).json()
            rate = data['conversion_rates']['RUB']
            result.append({
                'currency': cur,
                'rate': round(rate, 2),
            })
        except (requests.exceptions.RequestException, KeyError, ValueError):
            continue
    return result


def get_stock_prices(stocks: list[str]) -> list[dict]:
    key = os.getenv('API_KEY_STOCK')
    result = []
    for symbol in stocks:
        try:
            data = requests.get(
                "https://www.alphavantage.co/query",
                params={"function": "GLOBAL_QUOTE", "symbol": symbol, "apikey": key},
                timeout=20,
            ).json()
            price = float(data['Global Quote']['05. price'])
            result.append({
                'stock': symbol,
                'price': price,
            })
        except (requests.exceptions.RequestException, KeyError, ValueError):
            continue
    return result
