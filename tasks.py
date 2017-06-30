"""Project management utils.

Run with e.g.:
    inv lint
"""

from invoke import task


@task
def pylint(ctx):
    """Run pylint, settings are stored in pylintrc file."""
    ctx.run('python -m pylint src tests')


@task
def pydocstyle(ctx):
    """Run pydocstyle."""
    ctx.run('python -m pydocstyle')


@task
def pycodestyle(ctx):
    """Run pycodestyle."""
    ctx.run('python -m pycodestyle --select E,W .')


@task
def mypy(ctx):
    """Run mypy type checker."""
    ctx.run('python -m mypy --ignore-missing-imports .')


@task(pylint, pydocstyle, pycodestyle, mypy)
def lint(_):
    """Run all linters at once."""
    pass


@task
def test(ctx):
    """Execute all tests with pytest test runner."""
    ctx.run('python -m pytest tests')
