import unittest


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def check_location(finish_location, location):
    if finish_location["min"] is None or location < finish_location["min"]:
        finish_location["min"] = location
    if finish_location["max"] is None or location > finish_location["max"]:
        finish_location["max"] = location


def check_node(node, finish_location, location):
    finish_location.setdefault("min", None)
    finish_location.setdefault("max", None)
    if node.left is None or node.right is None:
        check_location(finish_location, location)
    if node.left is not None:
        check_node(node.left, finish_location, location + 1)
    if node.right is not None:
        check_node(node.right, finish_location, location + 1)
    return True if finish_location["max"] - finish_location["min"] <= 1 else False


class TestAppendNode(unittest.TestCase):
    def test1(self):
        """
        1→2→4
          3
        """
        node = Node(1)
        node.left = Node(2)
        node.right = Node(3)
        node.left.left = Node(4)
        assert check_node(node, {}, 0)

    def test2(self):
        """
        1→2→4→5
          3
        """
        node = Node(1)
        node.left = Node(2)
        node.right = Node(3)
        node.left.left = Node(4)
        node.left.left.left = Node(5)
        assert not check_node(node, {}, 0)


if __name__ == '__main__':
    unittest.main()
