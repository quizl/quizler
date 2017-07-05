"""Entry point and CLI."""

import argparse

from src.lib import get_api_envs
from src.utils import get_common_terms


def create_parser():
    parser = argparse.ArgumentParser(description='Quizlet Utils')
    commands = parser.add_subparsers(title="Commands", dest="command")
    commands.add_parser("common", help="Find duplicate terms across all sets")
    commands.required = True
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    api_envs = get_api_envs()
    if args.command == 'common':
        get_common_terms(*api_envs)


if __name__ == '__main__':
    main()
