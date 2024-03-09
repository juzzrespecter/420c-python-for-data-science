import numpy as np
from numpy import ndarray as array
from PIL import Image


def ft_load(path: str) -> array:
    """
    Loads an image, prints format and its pixels in RGB fmt.
    Returns empty array in failure.

    - path: path to file to open.
    """
    try:
        img = Image.open(path)
        img_arr = np.asarray(img)
        h, w, px_len = img_arr.shape
        print(f"Image shape: height - {h}, width - {w}, px_size - {px_len}")
        print(img_arr)
        return img_arr
    except IOError as e:
        print(f"{type(e).__name__} :: {e}")
    return []
