class Node(object):
    def __init__(self, data):
        self.data = data
        self.parents = []
        self.children = []


def make_project(projects, depends):
    nodes = {}
    for project in projects:
        nodes.update({project: Node(project)})

    for depend in depends:
        parent_data = depend[1]
        children_data = depend[0]
        validate_append_children_data(children_data, nodes[parent_data])
        nodes[parent_data].children.append(nodes[children_data])
        nodes[children_data].parents.append(nodes[parent_data])

    node_set = {}
    for node in nodes.values():
        if not node.children:
            target_dict, node_set = add_node(node, 0, {}, node_set)
            sorted_value = sorted(target_dict.items(), reverse=True, key=lambda x: x[0])
            for value in sorted_value:
                yield value[1]


def add_node(node, level, target_dict, node_set):
    target_dict.setdefault(level, [])
    if not node in node_set:
        target_dict[level].append(node)
        node_set.add(node)
    if not node.parents:
        return target_dict, node_set
    for children in node.children:
        return add_node(children, level + 1, target_dict,node_set)


def validate_append_children_data(data, node):
    if not node.parents:
        return
    for parent in node.parents:
        if parent.data == data:
            ValueError("エラー")
        return validate_append_children_data(data, parent)
