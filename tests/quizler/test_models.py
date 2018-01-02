# pylint: disable=no-self-use,missing-docstring,invalid-name

import unittest

import pytest
from quizler.models import Term, WordSet
from tests.factories import TermFactory, WordSetFactory


class TestTerm(unittest.TestCase):

    def test_from_dict(self):
        raw_data = {
            'definition': 'term definition',
            'id': 12345,
            'image': None,
            'rank': 0,
            'term': 'term'
        }
        term = Term.from_dict(raw_data)
        assert term.definition == 'term definition'
        assert term.term_id == 12345
        assert term.image is None
        assert term.rank == 0
        assert term.term == 'term'

    def test_wrong_term_json_structure(self):
        with self.assertRaises(ValueError):
            Term.from_dict({'some data': '142% unexpected'})

    def test_correct_init(self):
        term = Term('definition', 1, None, 0, 'term')
        assert term.definition == 'definition'
        assert term.term_id == 1
        assert term.image is None
        assert term.term == 'term'

    def test_to_dict(self):
        term = Term('definition1', 1, None, 1, 'term1')
        assert term.to_dict() == {
            'definition': 'definition1',
            'id': 1,
            'image': None,
            'rank': 1,
            'term': 'term1'
        }

    def test_equal_terms(self):
        term0 = Term('definition', 0, None, 0, 'term')
        term1 = Term('definition', 0, None, 0, 'term')
        assert term0 == term1

    def test_unequal_terms(self):
        term0 = Term('definition0', 0, None, 0, 'term0')
        term1 = Term('definition1', 1, None, 0, 'term1')
        assert term0 != term1

    def test_wrong_equality_type(self):
        with pytest.raises(ValueError):
            assert TermFactory() == 1


class TestWordSet(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.term0 = TermFactory()
        cls.term1 = TermFactory()
        cls.term2 = TermFactory()
        cls.word_set_0 = WordSetFactory(terms=[cls.term0, cls.term1])
        cls.word_set_1 = WordSetFactory(terms=[cls.term1, cls.term2])

    def test_terms_set(self):
        assert self.word_set_0.term_set == {self.term0.term, self.term1.term}
        assert self.word_set_1.term_set == {self.term1.term, self.term2.term}

    def test_has_common(self):
        assert self.word_set_0.has_common(self.word_set_1) == {self.term1.term}

    def test_has_common_wrong_type(self):
        with self.assertRaises(ValueError):
            self.word_set_0.has_common([1, 2, 3])

    def test_from_dict(self):
        raw_data = {
            'id': 0,
            'title': 'title0',
            'terms': [
                {
                    'definition': 'definition0',
                    'id': 0,
                    'image': None,
                    'rank': 0,
                    'term': 'term0'
                }
            ]
        }
        wordset = WordSet.from_dict(raw_data)
        assert wordset.set_id == 0
        assert wordset.title == 'title0'
        assert wordset.terms == [Term('definition0', 0, None, 0, 'term0')]

    def test_from_bad_dict(self):
        with pytest.raises(ValueError):
            WordSet.from_dict({})

    def test_to_dict(self):
        wordset = WordSet(0, 'title0', [Term('def0', 0, None, 0, 'term0')])
        assert wordset.to_dict() == {
            'id': 0,
            'title': 'title0',
            'terms': [
                {
                    'definition': 'def0',
                    'id': 0,
                    'image': None,
                    'rank': 0,
                    'term': 'term0'
                }
            ]
        }

    def test_equal_wordsets(self):
        term = TermFactory()
        wordset0 = WordSet(0, 'title', terms=[term])
        wordset1 = WordSet(0, 'title', terms=[term])
        assert wordset0 == wordset1

    def test_unequal_wordsets(self):
        wordset0 = WordSet(0, 'title0', [])
        wordset1 = WordSet(1, 'title1', [])
        assert wordset0 != wordset1

    def test_equal_wordsets_with_different_terms(self):
        term0 = TermFactory()
        term1 = TermFactory()
        wordset0 = WordSet(0, 'title', terms=[term0])
        wordset1 = WordSet(0, 'title', terms=[term1])
        assert wordset0 != wordset1

    def test_repr(self):
        assert repr(self.word_set_0) == 'WordSet(id={}, title={})'.format(
            self.word_set_0.set_id, self.word_set_0.title)
        assert repr(self.word_set_1) == 'WordSet(id={}, title={})'.format(
            self.word_set_1.set_id, self.word_set_1.title)

    def test_str(self):
        assert str(self.word_set_0) == self.word_set_0.title
        assert str(self.word_set_1) == self.word_set_1.title
