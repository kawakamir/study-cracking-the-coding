class EmptyStackException(Exception):
    pass


class Stack(object):
    def __init__(self):
        self.top_stack = None

    def pop(self):
        if self.top_stack is None:
            raise EmptyStackException("stackが存在しません")
        data = self.top_stack.data
        self.top_stack = self.top_stack.next
        return data

    def push(self, data):
        stack = StackNode(data, self.top_stack)
        self.top_stack = stack

    def peek(self):
        if self.top_stack is None:
            raise EmptyStackException("stackが存在しません")
        return self.top_stack.data

    def is_empty(self):
        return self.top_stack is None


class StackNode(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next
