import unittest
from unittest import mock

from main import create_parser, main


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


class TestMain(unittest.TestCase):
    @mock.patch('main.get_common_terms')
    @mock.patch('sys.argv', ['', 'common'])
    def test_common(self, mock_get_common_terms):
        main()
        mock_get_common_terms.assert_called_once()
