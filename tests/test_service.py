import pytest
import source.service as service
import unittest.mock as mock

@mock.patch("source.service.get_data_from_db")
def test_get_data_from_db(mock_get_db_data):
    mock_get_db_data.return_value = "tanvin"
    user_name = service.get_data_from_db(1)
    assert user_name == "tanvin"


