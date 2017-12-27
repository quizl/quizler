# pylint: disable=no-self-use,missing-docstring,invalid-name

import unittest
from unittest import mock

from quizler.models import WordSet
from quizler.utils import print_common_terms, get_common_terms, get_user_sets, \
    print_user_sets
from tests.factories import TermFactory, WordSetFactory
from tests.utils import MockStdoutTestCase


@mock.patch('quizler.utils.get_user_sets')
class TestGetCommonTerms(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.term0 = TermFactory()
        cls.term1 = TermFactory()
        cls.term2 = TermFactory()
        cls.term3 = TermFactory()

    def test_one_common_term(self, mock_get_user_sets):
        wordset0 = WordSetFactory(terms=[self.term0, self.term1])
        wordset1 = WordSetFactory(terms=[self.term1, self.term2])
        mock_data = [wordset0, wordset1]
        mock_get_user_sets.return_value = mock_data
        assert get_common_terms() == [
            (wordset0.title, wordset1.title, {self.term1.term})]

    def test_no_common_terms(self, mock_get_user_sets):
        wordset0 = WordSetFactory(terms=[self.term0, self.term1])
        wordset1 = WordSetFactory(terms=[self.term2, self.term3])
        mock_data = [wordset0, wordset1]
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
        wordset0 = WordSetFactory(terms=[TermFactory()])
        wordset1 = WordSetFactory(terms=[TermFactory()])

        mock_data = [wordset0.to_dict(), wordset1.to_dict()]
        wordsets = [WordSet.from_dict(wordset) for wordset in mock_data]
        mock_api_call.return_value = mock_data
        assert get_user_sets() == wordsets

    def test_there_are_no_sets(self, mock_api_call):
        mock_api_call.return_value = []
        self.assertEqual(get_user_sets(), [])


class TestPrintUserSets(MockStdoutTestCase):

    def test_no_sets(self):
        print_user_sets([], False)
        self.assertStdout('No sets found')

    def test_one_set(self):
        wordset = WordSetFactory()
        print_user_sets([wordset], False)
        self.assertStdout('Found sets: 1\n'
                          '    {}'.format(wordset.title))

    def test_two_sets_without_terms(self):
        wordset0 = WordSetFactory(terms=[TermFactory(), TermFactory()])
        wordset1 = WordSetFactory(terms=[TermFactory(), TermFactory()])
        print_user_sets([wordset0, wordset1], False)
        self.assertStdout('Found sets: 2\n'
                          '    {}\n'
                          '    {}'.format(wordset0.title, wordset1.title))

    def test_two_sets_with_terms(self):
        term0 = TermFactory()
        term1 = TermFactory()
        term2 = TermFactory()
        wordset0 = WordSetFactory(terms=[term0, term1])
        wordset1 = WordSetFactory(terms=[term2])
        print_user_sets([wordset0, wordset1], True)
        self.assertStdout('Found sets: 2\n'
                          '    {}\n'
                          '        {} = {}\n'
                          '        {} = {}\n'
                          '    {}\n'
                          '        {} = {}'
                          .format(wordset0.title, term0.term, term0.definition, term1.term,
                                  term1.definition, wordset1.title, term2.term, term2.definition))
