from utils.functions import load_data, sort_date, search_top_transactions, show_info


if __name__ == '__main__':
    data = load_data()
    actual_transactions, data_transactions = sort_date(data)
    info = search_top_transactions(actual_transactions, data_transactions)
    print(show_info(info))
    

    
