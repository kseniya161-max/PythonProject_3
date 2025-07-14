import pytest

from src.processing import filter_by_state


@pytest.fixture
def operation():
    return [{'id': 41428829, 'state': 'EXECUTED',
              'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED',
              'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED',
              'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED',
              'date': '2018-10-14T08:21:33.419441'}]

# @pytest.mark.parametrize("state, expected", [{"EXECUTED"},{"CANCELED"},])
# def test_filter_by_state(state, expected):
#     assert filter_by_state(state) == expected




@pytest.fixture
def fixture_get_by_date():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
           {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
           {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


