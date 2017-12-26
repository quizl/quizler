"""OOP models for Quizlet terms abstractions."""


class Term:
    """Quizlet term abstraction."""

    def __init__(self, definition, term_id, image, rank, term):
        self.definition = definition
        # pylint: disable=invalid-name
        self.id = term_id
        # pylint: enable=invalid-name
        self.image = image
        self.rank = rank
        self.term = term

    @staticmethod
    def from_dict(raw_data):
        """Create Term from raw dictionary data."""
        try:
            definition = raw_data['definition']
            term_id = raw_data['id']
            image = raw_data['image']
            rank = raw_data['rank']
            term = raw_data['term']
            return Term(definition, term_id, image, rank, term)
        except KeyError:
            raise ValueError('Unexpected term json structure')

    def to_dict(self):
        """Convert Term into raw dictionary data."""
        return {
            'definition': self.definition,
            'id': self.id,
            'image': self.image,
            'rank': self.rank,
            'term': self.term
        }

    def __eq__(self, other):
        if not isinstance(other, Term):
            raise ValueError
        return all((
            self.definition == other.definition,
            self.id == other.id,
            self.image == other.image,
            self.rank == other.rank,
            self.term == other.term
        ))


class WordSet:
    """Quizlet set of terms and descriptions abstraction."""

    def __init__(self, set_id, title, terms):
        # pylint: disable=invalid-name
        self.id = set_id
        # pylint: enable=invalid-name
        self.title = title
        self.terms = terms

    def has_common(self, other):
        """Return set of common words between two word sets."""
        if not isinstance(other, WordSet):
            raise ValueError('Can compare only WordSets')
        return self.term_set & other.term_set

    @property
    def term_set(self):
        """Set of all terms in WordSet."""
        return {term.term for term in self.terms}

    @staticmethod
    def from_dict(raw_data):
        """Create WordSet from raw dictionary data."""
        try:
            set_id = raw_data['id']
            title = raw_data['title']
            terms = [Term.from_dict(term) for term in raw_data['terms']]
            return WordSet(set_id, title, terms)
        except KeyError:
            raise ValueError('Unexpected set json structure')

    def to_dict(self):
        """Convert WordSet into raw dictionary data."""
        return {
            'id': self.id,
            'title': self.title,
            'terms': [term.to_dict() for term in self.terms]
        }

    def __eq__(self, other):
        return all((
            self.id == other.id,
            self.title == other.title,
            self.terms == other.terms
        ))

    def __str__(self):
        return '{}'.format(self.title)

    def __repr__(self):
        return 'WordSet(id={}, title={})'.format(self.id, self.title)
