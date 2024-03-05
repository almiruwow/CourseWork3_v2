import json
from datetime import datetime
import copy


def load_data():
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data


def sort_date(dataset):
    new_dateset = []
    transactions = []
    new_data = copy.deepcopy(dataset)

    for data in new_data:
        if data.get('date') is None or data.get('state') == "CANCELED":
            continue

        date_str = data.get('date')
        date = datetime.fromisoformat(date_str)

        data['date'] = date

        transactions.append(date)
        new_dateset.append(data)

    transactions.sort(reverse=True)

    return transactions[:5], new_dateset


def search_top_transactions(top_5, dataset):
    result = []
    for date in top_5:
        for data in dataset:
            if date == data.get('date'):
                result.append(data)
                break

    return result


def show_info(information):
    text = ''
    for info in information:

        if info.get('from') is None:
            info['from'] = 'Реквизиты'
        elif info.get('from')[:4] == 'Счет':
            info['from'] = 'Счет **' + info.get('from')[-4:]
        else:
            info['from'] = info.get('from')[:-10] + '******' + info.get('from')[-4:]
            info['from'] = info['from'][:-12] + ' ' + info['from'][-12:-8] + ' ' \
                           + info['from'][-8:-4] + ' ' + info['from'][-4:]

        if info.get('to')[:4] == 'Счет':
            info['to'] = 'Счет **' + info.get('to')[-4:]
        else:
            info['to'] = info.get('to')[:-10] + '******' + info.get('to')[-4:]
            info['to'] = info['to'][:-12] + ' ' + info['to'][-12:-8] + ' ' \
                           + info['to'][-8:-4] + ' ' + info['to'][-4:]

        date = info['date']

        text += f'{date.day}.{date.month}.{date.year} {info["description"]}\n' \
                f'{info["from"]} -> {info["to"]}\n' \
                f'{info["operationAmount"]["amount"]} {info["operationAmount"]["currency"]["name"]}\n\n'

    return text





