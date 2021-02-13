[![](https://travis-ci.org/kaelzhang/python-get-rolling-window.svg?branch=master)](https://travis-ci.org/kaelzhang/python-get-rolling-window)
[![](https://codecov.io/gh/kaelzhang/python-get-rolling-window/branch/master/graph/badge.svg)](https://codecov.io/gh/kaelzhang/python-get-rolling-window)
[![](https://img.shields.io/pypi/v/get-rolling-window.svg)](https://pypi.org/project/get-rolling-window/)
[![](https://img.shields.io/pypi/l/get-rolling-window.svg)](https://github.com/kaelzhang/python-get-rolling-window)

# get-rolling-window

Create a rolling window from a 1-D numpy ndarray

## Install

```sh
$ pip install get-rolling-window
```

## Usage

```py
import numpy as np
from get_rolling_window import rolling_window

array = np.arange(1, 8)

rolling_window(array, 3, 2)
# array([[1, 2, 3],
#        [3, 4, 5],
#        [5, 6, 7]])
```

## rolling_window(array, size, shift, stride) -> np.ndarray

Gets an `size`-period rolling window for `array` as an numpy 1-D array

```
|-------- size:3 --------|
|- stride:1 -|           |
|            |           |
1            2           3 --------|---
                                shift:2
3            4           5 --------|---

5            6           7
```

- **array** `np.ndarray` The 1-D numpy array. If the given array has more than one dimensions, it will be treated as a 1-D array.
- **size** `int` The size of the window.
- **shift?** `int=None` The `shift` argument determines the number of input elements by which the window moves on each iteration. Defaults to no shift.
- **stride?** `int=1` Determines the stride of the input elements. Defaults to `1`.

Returns `np.ndarray`

## License

[MIT](LICENSE)
