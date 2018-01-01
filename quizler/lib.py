"""Additional none-user-visible utilities."""

from typing import Dict
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


def api_call(method: str, end_point: str, params: Dict[str, str] = None, client_id: str = None,
             access_token: str = None):
    """Call given API end_point with API keys."""
    if bool(client_id) == bool(access_token):
        raise ValueError('Either client_id or access_token')

    url = 'https://api.quizlet.com/2.0/{}'.format(end_point)

    if not params:
        params = {}
    if client_id:
        params['client_id'] = client_id

    headers = {'Authorization': 'Bearer {}'.format(access_token)} if access_token else None

    # pylint: disable=too-many-function-args
    response = requests.request(method, url, params=params, headers=headers)
    # pylint: enable=too-many-function-args

    # pylint: disable=no-member
    if int(response.status_code / 100) != 2:
    # pylint: enable=no-member
        raise ValueError(
            'Unknown end point, server returns {}'.format(response.status_code)
        )

    try:
        return response.json()
    except json.decoder.JSONDecodeError:
        pass
