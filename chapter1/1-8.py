sample = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 0, 1],
    [5, 4, 3, 2, 1],
]


def set_to_zero(sample):
    row_with_zero = {}
    column_with_zero = {}
    for i, line in enumerate(sample):
        for j, word in enumerate(line):
            if word == 0:
                row_with_zero[i] = True
                column_with_zero[j] = True

    for i, line in enumerate(sample):
        for j, _ in enumerate(line):
            if row_with_zero.get(i) or column_with_zero.get(j):
                sample[i][j] = 0

    print(sample)


if __name__ == '__main__':
    set_to_zero(sample)
