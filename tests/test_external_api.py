import pytest
import unittest.mock
import requests
from unittest.mock import patch
from src.external_api import convert_currency

def test_convert_currency():
    """ Конвертирует ли USD  в рубли"""
    with patch('src.external_api.get_currency') as mock_get_currency:
        mock_get_currency.return_value = 75.0
        print("Before conversion")
        result = convert_currency(50, 'USD')
        print("After conversion")
        assert result == 3750.0


def test_convert_currency_rub():
    """Тестирует, что RUB не конвертируется"""
    result = convert_currency(100, 'RUB')
    assert result == 100.0