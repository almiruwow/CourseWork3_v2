from utils.functions import load_data, sort_date, search_top_transactions


if __name__ == '__main__':
    data = load_data()

    actual_transactions, data_transactions = sort_date(data)
    print(len(search_top_transactions(actual_transactions, data_transactions)))

    for d in search_top_transactions(actual_transactions, data_transactions):
        print(d)
