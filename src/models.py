"""OOP models for Quizlet terms abstractions."""

from typing import List, Dict, Set


class WordSet:
    """Set of terms and descriptions."""

    def __init__(self, title: str, terms: List[Dict]) -> None:
        """Where terms are raw data from API call."""
        self.title = title
        self.terms = terms

    def has_common(self, other: 'WordSet') -> Set[str]:
        """Return set of common words between two word sets."""
        if not isinstance(other, WordSet):
            raise ValueError('Can compare only WordSets')
        return self.term_set & other.term_set

    @property
    def term_set(self) -> Set[str]:
        """Set of all terms in WordSet."""
        return {term['term'] for term in self.terms}

    def __str__(self):
        """E.g. "Icelandic Phrases"."""
        return f'{self.title}'

    __repr__ = __str__
