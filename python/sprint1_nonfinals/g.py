def to_binary(number: int) -> str:
    binar = ''
    if number == 0:
        return '0'
    while number != 0:
        if number % 2 == 0:
            binar += '0'
            number = number // 2
        if number % 2 > 0:
            binar += '1'
            number = number // 2
    return(binar[::-1])

def read_input() -> int:
    return int(input().strip())

print(to_binary(read_input()))
