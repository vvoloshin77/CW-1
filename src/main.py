from src.reports import spending_by_category
from src.utils import read_transactions


if __name__ == '__main__':
    df = read_transactions('data/operations.xlsx')
    result = spending_by_category(df, 'Супермаркеты', '2021-12-31')
    # print(df.shape)
    # print(df.head())
    print(result.shape)

