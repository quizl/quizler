"""Entry point and CLI."""

import argparse

from src.lib import get_api_envs
from src.utils import get_common_terms, apply_regex


def create_parser():
    parser = argparse.ArgumentParser(description='Quizlet Utils')
    commands = parser.add_subparsers(title='Commands', dest='command')
    commands.required = True

    commands.add_parser('common', help='Find duplicate terms across all sets')

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
        get_common_terms(*api_envs)
    elif args.command == 'apply':
        apply_regex(args.pattern, args.repl, args.set_name, *api_envs)


if __name__ == '__main__':
    main()
