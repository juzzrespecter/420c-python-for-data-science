from numpy import ndarray as array, dot, empty
from load_image import ft_load
from sys import stderr
import matplotlib.pyplot as plt


def apply_zoom(file_array: array) -> array:
    """
    Zooms img to raccoon's face.

    - file_array: original file array
    """
    cropped = file_array[100:500, 450:850, :]
    grayscale = dot(cropped[..., :3], [0.2989, 0.587, 0.114])
    return grayscale


def apply_rotate(file_array: array) -> array:
    """
    Apply rotation to matrix.

    - file_array: matrix to be rotated.
    """
    rot_array = empty(file_array.shape)
    for idx, h in enumerate(file_array):
        for jdx, px in enumerate(h):
            rot_array[jdx][idx] = px
    return rot_array


def main():
    """ Zooms, greyscales, rotates an image """
    file = "animal.jpeg"
    file_array = ft_load(file)
    if len(file_array) < 1:
        print("[ Rotate.py ] Fatal error - could not read image.", file=stderr)
        return
    file_array = apply_zoom(file_array)
    rot_array = apply_rotate(file_array)
    print(f"New shape after transpose: {rot_array.shape}")
    print(rot_array)
    plt.imshow(rot_array, cmap='gray')
    try:
        plt.show()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
