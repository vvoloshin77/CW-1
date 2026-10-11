from typing import Optional

import pandas as pd


def report_to_file(arg=None):
    filename = arg if isinstance(arg, str) else "data/report.json"

    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"вызываю {func.__name__}")
            result = func(*args, **kwargs)
            print("отчёт готов, строк:", len(result))
            result.to_json(filename, orient="records", indent=2, force_ascii=False)
            return result

        return wrapper

    if callable(arg):
        return decorator(arg)
    return decorator


@report_to_file("data/test.json")
def spending_by_category(
    transactions: pd.DataFrame, category: str, date: Optional[str] = None
) -> pd.DataFrame:
    dates = pd.to_datetime(transactions["Дата операции"], dayfirst=True)
    if date is None:
        end = pd.Timestamp.now()
    else:
        end = pd.to_datetime(date)
    start = end - pd.DateOffset(months=3)
    mask = (
        (transactions["Категория"] == category)
        & (dates >= start)
        & (dates <= end)
        & (transactions["Статус"] == "OK")
        & (transactions["Сумма операции"] < 0)
    )
    return transactions[mask]
