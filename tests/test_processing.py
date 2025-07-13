from src.processing import filter_by_state

def test_filter_by_state(operation, state):
    assert filter_by_state('operation', 'state'== "EXECUTED") == "EXECUTED"

    assert filter_by_state('operation', "state"== "CANCELED") == "CANCELED"







