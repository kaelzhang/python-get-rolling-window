from typing import (
    Optional
)

import numpy as np


__version__ = '1.0.0'


def rolling_window(
    array: np.ndarray,
    size: int,
    shift: Optional[int] = None,
    stride: int = 1
) -> np.ndarray:
    """Gets an array of `size`-period rolling windows from `array` as an numpy 1-D array

    Graph::

        |-------- size:3 --------|
        |- stride:1 -|           |
        |            |           |
        1            2           3 --------|---
                                        shift:2
        3            4           5 --------|---

        5            6           7

    Args:
        array (np.ndarray): The 1-D numpy array. If the given array has more than one dimensions, it will be treated as a 1-D array.
        size (int): The size of the window.
        shift (:obj:`int`, optional): The `shift` argument determines the number of input elements by which the window moves on each iteration. Defaults to the size of window.
        stride (:obj:`int`, optional): Determines the stride of the input elements. Defaults to `1`.

    Returns:
        np.ndarray
    """

    shift = shift or size

    first_length = 1 + stride * (size - 1)

    length = len(array)
    step_length = length - first_length
    steps = step_length // shift
    rest = step_length - shift * steps

    steps += 1

    if rest:
        # drop the last window
        # if its size is smaller than `size`.
        array = array[:-rest]

    item_stride = array.strides[0]

    ret = np.lib.stride_tricks.as_strided(
        array,
        # rolling_window "destroy" the first dimension of input `array`,
        shape=(steps, size) + array.shape[1:],
        strides=(item_stride * shift, item_stride * stride) + array.strides[1:]
    )

    return ret
