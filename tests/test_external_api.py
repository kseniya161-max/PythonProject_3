import pytest
import unittest.mock
from unittest.mock import patch
from src.external_api import convert_currency


def test_convert_currency():
    """ Конвертирует ли USD  в рубли"""
    with patch('src.external_api.get_currency') as mock_get_currency:
        mock_get_currency.return_value = 75.0
        result = convert_currency(100, 'USD')
        assert result == 7500.0
