#!/usr/bin/env python3
import sys

def main():
    args = sys.argv[1:]
    try:
        assert len(args) < 2, "invalid number of arguments"
        if len(args) < 1:
            to_parse =input("Please provide a string to parse\n>> ")
        else:
            to_parse = args[0]
        upper = sum([1 for c in to_parse if c.isupper()])
        lower = sum([1 for c in to_parse if c.islower()])
        marks = sum([1 for c in to_parse if ".?!,;:-~{}()'\"_")
        number = sum([1 for c in to_parse if c.isdigit()])
        print(upper, lower)
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")

if __name__ == "__main__":
    main()
