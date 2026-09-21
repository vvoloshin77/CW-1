from typing import Optional
import pandas as pd


def spending_by_category(transactions: pd.DataFrame,
                         category: str,
                         date: Optional[str] = None) -> pd.DataFrame:
    dates = pd.to_datetime(transactions['Дата операции'], dayfirst=True)
    if date is None:
        end = pd.Timestamp.now()
    else:
        end = pd.to_datetime(date)
    start = end - pd.DateOffset(months=3)
    # return transactions[transactions['Категория'] == category]
    mask = (
            (transactions['Категория'] == category)
            & (dates >= start)
            & (dates <= end)
            & (transactions['Статус'] == 'OK')
            & (transactions['Сумма операции'] < 0)
    )
    return transactions[mask]