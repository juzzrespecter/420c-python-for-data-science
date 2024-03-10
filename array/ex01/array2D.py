import numpy as np
from sys import stderr


def validate_arr(lst: list) -> bool:
    """
    Validate list constrains for slice_me fn.

    - lst: 2D list
    """
    try:
        np.array(lst)
    except ValueError:
        return False
    return isinstance(lst, list) and all(isinstance(el, list) for el in lst)

# esto esta roto
def validate_index(i: int, j: int) -> bool:
    """
    Validate indexes, must be integers

    - i: start index
    - j: end index
    """

    try:
        int(i), int(j)
    except ValueError:
        return False
    return True


def slice_me(family: list, start: int, end: int) -> list:
    """
    Prints shape of a 2D array and slices using provided arguments.
    Returns None with invalid input.

    - family: 2D array to slice.
    - start, end: indexes of slice.
    """

    if not validate_arr(family) or not validate_index(start, end):
        print("Invalid input, espabila", file=stderr)
        return None
    arr = np.array(family)
    sliced_arr = arr[start:end]
    print(f"My shape is: {arr.shape}")
    print(f"My new shape is: {sliced_arr.shape}")
    return arr[start:end]
