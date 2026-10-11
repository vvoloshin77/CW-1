from src.utils import read_transactions


def test_read_transactions():
    assert read_transactions("data/operations.xlsx").shape == (6705, 15)


def test_read_transactions_not_excel():
    rd = read_transactions("README.md")
    assert rd.empty


def test_read_transactions_not_path():
    rd = read_transactions("hello world")
    assert rd.empty
