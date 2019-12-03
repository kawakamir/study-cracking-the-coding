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


def delete_duplication(head):
    values_dict = {}
    node = head
    pre_node = None
    while node is not None:
        if values_dict.get(node.value) is not None:
            pre_node.next = node.next
        else:
            pre_node = node
        values_dict[node.value] = True
        node = node.next


def delete_duplication_each(node, pre_comparison_node, comparison_node):
    if comparison_node is None:
        return
    if node.value == comparison_node.value:
        pre_comparison_node.next = comparison_node.next
        return delete_duplication_each(node, pre_comparison_node, comparison_node.next)
    return delete_duplication_each(node, comparison_node, comparison_node.next)


def delete_duplication_no_buffer(head):
    while head is not None:
        delete_duplication_each(head, head, head.next)
        head = head.next


head1 = Node(1)
head1.append_to_tail(1)

head2 = Node(1)
head2.append_to_tail(2)
head2.append_to_tail(2)

head3 = Node(1)
head3.append_to_tail(2)
head3.append_to_tail(1)

if __name__ == '__main__':
    # delete_duplication(head1)
    # delete_duplication(head2)
    # delete_duplication(head3)

    delete_duplication_no_buffer(head1)
    delete_duplication_no_buffer(head2)
    delete_duplication_no_buffer(head3)

    assert head1.to_list() == [1]
    assert head2.to_list() == [1, 2]
    assert head3.to_list() == [1, 2]
