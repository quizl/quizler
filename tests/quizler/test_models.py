import unittest

from quizler.models import WordSet, Term


class TestTerm(unittest.TestCase):

    def test_correct_init(self):
        raw_data = {
            'definition': 'term definition',
            'id': 12345,
            'image': None,
            'rank': 0,
            'term': 'term'
        }
        term = Term(raw_data)
        self.assertEqual(term.definition, 'term definition')
        self.assertEqual(term.id, 12345)
        self.assertEqual(term.image, None)
        self.assertEqual(term.rank, 0)
        self.assertEqual(term.term, 'term')

    def test_wrong_term_json_structure(self):
        with self.assertRaises(ValueError):
            Term({'some data': '142% unexpected'})


class TestWordSet(unittest.TestCase):

    def setUp(self):
        self.word_set_1 = WordSet({
            'id': 0,
            'title': 'WordSet1',
            'terms': [{'term': 'term1'},
                      {'term': 'term2'}]
        })
        self.word_set_2 = WordSet({
            'id': 1,
            'title': 'WordSet2',
            'terms': [{'term': 'term2'},
                      {'term': 'term3'}]
        })

    def test_terms_set(self):
        self.assertSetEqual(self.word_set_1.term_set, {'term1', 'term2'})
        self.assertSetEqual(self.word_set_2.term_set, {'term2', 'term3'})

    def test_has_common(self):
        self.assertSetEqual(
            self.word_set_1.has_common(self.word_set_2),
            {'term2'}
        )

    def test_has_common_wrong_type(self):
        with self.assertRaises(ValueError):
            self.word_set_1.has_common([1, 2, 3])

    def test_repr(self):
        self.assertEqual(repr(self.word_set_1), 'WordSet1')
        self.assertEqual(repr(self.word_set_2), 'WordSet2')

    def test_str(self):
        self.assertEqual(str(self.word_set_1), 'WordSet1')
        self.assertEqual(str(self.word_set_2), 'WordSet2')
