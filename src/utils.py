import pandas as pd
import logging

logger = logging.getLogger(__name__)


def read_transactions(file_path: str) -> pd.DataFrame:
    try:
        rd = pd.read_excel(file_path)
        logger.info('Прочитано строк: %s', len(rd))
        return rd
    except FileNotFoundError:
        logger.error('Файл не найден: %s', file_path)
        return pd.DataFrame()
    except Exception as e:
        logger.error('Не удалось прочитать %s: %s', file_path, e)
        return pd.DataFrame()
