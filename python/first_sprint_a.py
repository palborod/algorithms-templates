#ID 75292796

from typing import List


def result(house_num):
    x = len(house_num)
    answ = [0] * x
    last_null = -x
    for i in range(len(house_num)):
        if house_num[i] != 0:
            answ[i] = i - last_null
        else:
            last_null = i
    last_null = 2 * x
    for i in reversed(range(len(house_num))):
        if house_num[i] != 0:
            answ[i] = min(last_null - i, answ[i])
        else:
            last_null = i
    return answ

def read_input() -> List[int]:
    n = int(input())
    house_num = list(map(int, input().strip().split()))
    return house_num


if __name__ == '__main__':
    house_num = read_input()
    print(*result(house_num))