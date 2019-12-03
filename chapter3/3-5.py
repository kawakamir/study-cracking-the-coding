class EmptyStackException(Exception):
    pass


class Stack(object):
    def __init__(self):
        self.top_node = None

    def sort(self):
        new_stack = Stack()
        node = self.top_node
        while node:
            self._sort_push(new_stack, node)
        return new_stack

    def pop(self):
        if self.top_node is None:
            raise EmptyStackException("stackが存在しません")
        data = self.top_node.data
        self.top_node = self.top_node.next
        return data

    def push(self, data):
        stack = StackNode(data, self.top_node)
        self.top_node = stack

    def peek(self):
        if self.top_node is None:
            raise EmptyStackException("stackが存在しません")
        return self.top_node.data

    def is_empty(self):
        return self.top_node is None

    def _sort_push(self, new_stack, data):
        node = new_stack.top_node
        if not node:
            new_stack.top_node = StackNode(data, None)
            return

        if data <= node.data:
            self.top_node = StackNode(data, node)
            return

        while node.next:
            if data <= node.next.data:
                new_node = StackNode(data, node.next)
                node.next = new_node
                return
            else:
                continue
        node.next = StackNode(data, None)


class StackNode(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next
