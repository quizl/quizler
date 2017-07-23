"""User-available utilities."""
# ToDo: rename the module

from itertools import combinations
from typing import List, Tuple, Set

from src.lib import api_call
from src.models import WordSet


def get_common_terms(*api_envs) -> List[Tuple[WordSet, WordSet, Set[str]]]:
    """Get all term duplicates across all user word sets."""
    response = api_call('sets', *api_envs)
    word_sets = []
    common_terms = []

    for word_set in response.json():
        word_sets.append(WordSet(word_set['title'], word_set['terms']))

    for word_set_1, word_set_2 in combinations(word_sets, 2):
        has_in_common = word_set_1.has_common(word_set_2)
        if has_in_common:
            common_terms.append((word_set_1, word_set_2, has_in_common))
    return common_terms


def print_common_terms(common_terms: List[Tuple[WordSet, WordSet, Set[str]]]):
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
    raise NotImplementedError  # ToDo: complete the utility


def apply_regex(pattern, repl, set_name, *api_envs):
    """Apply regex replace to all terms in word set."""
    raise NotImplementedError  # ToDo: complete the utility
