from get_rolling_window import rolling_window
import numpy as np


def test_main():
    expected = np.array([
        [1, 2, 3],
        [3, 4, 5],
        [5, 6, 7],
    ])

    # 1, 2, 3, 4, 5, 6, 7

    assert np.array_equal(
        rolling_window(np.arange(1, 8), 3, 2),
        expected
    )

    assert np.array_equal(
        rolling_window(np.arange(1, 9), 3, 2, 1),
        expected
    )

    assert np.array_equal(
        rolling_window(np.arange(1, 9), 3, 1, 2),
        np.array([
            [1, 3, 5],
            [2, 4, 6],
            [3, 5, 7],
            [4, 6, 8]
        ])
    )

    assert np.array_equal(
        rolling_window(np.arange(1, 9), 3, 2, 2),
        np.array([
            [1, 3, 5],
            [3, 5, 7]
        ])
    )


def float_array(start, before) -> np.ndarray:
    return np.array([
        float(i)
        for i in range(start, before)
    ])


def test_float():
    expected = np.array([
        [1., 2., 3.],
        [3., 4., 5.],
        [5., 6., 7.],
    ])

    assert np.array_equal(
        rolling_window(float_array(1, 8), 3, 2),
        expected
    )

    assert np.array_equal(
        rolling_window(float_array(1, 9), 3, 2),
        expected
    )


def test_bool():
    result = rolling_window(
        np.array([True, False, True, True, False, False]), 3, 2)

    assert np.array_equal(
        result,
        np.array([
            [True, False, True],
            [True, True, False]
        ])
    )
