import sys
from ft_filter import ft_filter


def main():
    """ Filter words of a string if word len is less or equal than five"""
    args = sys.argv[1:]
    try:
        assert len(args) == 2, "Wrong number of arguments."
        assert isinstance(args[0], str) and args[1].isdigit(), "Bad type!"
        assert all([c.isalnum() or c.isspace() for c in args[0]]), "Bad chars!"
    except AssertionError as e:
        print(f'{type(e).__name__}: {e}', file=sys.stderr)
        return 1
    string, n = args
    it = [i for i in string.split(' ')]
    print(list(ft_filter(lambda x: len(x) > int(n), it)))


if __name__ == "__main__":
    main()
