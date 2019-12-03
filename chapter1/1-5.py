import sys


def is_can_change_at_once(stringA, stringB):
    lengthA = len(stringA)
    lengthB = len(stringB)

    error_num = 0

    if abs(lengthB - lengthA) >= 2:
        return False
    if lengthA == lengthB:
        for a, b in zip(stringA, stringB):
            if a != b:
                error_num += 1
                if error_num > 1:
                    return False

    else:
        longer_string = stringA if lengthA > lengthB else stringB
        shorter_string = stringA if lengthA < lengthB else stringB

        check_location = 0
        error_num = 0
        for i, part in enumerate(longer_string, 1):
            if i == len(longer_string) or part != shorter_string[check_location]:
                error_num += 1
                if error_num > 1:
                    return False
                continue
            check_location += 1
    return True


if __name__ == '__main__':
    stringA = sys.argv[1]
    stringB = sys.argv[2]
    print(is_can_change_at_once(stringA, stringB))
