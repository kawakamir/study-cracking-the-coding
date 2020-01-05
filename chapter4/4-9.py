class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_list(node, level, target):
    target[level].append(node.data)
    if node.left is not None:
        create_list(node.left, level + 1, target)
    if node.right is not None:
        create_list(node.right, level + 1, target)
    return target


def create_candidate_list(separeted_dict, level, target_list):
    try:
        separeted_dict[level]
    except KeyError:
        yield target_list
        return
    separeted_list = separeted_dict[level]
    for each_list in permutationGeneratorRecursive(separeted_list, len(separeted_list)):
        yield from create_candidate_list(separeted_dict, level + 1, target_list + each_list)


def permutationGeneratorRecursive(data, r):
    if r <= 0 or r > len(data):
        return []

    return _permutationGeneratorRecursive(data, r, [])


def _permutationGeneratorRecursive(data, r, progress):
    if r == 0:
        yield progress
        return

    for i in range(len(data)):
        yield from _permutationGeneratorRecursive(listExcludedIndices(data, [i]), r - 1, progress + [data[i]])


def listExcludedIndices(data, indices):
    return [x for i, x in enumerate(data) if i not in indices]
