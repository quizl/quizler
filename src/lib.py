"""Additional none-user-visible utilities."""

import requests

from envs import CLIENT_ID, USER_ID


def api_call(end_point):
    """Call given API end_point."""
    url = f'https://api.quizlet.com/2.0/users/{USER_ID}/{end_point}'
    params = {'client_id': CLIENT_ID}
    response = requests.get(url, params)
    if response.status_code != 200:
        raise ValueError(
            f'Unknown end point, server returns {response.status_code}'
        )
    else:
        return response
