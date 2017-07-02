import unittest
from unittest import mock

from src.lib import api_call


class TestApiCall(unittest.TestCase):
    def test_unknown_endpoint(self):
        with mock.patch('requests.get') as mock_get:
            response = mock_get.return_value
            response.status_code = 404
            with self.assertRaises(ValueError):
                api_call('unknown_end_point')

    def test_correct_url_was_called(self):
        with mock.patch('requests.get') as mock_get:
            api_call('end_point')
            mock_get.assert_called_once_with()
