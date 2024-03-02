import pytest
from utils.functions import load_data, sort_date


@pytest.fixture
def dataset_fixture():
    return load_data()


@pytest.fixture
def sort_fixture():
    return sort_date(load_data())

