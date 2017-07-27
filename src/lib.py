"""Additional none-user-visible utilities."""

import os

import requests


def get_api_envs():
    """Get required API keys from environment variables."""
    client_id = os.environ.get('CLIENT_ID')
    user_id = os.environ.get('USER_ID')
    if not client_id or not user_id:
        raise ValueError('API keys are not found in the environment')
    return client_id, user_id


def api_call(end_point, client_id, user_id):
    """Call given API end_point with API keys."""
    url = f'https://api.quizlet.com/2.0/users/{user_id}/{end_point}'
    params = {'client_id': client_id}
    response = requests.get(url, params)
    if response.status_code != 200:
        raise ValueError(
            f'Unknown end point, server returns {response.status_code}'
        )
    else:
        return response.json()
