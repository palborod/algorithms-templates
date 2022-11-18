#ID 75139105

def speed_typing(k, matrix):
    t = 0
    score = 0
    while t <= 9:
        count_t = matrix.count(str(t))
        if 0 < count_t <= k * 2:
            score += 1
        t += 1
    return score



def read_input():
    k = int(input())
    matrix = ''
    matrix = ''.join([matrix + input() for i in range(4)])
    return k, matrix


k, matrix = read_input()
print(speed_typing(k, matrix))