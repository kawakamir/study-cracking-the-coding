import unittest


class Node(object):

    def __init__(self, x, y=None, z=None):
        self.value = x
        self.next = y
        self.prev = z

    def append_to_tail(self, value):
        node = self
        while node.next is not None:
            node = node.next
        node.next = Node(value)

    @staticmethod
    def make_nodes(raws):
        head_node = None
        prev_node = None
        if len(raws):
            ValueError("rawsを入れてください。")
        for raw in raws:
            node = Node(raw)
            if not head_node:
                head_node = node
            if prev_node:
                prev_node.next = node
                node.prev = prev_node
            prev_node = node

        last_node = node
        return head_node, last_node

    def to_list(self):  # headの時のみ使用可能
        node_list = []
        node = self
        while node is not None:
            node_list.append(node.value)
            node = node.next
        return node_list


def is_palindrome(head, last):
    proceed_node = head
    fall_back_node = last
    while True:
        if proceed_node.value != fall_back_node.value:
            return False

        if proceed_node.prev == fall_back_node or proceed_node == fall_back_node:
            return True

        proceed_node = proceed_node.next
        fall_back_node = fall_back_node.prev


class TestIsPanlindrome(unittest.TestCase):
    def test1(self):
        head, last = Node.make_nodes([1, 2, 1])
        assert is_palindrome(head, last)

        head, last = Node.make_nodes([1, 2, 2, 1])
        assert is_palindrome(head, last)

        head, last = Node.make_nodes([1, 2, 2, 1, 1])
        assert not is_palindrome(head, last)


if __name__ == '__main__':
    unittest.main()
