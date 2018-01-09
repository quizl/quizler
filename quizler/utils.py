"""User-available utilities."""
# ToDo: rename the module

from itertools import combinations

from quizler.lib import api_call
from quizler.models import WordSet


def get_user_sets(client_id, user_id):
    """Find all user sets."""
    data = api_call('get', 'users/{}/sets'.format(user_id), client_id=client_id)
    return [WordSet.from_dict(wordset) for wordset in data]


def print_user_sets(wordsets, print_terms):
    """Print all user sets by title. If 'print_terms', also prints all terms of all user sets.
    :param wordsets: List of WordSet.
    :param print_terms: If True, also prints all terms of all user sets.
    """
    if not wordsets:
        print('No sets found')
    else:
        print('Found sets: {}'.format(len(wordsets)))
        for wordset in wordsets:
            print('    {}'.format(wordset))
            if print_terms:
                for term in wordset.terms:
                    print('        {}'.format(term))


def get_common_terms(*api_envs):
    """Get all term duplicates across all user word sets as a list of
    (title of first word set, title of second word set, set of terms) tuples."""
    common_terms = []
    # pylint: disable=no-value-for-parameter
    wordsets = get_user_sets(*api_envs)
    # pylint: enable=no-value-for-parameter

    for wordset1, wordset2 in combinations(wordsets, 2):
        common = wordset1.has_common(wordset2)
        if common:
            common_terms.append((wordset1.title, wordset2.title, common))
    return common_terms


def print_common_terms(common_terms):
    """Print common terms for each pair of word sets.
    :param common_terms: Output of get_common_terms().
    """
    if not common_terms:
        print('No duplicates')
    else:
        for set_pair in common_terms:
            set1, set2, terms = set_pair
            print('{} and {} have in common:'.format(set1, set2))
            for term in terms:
                print('    {}'.format(term))


def delete_term(set_id, term_id, access_token):
    """Delete the given term."""
    api_call('delete', 'sets/{}/terms/{}'.format(set_id, term_id), access_token=access_token)


def add_term(set_id, term, access_token):
    """Add the given term to the given set.
    :param term: Instance of Term.
    """
    api_call('post', 'sets/{}/terms'.format(set_id), term.to_dict(), access_token=access_token)


def reset_term_stats(set_id, term_id, client_id, user_id, access_token):
    """Reset the stats of a term by deleting and re-creating it."""
    found_sets = [user_set for user_set in get_user_sets(client_id, user_id)
                  if user_set.set_id == set_id]
    if len(found_sets) != 1:
        raise ValueError('{} set(s) found with id {}'.format(len(found_sets), set_id))
    found_terms = [term for term in found_sets[0].terms if term.term_id == term_id]
    if len(found_terms) != 1:
        raise ValueError('{} term(s) found with id {}'.format(len(found_terms), term_id))
    term = found_terms[0]

    if term.image.url:
        # Creating a term with an image requires an "image identifier", which you get by uploading
        # an image via https://quizlet.com/api/2.0/docs/images , which can only be used by Quizlet
        # PLUS members.
        raise NotImplementedError('"{}" has an image and is thus not supported'.format(term))

    print('Deleting "{}"...'.format(term))
    delete_term(set_id, term_id, access_token)
    print('Re-creating "{}"...'.format(term))
    add_term(set_id, term, access_token)
    print('Done')
