#ID 75292572

def speed_typing(k, matrix):
    t = 1
    score = 0
    for t in '123456789':
        count_t = matrix.count(t) 
        if 0 < count_t <= k * 2:
            score += 1
    return score



def read_input():
    k = int(input())
    matrix = ''
    matrix = ''.join([matrix + input() for i in range(4)])
    return k, matrix


if __name__ == '__main__':
    k, matrix = read_input()
    print(speed_typing(k, matrix))