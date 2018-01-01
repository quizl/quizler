# pylint: disable=no-self-use,missing-docstring,invalid-name

import unittest
from unittest import mock

from quizler.lib import api_call, get_api_envs
from tests.utils import mock_envs


class TestGetApiEnvs(unittest.TestCase):

    @mock_envs()
    def test_no_envs(self):
        with self.assertRaises(ValueError):
            get_api_envs()

    @mock_envs(USER_ID='user_id')
    def test_no_client_id(self):
        with self.assertRaises(ValueError):
            get_api_envs()

    @mock_envs(CLIENT_ID='client_id')
    def test_no_user_id(self):
        with self.assertRaises(ValueError):
            get_api_envs()

    @mock_envs(CLIENT_ID='client_id', USER_ID='user_id')
    def test_all_envs_are_set(self):
        client_id, user_id = get_api_envs()
        self.assertEqual(client_id, 'client_id')
        self.assertEqual(user_id, 'user_id')


class TestApiCall(unittest.TestCase):

    @mock.patch('requests.request')
    def test_unknown_endpoint(self, mock_request):
        mock_request.return_value.status_code = 404
        with self.assertRaises(ValueError):
            api_call('get', 'unknown_end_point', {}, 'client_id')

    @mock.patch('requests.request')
    def test_correct_url_was_called(self, mock_request):
        mock_request.return_value.status_code = 200
        api_call('get', 'end_point', {}, 'client_id')
        mock_request.assert_called_once_with(
            'get',
            'https://api.quizlet.com/2.0/end_point',
            params={'client_id': 'client_id'}
        )

    @mock.patch('requests.request')
    def test_correct_output_was_returned(self, mock_request):
        response = mock.Mock()
        response.status_code = 200
        mock_request.return_value = response
        data = api_call('get', 'end_point', {}, 'client_id')
        self.assertEqual(data, response.json())
