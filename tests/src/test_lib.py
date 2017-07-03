import unittest
from unittest import mock

from src.lib import api_call


class TestApiCall(unittest.TestCase):
    @mock.patch('requests.get')
    def test_unknown_endpoint(self, mock_get):
        mock_get.return_value.status_code = 404
        with self.assertRaises(ValueError):
            api_call('unknown_end_point')

    @mock.patch('requests.get')
    @mock.patch('src.lib.CLIENT_ID', 'user_id_123')
    def test_correct_url_was_called(self, mock_get):
        mock_get.return_value.status_code = 200
        api_call('end_point')
        mock_get.assert_called_once_with(
            'https://api.quizlet.com/2.0/users/pavel_karateev/end_point',
            {'client_id': 'user_id_123'}
        )
