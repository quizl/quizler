import unittest
from unittest import mock

from quizler.models import WordSet
from quizler.utils import print_common_terms, get_common_terms, get_user_sets, \
    print_user_sets
from tests.utils import MockStdoutTestCase


@mock.patch('quizler.utils.get_user_sets')
class TestGetCommonTerms(unittest.TestCase):

    def test_one_common_term(self, mock_get_user_sets):
        mock_data = [
            WordSet({'id': 0,
                     'title': 'wordset1',
                     'terms': [{'term': 'term1'}, {'term': 'term2'}]}),
            WordSet({'id': 1,
                     'title': 'wordset2',
                     'terms': [{'term': 'term2'}, {'term': 'term3'}]}),
        ]
        mock_get_user_sets.return_value = mock_data
        self.assertEqual(
            get_common_terms(),
            [('wordset1', 'wordset2', {'term2'})]
        )

    def test_no_common_terms(self, mock_get_user_sets):
        mock_data = [
            WordSet({'id': 0,
                     'title': 'wordset1',
                     'terms': [{'term': 'term1'}, {'term': 'term2'}]}),
            WordSet({'id': 1,
                     'title': 'wordset2',
                     'terms': [{'term': 'term3'}, {'term': 'term4'}]})
        ]
        mock_get_user_sets.return_value = mock_data
        self.assertEqual(get_common_terms(), [])


class TestPrintCommonTerms(MockStdoutTestCase):

    def test_no_duplicates(self):
        print_common_terms([])
        self.assertStdout('No duplicates')

    def test_duplicates_in_one_pair(self):
        print_common_terms([('wordset1', 'wordset2', {'term1'})])
        self.assertStdout('wordset1 and wordset2 have in common:\n'
                          '    term1')

    def test_duplicates_in_multiple_pairs(self):
        print_common_terms([
            ('wordset1', 'wordset2', {'term12'}),
            ('wordset2', 'wordset3', {'term23'})
        ])
        self.assertStdout('wordset1 and wordset2 have in common:\n'
                          '    term12\n'
                          'wordset2 and wordset3 have in common:\n'
                          '    term23')


@mock.patch('quizler.utils.api_call')
class TestGetUserSets(unittest.TestCase):

    def test_there_are_sets(self, mock_api_call):
        mock_data = [
            {
                'id': 0,
                'title': 'wordset1',
                'terms': [{'term': 'term1'}, {'term': 'term2'}]
            },
            {
                'id': 1,
                'title': 'wordset2',
                'terms': [{'term': 'term3'}, {'term': 'term4'}]
            }
        ]
        # ToDo: bad testing - same logic in the code
        wordsets = [WordSet(wordset) for wordset in mock_data]
        mock_api_call.return_value = mock_data
        self.assertEqual(get_user_sets(), wordsets)

    def test_there_are_no_sets(self, mock_api_call):
        mock_api_call.return_value = []
        self.assertEqual(get_user_sets(), [])


class TestPrintUserSets(MockStdoutTestCase):

    def test_no_sets(self):
        print_user_sets([])
        self.assertStdout('No sets found')

    def test_one_set(self):
        print_user_sets([WordSet({'id': 0, 'title': 'wordset0', 'terms': []})])
        self.assertStdout('Found sets: 1\n'
                          '    wordset0')

    def test_two_sets(self):
        print_user_sets([
            WordSet({'id': 0, 'title': 'wordset0', 'terms': []}),
            WordSet({'id': 1, 'title': 'wordset1', 'terms': []}),
        ])
        self.assertStdout('Found sets: 2\n'
                          '    wordset0\n'
                          '    wordset1')


class TestApplyRegex(unittest.TestCase):
    ...
