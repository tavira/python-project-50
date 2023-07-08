import argparse


def main():
    args = get_args_from_cmd_usage()
    print(args)


def get_args_from_cmd_usage():
    description = "Compares two configuration files and shows a difference."
    arg1_description = "first file"
    arg2_description = "second file"

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(arg1_description)
    parser.add_argument(arg2_description)

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    main()
