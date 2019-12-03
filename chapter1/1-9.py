





def is_substring(str1, str2):
    return str1 in str2


def is_rotation(str1, str2):
    if len(str1) != len(str2):
        return False
    return is_substring(str1, str2 + str2)
