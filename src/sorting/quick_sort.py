from typing import List, TypeVar, Protocol


class Compareble(Protocol):
    def __lt__(self, other: "Compareble") -> bool: ...
    def __le__(self, other: "Compareble") -> bool: ...

T = TypeVar("T", bound=Compareble)


def quick_sort(arr: List[T], left: int = 0, right: int | None = None) -> None:
    if right is None:
        right = len(arr) - 1

    if left < right:
        pivot_index = partition(arr, left, right)
        quick_sort(arr, left, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, right)


def partition(arr: List[T], left: int, right: int) -> int:
    pivot = arr[right]
    i: int = left - 1

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1
