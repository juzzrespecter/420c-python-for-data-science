from load_image import ft_load
from sys import stderr
from numpy import ndarray as array, dot
import matplotlib.pyplot as plt


def apply_zoom(file_array: array) -> array:
    """
    Zooms img to raccoon's face.

    - file_array: original file array
    """
    cropped = file_array[100:500, 450:850, :]
    grayscale = dot(cropped[..., :3], [0.2989, 0.587, 0.114])
    return grayscale


def main():
    """
    Loads 'animal.jpeg' image, displays its shape and content,
    then slices it and shows zoomed image.
    """
    file = "animal.jpeg"
    file_array = ft_load(file)
    if len(file_array) < 1:
        print("[ Zoom.py ] Fatal error - could not read image.", file=stderr)
        return
    file_array = apply_zoom(file_array)
    print(f"Image shape after zoom: {file_array.shape}")
    print(file_array)
    plt.imshow(file_array, cmap='gray')
    try:
        plt.show()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
