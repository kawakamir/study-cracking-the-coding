import unittest


def create_minimal_bst(target_list, start, end):
    if end < start:
        return None
    mid = int((start + end) / 2)
    node = Node(target_list[mid])
    node.left = create_minimal_bst(target_list, start, mid - 1)
    node.right = create_minimal_bst(target_list, mid + 1, end)
    return node


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Test(unittest.TestCase):
    def test1(self):
        target_list = [1, 2, 3, 4]
        node = create_minimal_bst(target_list, 0, len(target_list) - 1)
        assert node.data == 2
        assert node.left.data == 1
        assert node.right.data == 3
        assert node.right.right.data == 4


if __name__ == '__main__':
    unittest.main()
