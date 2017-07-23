import unittest

from src.models import WordSet
from src.utils import print_common_terms
from tests.utils import MockStdoutTestCase


class TestGetCommonTerms(unittest.TestCase):
    ...  # ToDo: complete tests


class TestPrintCommonTerms(MockStdoutTestCase):
    def test_no_duplicates(self):
        print_common_terms([])
        self.assertStdout('No duplicates')

    def test_duplicates_in_one_pair(self):
        wordset1 = WordSet('wordset1', [])
        wordset2 = WordSet('wordset2', [])
        print_common_terms([(wordset1, wordset2, {'term1'})])
        self.assertStdout('wordset1 and wordset2 have in common:\n'
                          '    term1')

    def test_duplicates_in_multiple_pairs(self):
        wordset1 = WordSet('wordset1', [])
        wordset2 = WordSet('wordset2', [])
        wordset3 = WordSet('wordset3', [])
        print_common_terms([
            (wordset1, wordset2, {'term12'}),
            (wordset2, wordset3, {'term23'})
        ])
        self.assertStdout('wordset1 and wordset2 have in common:\n'
                          '    term12\n'
                          'wordset2 and wordset3 have in common:\n'
                          '    term23')
