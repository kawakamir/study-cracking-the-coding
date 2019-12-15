import unittest

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def append_node(node, connect_dict, count):
    connect_dict.setdefault(count, [])
    connect_dict[count].append(node.data)
    if node.left is not None:
        append_node(node.left, connect_dict, count + 1)
    if node.right is not None:
        append_node(node.right, connect_dict, count + 1)
    return connect_dict

class TestAppendNode(unittest.TestCase):
    def test1(self):
        """
        1
        2, 3
        4, 5, 6, 7
        """
        node = Node(1)
        node.left = Node(2)
        node.right = Node(3)
        node.left.left = Node(4)
        node.left.right = Node(5)
        node.right.left = Node(6)
        node.right.right = Node(7)
        connect_dict = append_node(node, {}, 0)
        assert [1] == connect_dict[0]
        assert [2, 3] == connect_dict[1]
        assert [4, 5, 6, 7] == connect_dict[2]

if __name__ == '__main__':
    unittest.main()
