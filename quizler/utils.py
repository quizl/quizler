"""User-available utilities."""
# ToDo: rename the module

from itertools import combinations
from typing import List, Tuple, Set

from quizler.lib import api_call
from quizler.models import WordSet


def get_common_terms(*api_envs) -> List[Tuple[str, str, Set[str]]]:
    """Get all term duplicates across all user word sets."""
    data = api_call('sets', *api_envs)
    wordsets = []
    common_terms = []

    for wordset in data:
        wordsets.append(WordSet(wordset))

    for wordset1, wordset2 in combinations(wordsets, 2):
        common = wordset1.has_common(wordset2)
        if common:
            common_terms.append((wordset1.title, wordset2.title, common))
    return common_terms


def print_common_terms(common_terms: List[Tuple[str, str, Set[str]]]):
    """Print common terms for each pair of word sets."""
    if not common_terms:
        print('No duplicates')
    else:
        for set_pair in common_terms:
            set1, set2, terms = set_pair
            print(f'{set1} and {set2} have in common:')
            for term in terms:
                print(f'    {term}')


def get_user_sets(*api_envs):
    """Find all user sets."""

    # https://api.quizlet.com/2.0/users/USERNAME/sets

    raise NotImplementedError  # ToDo: complete the utility


def apply_regex(pattern, repl, set_name, *api_envs):
    """Apply regex replace to all terms in word set."""
    raise NotImplementedError  # ToDo: complete the utility
