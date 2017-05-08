from invoke import task


@task
def pylint(ctx):
    ctx.run('python -m pylint main.py src tests')


@task
def pydocstyle(ctx):
    ctx.run('python -m pydocstyle')


@task
def pycodestyle(ctx):
    ctx.run('python -m pycodestyle --select E,W .')


@task
def mypy(ctx):
    ctx.run('python -m mypy .')


@task(pylint, pydocstyle, pycodestyle, mypy)
def lint(_):
    pass


@task
def test(ctx):
    ctx.run('python -m pytest tests')
