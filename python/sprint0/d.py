from typing import List, Tuple, Optional

def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    # Здесь реализация вашего решения
    for i in range(len(arr)):
        s1 = arr[i]
        for j in range(i+1, len(arr)):
            s2 = arr[j]
            if s1 + s2 == target_sum:
                return s1, s2
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
