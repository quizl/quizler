"""Additional none-user-visible utilities."""

import json
import os
import requests


def get_api_envs():
    """Get required API keys from environment variables."""
    client_id = os.environ.get('CLIENT_ID')
    user_id = os.environ.get('USER_ID')
    if not client_id or not user_id:
        raise ValueError('API keys are not found in the environment')
    return client_id, user_id


def api_call(method, end_point, params=None, client_id=None, access_token=None):
    """Call given API end_point with API keys.
    :param method: HTTP method (e.g. 'get', 'delete').
    :param end_point: API endpoint (e.g. 'users/john/sets').
    :param params: Dictionary to be sent in the query string (e.g. {'myparam': 'myval'})
    :param client_id: Quizlet client ID as string.
    :param access_token: Quizlet access token as string.
    client_id and access_token are mutually exclusive but mandatory.
    """
    if bool(client_id) == bool(access_token):
        raise ValueError('Either client_id or access_token')

    url = 'https://api.quizlet.com/2.0/{}'.format(end_point)

    if not params:
        params = {}
    if client_id:
        params['client_id'] = client_id

    headers = {'Authorization': 'Bearer {}'.format(access_token)} if access_token else None

    response = requests.request(method, url, params=params, headers=headers)

    if int(response.status_code / 100) != 2:
        error_title = ''
        try:
            error_title += ', ' + response.json()['error_title']
        except ValueError:
            pass
        except KeyError:
            pass
        raise ValueError(
            '{} returned {}{}'.format(url, response.status_code, error_title)
        )

    try:
        return response.json()
    except json.decoder.JSONDecodeError:
        pass
