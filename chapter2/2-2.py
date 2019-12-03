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




def take_item_from_end(head, num):
    values = []
    node = head
    while node is not None:
        values.append(node.value)
        node = node.next
    return values[-num]
