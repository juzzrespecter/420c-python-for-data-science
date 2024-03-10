import numpy as np
from sys import stderr


def validate(lst: list) -> bool:
    """ Validate type of array & has any invalid value """
    try:
        np.array(lst, dtype=float)
    except ValueError:
        return False
    return True

# validacion rota con none
def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """ Returns a list of BMI values, empty array in error """
    if len(height) != len(weight):
        print("Arrays size does not match.", file=stderr)
        return []
    if not validate(height) or not validate(weight):
        print("Array does not comply with type constrains", file=stderr)
        return []
    return (weight / np.power(height, 2)).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """ Checks if arrays of BMI complies with limit """
    if not validate(bmi):
        print()
        return []
    return [x > limit for x in bmi]
