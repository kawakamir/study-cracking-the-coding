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


def sum_order(node1, node2):
    pre_sum_node = None
    value_delta = 0
    head = None
    while node1 or node2 or value_delta:
        if node1 and node2:
            check_value = node1.value + node2.value + value_delta
        elif node1:
            check_value = node1.value + value_delta
        elif node2:
            check_value = node2.value + value_delta
        else:
            check_value = value_delta

        sum_node = Node(check_value % 10)
        if not head:
            head = sum_node

        value_delta = check_value // 10

        if pre_sum_node:
            pre_sum_node.next = sum_node

        pre_sum_node = sum_node

        if node1:
            node1 = node1.next
        if node2:
            node2 = node2.next

    return head


def sum_dec_order(node1, node2):
    head1 = node1
    head2 = node2
    # nodeの数を合わせる
    while node1 or node2:
        if node1 is None:
            head_node = Node(0)
            head_node.next = head1
            head1 = head_node
            node2 = node2.next
        elif node2 is None:
            head_node = Node(0)
            head_node.next = head2
            head2 = head_node
            node1 = node1.next
        else:
            node1 = node1.next
            node2 = node2.next

    node1 = head1
    node2 = head2
    pre_sum_node = None
    head_sum_node = None

    while node1:
        sum_value = node1.value + node2.value

        if sum_value // 10 and not pre_sum_node:
            pre_sum_node = Node(1)
            head_sum_node = pre_sum_node

        sum_node = Node(sum_value % 10)
        if not head_sum_node:
            head_sum_node = sum_node

        if pre_sum_node:
            pre_sum_node.value = pre_sum_node.value + sum_value // 10
            pre_sum_node.next = sum_node

        pre_sum_node = sum_node

        node1 = node1.next
        node2 = node2.next

    return head_sum_node


class TestSumOrder(unittest.TestCase):
    def test1(self):
        head1 = Node(1)
        head1.append_to_tail(2)
        head1.append_to_tail(3)
        head2 = Node(1)
        head2.append_to_tail(2)
        head2.append_to_tail(3)
        sum_head = sum_order(head1, head2)
        assert sum_head.to_list() == [2, 4, 6]

        head1 = Node(7)
        head1.append_to_tail(1)
        head1.append_to_tail(6)
        head2 = Node(5)
        head2.append_to_tail(9)
        head2.append_to_tail(2)
        sum_head = sum_order(head1, head2)
        assert sum_head.to_list() == [2, 1, 9]

        head1 = Node(7)
        head1.append_to_tail(1)
        head1.append_to_tail(7)
        head2 = Node(5)
        head2.append_to_tail(9)
        head2.append_to_tail(2)
        sum_head = sum_order(head1, head2)
        assert sum_head.to_list() == [2, 1, 0, 1]

        head1 = Node(7)
        head1.append_to_tail(1)
        head1.append_to_tail(7)
        head2 = Node(5)
        head2.append_to_tail(9)
        sum_head = sum_order(head1, head2)
        assert sum_head.to_list() == [2, 1, 8]


class TestSumDecOrder(unittest.TestCase):
    def test1(self):
        head1 = Node(6)
        head1.append_to_tail(1)
        head1.append_to_tail(7)
        head2 = Node(2)
        head2.append_to_tail(9)
        head2.append_to_tail(5)
        sum_head = sum_dec_order(head1, head2)
        assert sum_head.to_list() == [9, 1, 2]

    def test2(self):
        head1 = Node(6)
        head1.append_to_tail(1)
        head2 = Node(2)
        head2.append_to_tail(9)
        head2.append_to_tail(5)
        sum_head = sum_dec_order(head1, head2)
        assert sum_head.to_list() == [3, 5, 6]


if __name__ == '__main__':
    unittest.main()
