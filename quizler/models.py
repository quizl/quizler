"""OOP models for Quizlet terms abstractions."""
from typing import List, Dict


# ToDo: base class for Term and WordSet
class Term:
    """Quizlet term abstraction."""

    def __init__(self, raw_data):
        try:
            # ToDo: type annotations
            self.definition = raw_data['definition']
            self.id = raw_data['id']
            self.image = raw_data['image']
            self.rank = raw_data['rank']
            self.term = raw_data['term']
        except KeyError:
            raise ValueError('Unexpected term json structure')


class WordSet:
    """Quizlet set of terms and descriptions abstraction."""

    def __init__(self, raw_data):
        try:
            self.set_id: int = raw_data['id']
            self.title: str = raw_data['title']
            # ToDo: separate abstraction for Terms
            self.terms: List[Dict] = raw_data['terms']
        except KeyError:
            raise ValueError('Unexpected set json structure')

    def has_common(self, other):
        """Return set of common words between two word sets."""
        if not isinstance(other, WordSet):
            raise ValueError('Can compare only WordSets')
        return self.term_set & other.term_set

    @property
    def term_set(self):
        """Set of all terms in WordSet."""
        return {term['term'] for term in self.terms}

    def __eq__(self, other):
        # ToDo: introduce better solution
        return all((
            self.set_id == other.set_id,
            self.title == other.title,
            self.terms == other.terms
        ))

    def __str__(self):
        return f'{self.title}'

    __repr__ = __str__
