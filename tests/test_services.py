import json

from src.services import simple_search
from src.utils import read_transactions


def test_simple_search():
    rd = read_transactions("data/operations.xlsx")
    result = json.loads(simple_search(rd, "колхоз"))
    assert len(result) == 677


def test_simple_search_h():
    rd = read_transactions("data/operations.xlsx")
    result = json.loads(simple_search(rd, "КОЛХОЗ"))
    assert len(result) == 677


def test_simple_search_l():
    rd = read_transactions("data/operations.xlsx")
    result = json.loads(simple_search(rd, "атом"))
    assert len(result) == 0
