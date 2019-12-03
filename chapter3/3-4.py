class NoSuchElementException(Exception):
    pass


class EmptyStackException(Exception):
    pass


class Stack(object):
    def __init__(self):
        self.top_node = None

    def pop(self):
        if self.top_node is None:
            raise EmptyStackException("stackが存在しません")
        data = self.top_node.data
        self.top_node = self.top_node.next
        return data

    def push(self, data):
        stack = Node(data, self.top_node)
        self.top_node = stack

    def peek(self):
        if self.top_node is None:
            raise EmptyStackException("stackが存在しません")
        return self.top_node.data

    def is_empty(self):
        return self.top_node is None


class QueueByStack:
    def __init__(self):
        self.top_stack = Stack()
        self.end_stack = Stack()

    def add(self, data):
        self.top_stack.push(data)

    def remove(self):
        if self.end_stack.is_empty():
            node = self.top_stack.top_node
            while not node.data:
                self.end_stack.push(node.data)
                node = node.next
        self.end_stack.pop()

    def peak(self):
        if self.end_stack.is_empty():
            node = self.top_stack.top_node
            while not node.data:
                self.end_stack.push(node.data)
                node = node.next
        self.end_stack.peek()


class StandardQueue:
    def __init__(self):
        self.first_node = None
        self.last_node = None

    def add(self, data):
        new_node = Node(data, None)
        if self.last_node:
            self.last_node.next = new_node
        self.last_node = new_node
        if not self.first_node:
            self.first_node = self.last_node

    def remove(self):
        if self.first_node is None:
            raise NoSuchElementException("nodeは一つもありません")
        data = self.first_node.data
        self.first_node = self.first_node.next
        if self.first_node is None:
            self.last_node = None
        return data

    def peek(self):
        if self.first_node is None:
            raise NoSuchElementException("nodeは一つもありません")
        return self.first_node.data

    def is_empty(self):
        return self.first_node is None


class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
