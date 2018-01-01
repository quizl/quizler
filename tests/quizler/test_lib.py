# pylint: disable=no-self-use,missing-docstring,invalid-name

import json
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

    def test_no_client_id_or_access_token(self):
        with self.assertRaises(ValueError):
            api_call('get', 'end_point')

    def test_client_id_and_access_token(self):
        with self.assertRaises(ValueError):
            api_call('get', 'end_point', client_id='client_id', access_token='token')

    @mock.patch('requests.request')
    def test_unknown_endpoint(self, mock_request):
        mock_request.return_value.status_code = 404
        with self.assertRaises(ValueError):
            api_call('get', 'unknown_end_point', client_id='client_id')

    @mock.patch('requests.request')
    def test_correct_url_was_called_with_client_id(self, mock_request):
        mock_request.return_value.status_code = 200
        api_call('get', 'end_point', client_id='client_id')
        mock_request.assert_called_once_with(
            'get',
            'https://api.quizlet.com/2.0/end_point',
            params={'client_id': 'client_id'},
            headers=None
        )

    @mock.patch('requests.request')
    def test_correct_url_was_called_with_access_token(self, mock_request):
        mock_request.return_value.status_code = 200
        api_call('get', 'end_point', access_token='token')
        mock_request.assert_called_once_with(
            'get',
            'https://api.quizlet.com/2.0/end_point',
            params={},
            headers={'Authorization': 'Bearer token'}
        )

    @mock.patch('requests.request')
    def test_json_output_was_returned(self, mock_request):
        response = mock.Mock()
        response.status_code = 200
        mock_request.return_value = response
        data = api_call('get', 'end_point', client_id='client_id')
        self.assertEqual(data, response.json())

    @mock.patch('requests.request')
    def test_non_json_output(self, mock_request):
        response = mock.Mock()
        response.status_code = 200
        response.json = mock.Mock(side_effect=json.decoder.JSONDecodeError('', '', 1))
        mock_request.return_value = response
        data = api_call('get', 'end_point', client_id='client_id')
        self.assertEqual(data, None)
