from numpy import ndarray as array
from numpy import asarray
from PIL import Image

import matplotlib as plt


def ft_load(path: str) -> array: #(you can return to the desired format)
    try:
        img = asarray(Image.open(path))
    except Exception as e:
        raise e
        pass