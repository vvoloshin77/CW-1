import pandas as pd
import logging

logger = logging.getLogger(__name__)


def simple_search(transactions: pd.DataFrame, query: str) -> str:
    logger.info('Поиск по запросу: %s', query)
    q = query.lower()
    mask = transactions.apply(
        lambda t: q in str(t["Описание"]).lower() or q in str(t["Категория"]).lower(),
        axis=1,
    )
    found = transactions[mask]
    logger.info('Найдено операций', len(found))
    return transactions[mask].to_json(orient="records", force_ascii=False)
