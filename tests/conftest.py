import pytest


@pytest.fixture
def operation():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
@pytest.fixture
def card():
    return "Maestro 1596837868705199", "Maestro **5199"


@pytest.fixture
def account():
    return "Счет 70007922896063612056", "Счет 7000 79** **** 2056"


@pytest.fixture
def date():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.fixture
def dates():
    return "11.03.2024"


@pytest.fixture
def mask_card():
    return "7000792289606361", "7000 79** **** 6361"


@pytest.fixture
def mask_account():
    return "73654108430135874305", "**4305"