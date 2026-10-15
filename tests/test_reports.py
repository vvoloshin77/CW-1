import pandas as pd

from src.reports import report_to_file, spending_by_category
from src.utils import read_transactions


def test_spending_by_supermarket():
    rd = read_transactions("data/operations.xlsx")
    assert len(spending_by_category(rd, "Супермаркеты", "2021-12-31")) == 131


def test_spending_by_trans():
    rd = read_transactions("data/operations.xlsx")
    assert len(spending_by_category(rd, "Переводы", "2021-12-31")) == 20


def test_spending_by_popol():
    rd = read_transactions("data/operations.xlsx")
    assert len(spending_by_category(rd, "Пополнения", "2021-12-31")) == 0


def test_report_to_file(tmp_path):
    out = tmp_path / "report.json"

    @report_to_file(str(out))
    def fake_report():
        return pd.DataFrame({"a": [1, 2]})

    fake_report()
    assert out.exists()
