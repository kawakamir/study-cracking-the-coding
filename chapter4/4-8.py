class Node(object):
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None


def get_same_parent(nodeA, nodeB):
    target = nodeA
    while True:
        get_same_parent_per_node(target, nodeB)
        target = nodeA.parent


def get_same_parent_per_node(target_parent, serch_node):
    if serch_node == target_parent:
        return serch_node
    return get_same_parent_per_node(target_parent, serch_node.parent)
