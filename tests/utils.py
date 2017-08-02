"""Utilities for tests."""

import inspect
import io
import sys
import unittest
from functools import wraps
from unittest import mock


def mock_envs(**envs):
    """Mock environment variables for test.

    Can be applied to:
      - any function
      - test class - all test methods (starts with "test_*" will be decorated)
    """

    def decorator(obj):
        @wraps(obj)
        def wrapper(*args, **kwargs):
            # clear=True to flush all envs before testing
            with mock.patch.dict('os.environ', envs, clear=True):
                obj(*args, **kwargs)

        if inspect.isclass(obj):
            for name, method in inspect.getmembers(obj, inspect.isfunction):
                if name.startswith('test_'):
                    setattr(obj, name, decorator(method))
            return obj
        else:
            return wrapper

    return decorator


def mock_argv(*cli_args):
    """Mock command line arguments."""

    def decorator(obj):
        @wraps(obj)
        def wrapper(*args, **kwargs):
            # Empty string as first argument to match python CLI parsing
            with mock.patch('sys.argv', [''] + list(cli_args)):
                obj(*args, **kwargs)

        if inspect.isclass(obj):
            for name, method in inspect.getmembers(obj, inspect.isfunction):
                if name.startswith('test_'):
                    setattr(obj, name, decorator(method))
            return obj
        else:
            return wrapper

    return decorator


class MockStdoutTestCase(unittest.TestCase):

    def setUp(self):
        patcher = mock.patch('sys.stdout', new=io.StringIO())
        self.addCleanup(patcher.stop)
        patcher.start()

    def assertStdout(self, expected, new_line=True):
        expected += '\n' if new_line else ''
        self.assertEqual(expected, sys.stdout.getvalue())


# ToDo: remove duplicated lines
