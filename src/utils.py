"""User-available utilities."""

from itertools import combinations

from src.lib import api_call
from src.models import WordSet


def get_common_terms():
    """Get all term duplicates across all user word sets."""
    response = api_call('sets')
    word_sets = []
    common_terms = []

    for word_set in response.json():
        word_sets.append(WordSet(word_set['title'], word_set['terms']))

    for word_set_1, word_set_2 in combinations(word_sets, 2):
        common_terms.append(
            (word_set_1, word_set_2, word_set_1.has_common(word_set_2)))
    return common_terms
