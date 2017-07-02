"""OOP models for Quizlet terms abstractions."""


class Term:
    """Quizlet term abstraction."""

    def __init__(self, raw_data):
        try:
            self.definition = raw_data['definition']
            self.id = raw_data['id']
            self.image = raw_data['image']
            self.rank = raw_data['rank']
            self.term = raw_data['term']
        except KeyError:
            raise ValueError('Unexpected term json structure')


class WordSet:
    """Quizlet set of terms and descriptions abstraction."""

    def __init__(self, title, terms):
        self.title = title
        self.terms = terms  # ToDo: separate abstraction for Term

    def has_common(self, other):
        """Return set of common words between two word sets."""
        if not isinstance(other, WordSet):
            raise ValueError('Can compare only WordSets')
        return self.term_set & other.term_set

    @property
    def term_set(self):
        """Set of all terms in WordSet."""
        return {term['term'] for term in self.terms}

    def __str__(self):
        return f'{self.title}'

    __repr__ = __str__
