import unittest


class GraphNode:
    def __init__(self, name, children):
        self.name = name
        self.children = children


def is_target_node(search_node, target_node):
    if search_node is None:
        return False
    if search_node is target_node:
        return True
    for child_node in search_node.children:
        return is_target_node(child_node, target_node)


def is_connected_nodes(node1, node2):
    if is_target_node(node1, node2) or is_target_node(node2, node1):
        return True
    return False


class TestIsConnected(unittest.TestCase):
    def test1(self):
        """
        A - C - D
        B -
        """
        D = GraphNode("D", [None])
        C = GraphNode("C", [D])
        B = GraphNode("B", [C])
        A = GraphNode("A", [C])
        assert is_connected_nodes(A, D) is True
        assert is_connected_nodes(A, B) is False


if __name__ == '__main__':
    unittest.main()
