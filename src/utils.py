import pandas as pd


def read_transactions(file_path: str) -> pd.DataFrame:
    try:
        return pd.read_excel(file_path)
    except FileNotFoundError:
        return pd.DataFrame()
    except Exception:
        return pd.DataFrame()