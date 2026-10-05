from datetime import datetime
import pandas as pd


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
