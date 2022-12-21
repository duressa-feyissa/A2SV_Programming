def swap_case(s):
    new = ""
    for i in s:
        if ord(i) >= 65 and ord(i) < 91:
            new += chr(ord(i) + 32)
        elif ord(i) >= 97 and ord(i) < 123:
            new += chr(ord(i) - 32)
        else:
            new += i
    return new

if __name__ == '__main__':
