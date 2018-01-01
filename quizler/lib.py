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


def api_call(method: str, end_point: str, params: Dict[str, str], client_id: str):
    """Call given API end_point with API keys."""
    url = 'https://api.quizlet.com/2.0/{}'.format(end_point)
    params['client_id'] = client_id
    # pylint: disable=too-many-function-args
    response = requests.request(method, url, params=params)
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
