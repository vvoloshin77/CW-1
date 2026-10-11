from src.utils import read_transactions
from src.views import (filter_by_period, get_card_data, get_greeting,
                       get_top_transactions)


def test_get_greeting():
    assert get_greeting("2021-12-31 09:00:00") == "Доброе утро"
    assert get_greeting("2021-12-31 14:00:00") == "Добрый день"
    assert get_greeting("2021-12-31 20:00:00") == "Добрый вечер"
    assert get_greeting("2021-12-31 02:00:00") == "Доброй ночи"


def test_filter_by_period():
    rd = read_transactions("data/operations.xlsx")
    period = filter_by_period(rd, "2021-12-31 16:44:00")
    assert len(period) == 182


def test_get_card_data():
    rd = read_transactions("data/operations.xlsx")
    period = filter_by_period(rd, "2021-12-31 16:44:00")
    assert len(get_card_data(period)) == 3


def test_get_top_transactions():
    rd = read_transactions("data/operations.xlsx")
    period = filter_by_period(rd, "2021-12-31 16:44:00")
    assert len(get_top_transactions(period)) == 5
