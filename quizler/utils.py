"""User-available utilities."""
# ToDo: rename the module

from itertools import combinations
from typing import List, Tuple, Set

from quizler.lib import api_call
from quizler.models import WordSet


def get_user_sets(*api_envs):
    """Find all user sets."""
    # pylint: disable=no-value-for-parameter
    data = api_call('sets', *api_envs)
    # pylint: enable=no-value-for-parameter
    return [WordSet.from_dict(wordset) for wordset in data]


def print_user_sets(wordsets: List[WordSet], print_terms: bool):
    """Print all user sets by title. If 'print_terms', also prints all terms of all user sets."""
    if not wordsets:
        print('No sets found')
    else:
        print('Found sets: {}'.format(len(wordsets)))
        for wordset in wordsets:
            print('    {}'.format(wordset))
            if print_terms:
                for term in wordset.terms:
                    print('        {}'.format(term))


def get_common_terms(*api_envs) -> List[Tuple[str, str, Set[str]]]:
    """Get all term duplicates across all user word sets."""
    common_terms = []
    wordsets = get_user_sets(*api_envs)

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
            print('{} and {} have in common:'.format(set1, set2))
            for term in terms:
                print('    {}'.format(term))


def apply_regex(pattern, repl, set_name, *api_envs):
    """Apply regex replace to all terms in word set."""
    print('{}, {}, {}, {}'.format(pattern, repl, set_name, api_envs))
    raise NotImplementedError  # ToDo: complete the utility
