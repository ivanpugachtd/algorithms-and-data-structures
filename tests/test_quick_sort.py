import pytest
from src.sorting.quick_sort import quick_sort
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


@pytest.mark.parametrize(
    "input_arr, expected",
    [
        ([1, 2, 5, 4, 3], [1, 2, 3, 4, 5]),
        ([1, 2, 5, 4, 3, 8, 6, 7, 10, 0, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12]),
        ([], []),
        ([3, 3, 3, 3], [3, 3, 3, 3]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1], [1]),
        (["banana", "apple", "cherry"], ["apple", "banana", "cherry"]),
    ],
)
def test_quick_sort(input_arr, expected):
    quick_sort(input_arr)
    assert input_arr == expected
