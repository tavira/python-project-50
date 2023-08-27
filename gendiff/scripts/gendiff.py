import argparse

from gendiff.diff.generate_diff import generate_diff


def main():
    args = vars(get_args_from_cmd_usage())
    diff = generate_diff(args['first file'], args['second file'])
    print(diff)


def get_args_from_cmd_usage():
    description = 'Compares two configuration files and shows a difference.'
    arg1_description = 'first file'
    arg2_description = 'second file'
    format_option_help = 'set format of output'

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(arg1_description)
    parser.add_argument(arg2_description)
    parser.add_argument('-f', '--format', help=format_option_help)

    return parser.parse_args()


if __name__ == '__main__':
    main()
