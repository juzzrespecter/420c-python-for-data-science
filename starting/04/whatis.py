import sys

args = sys.argv[1:]
if len(args) < 1:
    sys.exit(0)
try:
    assert args[0].isdigit(), "argument is not an integer"
    assert len(args) == 1, "more than one argument is provided"
    n = int(args[0])
    if n % 2:
        print("I'm Even")
    else:
        print("I'm Odd")
except AssertionError as e:
    print(f'{type(e).__name__}: {e}')