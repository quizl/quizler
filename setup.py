from distutils.core import setup

from setuptools import find_packages

setup(
    name='quizler',
    packages=find_packages(exclude=['tests', '*.test', '*.test.*']),
    version='0.0.3',
    description='Set of utils for Quizlet API',
    author='Pavel Karateev',
    author_email='karateev.pavel@ya.ru',
    url='https://github.com/lancelote/quizler',
    download_url='https://github.com/lancelote/quizler/archive/0.0.1.tar.gz',
    keywords=['quizlet', 'api'],
    entry_points={
        'console_scripts': [
            'quizler = quizler.main:main'
        ]
    },
    install_requires=['requests'],
)
