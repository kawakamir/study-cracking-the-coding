import copy
import unittest


class Node(object):
    def __init__(self, x, y=None):
        self.value = x
        self.next = y

    def append_to_tail(self, value):
        node = self
        while node.next is not None:
            node = node.next
        node.next = Node(value)

    def to_list(self):  # headの時のみ使用可能
        node_list = []
        node = self
        while node is not None:
            node_list.append(node.value)
            node = node.next
        return node_list


def connect_under_specify_num(head, pre_node, node, num):
    if node is None:
        return head
    if node.value >= num:
        if node.next is None:
            node = None
            if pre_node:
                pre_node.next = node
        else:
            node.value = node.next.value
            node.next = node.next.next
        return connect_under_specify_num(head, pre_node, node, num)
    if head is None:
        head = node
    return connect_under_specify_num(head, node, node.next, num)


def connect_over_specify_num(head, pre_node, node, num):
    if node is None:
        return head
    if node.value < num:
        if node.next is None:
            node = None
            if pre_node:
                pre_node.next = None
        else:
            node.value = node.next.value
            node.next = node.next.next
        return connect_over_specify_num(head, pre_node, node, num)

    if head is None:
        head = node
    return connect_over_specify_num(head, node, node.next, num)


def separated_by_num(head, num):
    under_head_node = connect_under_specify_num(None, None, copy.deepcopy(head), num)
    over_head_node = connect_over_specify_num(None, None, copy.deepcopy(head), num)

    node = under_head_node

    if under_head_node is None:
        return over_head_node

    while node is not over_head_node:
        if node.next is None:
            node.next = over_head_node
        node = node.next

    return under_head_node


class TestSeparateByNum(unittest.TestCase):
    def test1(self):
        head = Node(1)
        head.append_to_tail(2)
        head.append_to_tail(3)
        separated_list = separated_by_num(head, 2).to_list()
        assert separated_list == [1, 2, 3]

    def test2(self):
        head = Node(1)
        head.append_to_tail(2)
        head.append_to_tail(3)
        separated_list = separated_by_num(head, 1).to_list()
        assert separated_list == [1, 2, 3]

    def test3(self):
        head = Node(1)
        head.append_to_tail(2)
        head.append_to_tail(3)
        separated_list = separated_by_num(head, 3).to_list()
        assert separated_list == [1, 2, 3]


def separated_by_num_v2(head, num):
    under_head = None
    under_last_node = None
    over_head = None
    over_last_node = None
    node = head
    while node:
        if node.value < num:
            if not under_head:
                under_head = node
            if under_last_node:
                under_last_node.next = node
            under_last_node = node
        else:
            if not over_head:
                over_head = node
            if over_last_node:
                over_last_node.next = node
            over_last_node = node
        node = node.next

    if under_last_node:
        under_last_node.next = over_head
    if not under_head:
        under_head = over_head

    return under_head


class TestSeparateByNumV2(unittest.TestCase):
    def test1(self):
        head = Node(1)
        head.append_to_tail(2)
        head.append_to_tail(3)
        separated_list = separated_by_num_v2(head, 2).to_list()
        assert separated_list == [1, 2, 3]

    def test2(self):
        head = Node(1)
        head.append_to_tail(2)
        head.append_to_tail(3)
        separated_list = separated_by_num_v2(head, 1).to_list()
        assert separated_list == [1, 2, 3]

    def test3(self):
        head = Node(1)
        head.append_to_tail(2)
        head.append_to_tail(3)
        separated_list = separated_by_num_v2(head, 3).to_list()
        assert separated_list == [1, 2, 3]


if __name__ == '__main__':
    unittest.main()
