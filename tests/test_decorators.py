import pytest
import logging
from src. decorators import  get_mask_card_number, get_mask_account, faulty_function


def test_decorators_get_mask_card_number(caplog):
    with caplog.at_level(logging.INFO):
        result = get_mask_card_number("7000792289606361")
        if result:
            assert result == "7000 79** **** 6361"
            assert "Function: get_mask_card_number completed successfully with result: 7000 79** **** 6361" in caplog.text
            assert "Starting function: get_mask_card_number, args: ('7000792289606361',), kwargs: {}" in caplog.text
            assert "INFO     get_mask_card_number:decorators.py:50 Ending function: get_mask_card_number" in caplog.text
        result_none = get_mask_card_number(None)
        assert result_none == ""
        assert "Starting function: get_mask_card_number, args: (None,), kwargs: {}" in caplog.text
        assert "Function: get_mask_card_number completed successfully with result: 7000 79** **** 6361" in caplog.text



def test_decorators_get_mask_card_account(caplog):
    with caplog.at_level(logging.INFO):
        result = get_mask_account("73654108430135874305")
        if result:
            assert result == "**4305"
            assert "Starting function: get_mask_account, args: ('73654108430135874305',), kwargs: {}" in caplog.text
            assert "Function: get_mask_account completed successfully with result: **4305" in caplog.text
            assert "Ending function: get_mask_account" in caplog.text


def test_decorator_time_account(caplog):
    with caplog.at_level(logging.INFO):
        result = get_mask_account("73654108430135874305")
        if result:
           assert "2025-07-27 19:22:43"


def test_decorator_logs_exceptions(caplog):
    with caplog.at_level(logging.ERROR):
        with pytest.raises(ValueError):
            faulty_function()

        assert "Error in function: faulty_function" in caplog.text
        assert "error type: ValueError" in caplog.text
        assert "args: ()" in caplog.text
        assert "kwargs: {}" in caplog.text
















