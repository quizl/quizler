# pylint: disable=missing-docstring

"""Factories for generating test data."""

import factory

from quizler import models


class TermFactory(factory.Factory):
    class Meta:
        model = models.Term

    definition = factory.LazyAttribute(
        lambda obj: 'definition{}'.format(obj.term_id))
    term_id = factory.Sequence(lambda n: n)
    image = None
    rank = 0
    term = factory.LazyAttribute(lambda obj: 'term{}'.format(obj.term_id))


class WordSetFactory(factory.Factory):
    class Meta:
        model = models.WordSet

    set_id = factory.Sequence(lambda n: n)
    title = factory.LazyAttribute(lambda obj: 'title{}'.format(obj.set_id))
    terms = []
