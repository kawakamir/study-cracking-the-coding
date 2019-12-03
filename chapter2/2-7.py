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

def out_common_nodes(node1, node2):
    head_node1 = node1
    head_node2 = node2
    last_node1 = None
    last_node2 = None
    count1 = 0
    count2 = 0
    while node1 or node2:
        if node1:
            last_node1 = node1
            node1 = node1.next
            count1 += 1
        if node2:
            last_node2 = node2
            node2 = node2.next
            count2 += 1
    if last_node1 != last_node2:
        return False

    long_node = head_node1 if count1 > count2 else head_node2
    short_node = head_node2 if count1 > count2 else head_node1
    long_count = count1 if count1 > count2 else count2
    short_count = count2 if count1 > count2 else count1

    common_nodes = []
    while long_node:
        if long_count > short_count:
            long_count -= 1
            long_node = long_node.next
            continue

        if long_node == short_count:
            common_nodes.append(long_node)

        long_node = long_node.next
        short_count = short_node.next

    return common_nodes


