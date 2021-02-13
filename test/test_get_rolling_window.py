from get_rolling_window import rolling_window
import numpy as np


def test_main():
    array = np.arange(1, 8)

    result = rolling_window(array, 3, 2)

    assert np.array_equal(
        result,
        np.array([
            [1, 2, 3],
            [3, 4, 5],
            [5, 6, 7],
        ])
    )
