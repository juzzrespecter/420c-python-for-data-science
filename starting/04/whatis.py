import sys

args = sys.argv[1:]
if len(args) < 1:
    sys.exit(0)
try:
    assert len(args) == 1, "more than one argument is provided"
    num = args[0]
    assert num.isdigit() or (num[0] in "-+" and num[1:].isdigit()), "argument is not an integer"
    n = int(num)
    if n % 2:
        print("I'm Odd")
    else:
        print("I'm Even")
except AssertionError as e:
    print(f'{type(e).__name__}: {e}')