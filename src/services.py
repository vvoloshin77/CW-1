import pandas as pd


def simple_search(transactions: pd.DataFrame, query: str) -> str:
    q = query.lower()
    mask = transactions.apply(
        lambda t: q in str(t["Описание"]).lower() or q in str(t["Категория"]).lower(),
        axis=1,
    )
    return transactions[mask].to_json(orient="records", force_ascii=False)
