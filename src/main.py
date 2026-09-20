from src.utils import read_transactions


if __name__ == '__main__':
    df = read_transactions('data/enaup.xlsx')
    print(df.shape)
    print(df.head())

