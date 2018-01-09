from distutils.core import setup

from setuptools import find_packages

version = '0.0.6'

setup(
    name='quizler',
    packages=find_packages(exclude=['tests', '*.test', '*.test.*']),
    version=version,
    description='Set of utils for Quizlet API',
    author='Pavel Karateev',
    author_email='karateev.pavel@ya.ru',
    url='https://github.com/quizl/quizler',
    download_url='https://github.com/quizl/quizler/archive/{}.tar.gz'.format(version),
    keywords=['quizlet', 'api'],
    entry_points={
        'console_scripts': [
            'quizler = quizler.main:main'
        ]
    },
    install_requires=['requests'],
)
