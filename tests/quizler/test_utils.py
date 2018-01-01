# pylint: disable=no-self-use,missing-docstring,invalid-name

import unittest
from unittest import mock

from quizler.models import WordSet
from quizler.utils import print_common_terms, get_common_terms, get_user_sets, \
    print_user_sets, delete_term, add_term, reset_term_stats
from tests.factories import ImageFactory, TermFactory, WordSetFactory
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
        assert get_user_sets('client_id', 'user_id') == wordsets

    def test_there_are_no_sets(self, mock_api_call):
        mock_api_call.return_value = []
        self.assertEqual(get_user_sets('client_id', 'user_id'), [])


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


@mock.patch('quizler.utils.api_call')
class TestDeleteTerm(unittest.TestCase):

    def test_one_term(self, mock_api_call):
        set_id = 1
        term_id = 2
        access_token = 'token'
        delete_term(set_id, term_id, access_token)
        mock_api_call.assert_called_once_with(
            'delete',
            'sets/{}/terms/{}'.format(set_id, term_id),
            access_token=access_token
        )


@mock.patch('quizler.utils.api_call')
class TestAddTerm(unittest.TestCase):

    def test_one_term(self, mock_api_call):
        set_id = 1
        term = TermFactory()
        access_token = 'token'
        add_term(set_id, term, access_token)
        mock_api_call.assert_called_once_with(
            'post',
            'sets/{}/terms'.format(set_id),
            term.to_dict(),
            access_token=access_token
        )


@mock.patch('quizler.utils.get_user_sets')
class TestResetTermStats(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.term0 = TermFactory(image=ImageFactory(url='http://domain.com/myimage.png'))
        cls.term1 = TermFactory()
        cls.term2 = TermFactory()
        cls.wordset0 = WordSetFactory(terms=[cls.term0, cls.term1])
        cls.wordset1 = WordSetFactory(terms=[cls.term2])
        cls.wordsets = [cls.wordset0, cls.wordset1]

    def test_set_not_found(self, mock_get_user_sets):
        mock_get_user_sets.return_value = self.wordsets
        unknown_set_id = -1
        term_id = self.term0.term_id
        client_id = 1
        user_id = 2
        access_token = 'token'
        with self.assertRaises(ValueError):
            reset_term_stats(unknown_set_id, term_id, client_id, user_id, access_token)

    def test_term_not_found(self, mock_get_user_sets):
        mock_get_user_sets.return_value = self.wordsets
        set_id = self.wordset0.set_id
        unknown_term_id = -1
        client_id = 1
        user_id = 2
        access_token = 'token'
        with self.assertRaises(ValueError):
            reset_term_stats(set_id, unknown_term_id, client_id, user_id, access_token)

    def test_term_has_image(self, mock_get_user_sets):
        mock_get_user_sets.return_value = self.wordsets
        set_id = self.wordset0.set_id
        term_id = self.term0.term_id
        client_id = 1
        user_id = 2
        access_token = 'token'
        with self.assertRaises(NotImplementedError):
            reset_term_stats(set_id, term_id, client_id, user_id, access_token)

    @mock.patch('quizler.utils.add_term')
    @mock.patch('quizler.utils.delete_term')
    def test_one_term(self, mock_delete_term, mock_add_term, mock_get_user_sets):
        mock_get_user_sets.return_value = self.wordsets
        set_id = self.wordset0.set_id
        term_id = self.term1.term_id
        client_id = 1
        user_id = 2
        access_token = 'token'
        reset_term_stats(set_id, term_id, client_id, user_id, access_token)
        mock_delete_term.assert_called_once_with(set_id, term_id, access_token)
        mock_add_term.assert_called_once_with(set_id, self.term1, access_token)
