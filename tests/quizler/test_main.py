import unittest
from unittest import mock

from quizler.main import create_parser, main
from tests.utils import mock_envs, mock_argv


class TestCreateParser(unittest.TestCase):

    def setUp(self):
        self.parser = create_parser()

    def test_with_empty_args(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args([])

    def test_unknown_command(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['ping'])

    def test_common_command(self):
        args = self.parser.parse_args(['common'])
        self.assertEqual(args.command, 'common')

    def test_sets_command(self):
        args = self.parser.parse_args(['sets'])
        self.assertEqual(args.command, 'sets')

    def test_apply_command_without_args(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['apply'])

    def test_apply_command_with_all_args(self):
        args = self.parser.parse_args(['apply', 'pattern', 'repl', 'set_name'])
        self.assertEqual(args.command, 'apply')
        self.assertEqual(args.pattern, 'pattern')
        self.assertEqual(args.repl, 'repl')
        self.assertEqual(args.set_name, 'set_name')


@mock_envs(CLIENT_ID='client_id', USER_ID='user_id')
class TestMain(unittest.TestCase):

    @mock.patch('quizler.main.get_common_terms')
    @mock.patch('quizler.main.print_common_terms')
    @mock_argv('common')
    def test_common(self, mock_get_common_terms, mock_print_common_terms):
        main()
        mock_get_common_terms.assert_called_once()
        mock_print_common_terms.assert_called_once()

    @mock.patch('quizler.main.get_user_sets')
    @mock_argv('sets')
    def test_sets(self, mock_get_user_sets):
        main()
        mock_get_user_sets.assert_called_once()

    @mock.patch('quizler.main.apply_regex')
    @mock_argv('apply', 'pattern', 'repl', 'set_name')
    def test_apply(self, mock_apply_regex):
        main()
        mock_apply_regex.assert_called_once()
