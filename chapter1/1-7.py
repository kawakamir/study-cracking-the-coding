sample = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [5, 4, 3, 2, 1],
    [6, 6, 6, 6, 6]
]


def rolling(sample):
    new_matrix = []
    num_lines = len(sample)
    for j, line in enumerate(sample):
        for i in range(num_lines):
            try:
                new_matrix[i].append(line.pop())
            except IndexError:
                new_matrix.append([line.pop()])
    print(new_matrix)


if __name__ == '__main__':
    rolling(sample)
