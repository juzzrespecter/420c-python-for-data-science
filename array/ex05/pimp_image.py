from numpy import ndarray as array, copy, empty


def ft_invert(arr: array) -> array:
    """ Applies invert filter color to image """
    return 255 - arr


def ft_red(arr: array) -> array:
    """ Applies red filter color to image """
    if not isinstance(arr, array):
        arr = array(arr)
    red = copy(arr)
    red[..., 1] = 0
    red[..., 2] = 0
    return red


def ft_green(arr: array) -> array:
    """ Applies green filter color to image """
    if not isinstance(arr, array):
        arr = array(arr)
    green = copy(arr)
    green[..., 0] = 0
    green[..., 2] = 0
    return green


def ft_blue(arr: array) -> array:
    """ Applies blue filter color to image """
    if not isinstance(arr, array):
        arr = array(arr)
    blue = copy(arr)
    blue[..., 0] = 0
    blue[..., 1] = 0
    return blue


def ft_grey(arr: array) -> array:
    """ Applies greyscale to image """
    if not isinstance(arr, array):
        arr = array(arr)
    grey = empty((arr.shape[0], arr.shape[1], 1))
    for idx, h in enumerate(arr):
        for jdx, px in enumerate(h):
            _, g, _ = px
            grey[idx][jdx][0] = g
    return grey
