import unittest

from src.models import WordSet


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
        self.assertSetEqual(self.word_set_1.term_set, {'term1', 'term2'})
        self.assertSetEqual(self.word_set_2.term_set, {'term2', 'term3'})

    def test_has_common(self):
        self.assertSetEqual(self.word_set_1.has_common(self.word_set_2),
                            {'term2'})

    def test_has_common_wrong_type(self):
        with self.assertRaises(ValueError):
            # noinspection PyTypeChecker
            self.word_set_1.has_common([1, 2, 3])

    def test_repr(self):
        self.assertEqual(repr(self.word_set_1), 'WordSet1')
        self.assertEqual(repr(self.word_set_2), 'WordSet2')

    def test_str(self):
        self.assertEqual(str(self.word_set_1), 'WordSet1')
        self.assertEqual(str(self.word_set_2), 'WordSet2')
