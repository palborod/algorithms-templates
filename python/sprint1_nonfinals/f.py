def is_palindrome(line: str) -> bool:
    line = line.replace(',', '')
    line = line.replace('.', '')
    line = line.replace('!', '')
    line = line.replace('?', '')
    line = line.replace(':', '')
    line = line.replace(' ', '')
    print(line)
    if line.lower() == line[::-1].lower():
        print(line)
        print(line[::-1])
        return True
    else:
        print(line)
        print(line[::-1])
        return False

print(is_palindrome(input().strip()))
