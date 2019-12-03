import sys


def is_palindrome(target: str):
    strings_dict = dict()
    len = 0
    for i in target:
        if i == " ":
            continue
        i = i.lower()
        strings_dict.setdefault(i, 0)
        strings_dict[i] += 1
        len += 1

    odd_num = 0
    if len % 2 == 1:
        for value in strings_dict.values():
            if value % 2 == 1:
                odd_num += 1
                if odd_num > 1:
                    return False

    else:
        for value in strings_dict.values():
            if value % 2 == 1:
                return False

    return True


if __name__ == '__main__':
    target = sys.argv[1]
    print(is_palindrome(target))
