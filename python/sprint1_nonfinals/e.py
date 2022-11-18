def get_longest_word(line: str) -> str:
    wordList = line.split(" ")
    word = wordList[0]
    for i in range(1, len(wordList)):
        if len(wordList[i]) > len(word):
            word = wordList[i]
    return word

def read_input() -> str:
    _ = input()
    line = input().strip()
    return line

def print_result(result: str) -> None:
    print(result)
    print(len(result))

print_result(get_longest_word(read_input()))
