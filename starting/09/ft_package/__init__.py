def count_in_list(haystack: list, needle: str):
    """ Returns number of appareances of element in list """
    return sum(1 for e in haystack if e == needle)
