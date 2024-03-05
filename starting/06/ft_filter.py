from typing import Optional, Callable, Iterable


def ft_filter(fn: Optional[Callable], it: Iterable) -> filter:
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    if fn is None:
        return (i for i in it if i)
    return (i for i in it if fn(i))
