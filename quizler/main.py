# pylint: disable=missing-docstring

"""Entry point and CLI."""

import argparse

from quizler.lib import get_api_envs
from quizler.utils import get_common_terms, apply_regex, get_user_sets, print_common_terms, \
                          print_user_sets


def create_parser():
    parser = argparse.ArgumentParser(description='Quizlet Utils')
    commands = parser.add_subparsers(title='Commands', dest='command')
    commands.required = True

    # Common
    commands.add_parser('common', help='Find duplicate terms across all sets')

    # Sets
    sets = commands.add_parser('sets', help='List all your sets')
    sets.add_argument('--terms', action='store_true', help='List all terms of all sets')

    # Apply
    apply = commands.add_parser('apply', help='Apply regex replace to set')
    apply.add_argument('pattern', type=str, help='Pattern to search for')
    apply.add_argument('repl', type=str, help='Replacement for pattern')
    apply.add_argument('set_name', type=str, help='Word set to apply to')

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    api_envs = get_api_envs()
    if args.command == 'common':
        common_terms = get_common_terms(*api_envs)
        print_common_terms(common_terms)
    elif args.command == 'sets':
        user_sets = get_user_sets(*api_envs)
        print_user_sets(user_sets, args.terms)
    elif args.command == 'apply':
        apply_regex(args.pattern, args.repl, args.set_name, *api_envs)


if __name__ == '__main__':
    main()
