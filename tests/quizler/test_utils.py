import unittest
from unittest import mock

from quizler.utils import print_common_terms, get_common_terms
from tests.utils import MockStdoutTestCase


@mock.patch('quizler.utils.api_call')
class TestGetCommonTerms(unittest.TestCase):

    def test_one_common_term(self, mock_api_call):
        mock_data = [
            {
                'title': 'wordset1',
                'terms': [{'term': 'term1'}, {'term': 'term2'}]
            },
            {
                'title': 'wordset2',
                'terms': [{'term': 'term2'}, {'term': 'term3'}]
            }
        ]
        mock_api_call.return_value = mock_data
        self.assertEqual(
            get_common_terms(),
            [('wordset1', 'wordset2', {'term2'})]
        )

    def test_no_common_terms(self, mock_apy_call):
        mock_data = [
            {
                'title': 'wordset1',
                'terms': [{'term': 'term1'}, {'term': 'term2'}]
            },
            {
                'title': 'wordset2',
                'terms': [{'term': 'term3'}, {'term': 'term4'}]
            }
        ]
        mock_apy_call.return_value = mock_data
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

    def test_there_are_sets(self):
        pass

    def test_there_are_no_sets(self):
        pass
