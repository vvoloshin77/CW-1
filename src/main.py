from src.views import main_page
import logging

logging.basicConfig(
    filename='logs/log_report.log',
    filemode='w',
    format='%(asctime)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO,
    encoding='utf-8',
)


if __name__ == "__main__":
    # df = read_transactions('data/operations.xlsx')
    # result = spending_by_category(df, 'Супермаркеты', '2021-12-31')
    # # print(df.shape)
    # # print(df.head())
    # print(result.shape)
    print(main_page("2021-12-31 16:44:00"))
