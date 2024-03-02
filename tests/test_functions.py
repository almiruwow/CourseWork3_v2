from utils.functions import *
import datetime


def test_json_load():
    assert type(load_data()) is list
    assert len(load_data()) > 100
    assert type(load_data()[0]) is dict


def test_sort_date(dataset_fixture):
    assert type(sort_date(dataset_fixture)[1]) is list
    assert len(sort_date(dataset_fixture)) == 2
    assert type(sort_date(dataset_fixture)[1][-1]) is dict
    assert len(sort_date(dataset_fixture)[0]) == 5


def test_search(sort_fixture):
    assert search_top_transactions(sort_fixture[0], sort_fixture[1])[-1] == \
           {'id': 801684332,
            'state': 'EXECUTED',
            'date': datetime.datetime(2019, 11, 5, 12, 4, 13, 781725),
            'operationAmount': {'amount': '21344.35', 'currency': {'name': 'руб.', 'code': 'RUB'}},
            'description': 'Открытие вклада', 'to': 'Счет 77613226829885488381'}

    assert len(search_top_transactions(sort_fixture[0], sort_fixture[1])) == 5
    assert type(search_top_transactions(sort_fixture[0], sort_fixture[1])) is list


def test_show_info(sort_fixture):
    assert type(show_info(search_top_transactions(sort_fixture[0], sort_fixture[1]))) == str