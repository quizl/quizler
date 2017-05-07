class WordSet:
    def __init__(self, title, terms):
        self.title = title
        self.terms = terms

    def has_common(self, other: 'WordSet'):
        """Check how many common words do sets have."""
        if not isinstance(other, WordSet):
            raise ValueError('Can compare only WordSets')
        return self.terms_set & other.terms_set

    @property
    def terms_set(self):
        """Set of all terms in WordSet."""
        return {term['term'] for term in self.terms}

    def __str__(self):
        return f'{self.title}'

    __repr__ = __str__
