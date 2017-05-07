import unittest

from lib.models import WordSet


class TestWordSet(unittest.TestCase):
    def setUp(self):
        self.word_set_1 = WordSet('WordSet1', [
            {'term': 'term1'},
            {'term': 'term2'}
        ])
        self.word_set_2 = WordSet('WordSet2', [
            {'term': 'term2'},
            {'term': 'term3'}
        ])

    def test_terms_set(self):
        self.assertSetEqual(self.word_set_1.terms_set, {'term1', 'term2'})
        self.assertSetEqual(self.word_set_2.terms_set, {'term2', 'term3'})

    def test_has_common(self):
        self.assertSetEqual(self.word_set_1.has_common(self.word_set_2),
                            {'term2'})
