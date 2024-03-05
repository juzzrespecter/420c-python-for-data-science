#!/usr/bin/env python3
import sys


def read_from_input() -> str:
    """ Reads user input from stdin """
    try:
        print("Please provide a string to parse\n>> ", end="")
        to_parse = sys.stdin.readline()
    except EOFError:
        to_parse = ""
    except KeyboardInterrupt:
        to_parse = ""
    return to_parse


def main():
    """
    Enumerates type of characters of a provided string.
    """
    args = sys.argv[1:]
    try:
        assert len(args) < 2, "invalid number of arguments"
        if len(args) < 1:
            to_parse = read_from_input()
        else:
            to_parse = args[0]
        upper = sum(1 for c in to_parse if c.isupper())
        lower = sum(1 for c in to_parse if c.islower())
        marks = sum(1 for c in to_parse if c in ".?!,;:-~{}()'\"_")
        number = sum(1 for c in to_parse if c.isdigit())
        spaces = sum(1 for c in to_parse if c.isspace())
        print(f"""
        The text contains {len(to_parse)} characters:
        {upper} upper letters.
        {lower} lower letters.
        {marks} punctuation marks.
        {number} digits.
        {spaces} spaces.
        """)
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
