import sys


def validate_input() -> None:
    """ Validate f input contains invalid characters """
    args = sys.argv[1:]
    assert len(args) == 1, "Bad number of arguments!"
    assert all([c.isalnum() or c.isspace() for c in args[0]]), "Bad chars!"


def translate_into_morse(input: str) -> list:
    """ Translate input into morse code """
    input = input.upper()
    morse_dict = {
        " ":  "/ ",
        "A": ".-",
        "B": " -...",
        "C": " -.-.",
        "D": " -..",
        "E": " .",
        "F": " ..-.",
        "G": " --.",
        "H": " ....",
        "I": " ..",
        "J": " .---",
        "K": " -.-",
        "L": " .-..",
        "M": " --",
        "N": " -.",
        "O": " ---",
        "P": " .--.",
        "Q": " --.-",
        "R": " .-.",
        "S": " ...",
        "T": " -",
        "U": " ..-",
        "V": " ...-",
        "W": " .--",
        "X": " -..-",
        "Y": " -.--",
        "Z": " --..",
        "0": "-----",
        "1": " .----",
        "2": " ..---",
        "3": " ...--",
        "4": " ....-",
        "5": " .....",
        "6": " -....",
        "7": " --...",
        "8": " ---..",
        "9": " ----."
    }
    return [morse_dict[c] for c in input]


def main():
    """ Encode a string into morse code """

    try:
        validate_input()
    except AssertionError as e:
        print(f'{type(e).__name__}: {e}', file=sys.stderr)
        return 1
    input = sys.argv[1]
    result = translate_into_morse(input)
    print(" ".join(result))


if __name__ == "__main__":
    main()
