from typing import List, Tuple, Optional

def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    first = 0
    last = len(arr) - 1
    while first < last:
        summ = arr[first] + arr[last]
        if summ == target_sum:
            return arr[first], arr[last]
        if summ < target_sum:
            first += 1
        else:
            last -= 1
    return None
    pass

def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    target_sum = int(input())
    return arr, target_sum

def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))

arr, target_sum = read_input()
print_result(two_sum(arr, target_sum))
