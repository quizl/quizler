"""Experiments with Quizlet API."""

from itertools import combinations
from typing import List

import requests

from envs import CLIENT_ID, USER_ID
from src.models import WordSet


def main():
    """Find term duplicates in all user sets."""
    url = f'https://api.quizlet.com/2.0/users/{USER_ID}/sets'
    params = {'client_id': CLIENT_ID}
    response = requests.get(url, params)

    word_sets: List[WordSet] = []
    for word_set in response.json():
        word_sets.append(WordSet(word_set['title'], word_set['terms']))

    for word_set_1, word_set_2 in combinations(word_sets, 2):
        common_terms = word_set_1.has_common(word_set_2)
        if common_terms:
            print(f'{word_set_1.title} and {word_set_2.title} have in common:')
            for term in common_terms:
                print(f'  {term}')


if __name__ == '__main__':
    main()
