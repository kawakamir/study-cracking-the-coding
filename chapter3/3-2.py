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
        if self.top_stack is None:
            stack = StackNode(data, self.top_stack, data)
        else:
            min_data = data if data < self.top_stack.min_data else self.top_stack.min_data
            stack = StackNode(data, self.top_stack, min_data)
        self.top_stack = stack

    def min(self):
        if self.top_stack is None:
            raise EmptyStackException("stackが存在しません")
        return self.top_stack.min_data

    def peek(self):
        if self.top_stack is None:
            raise EmptyStackException("stackが存在しません")
        return self.top_stack.data

    def is_empty(self):
        return self.top_stack is None


class StackNode(object):
    def __init__(self, data, next, min_data):
        self.data = data
        self.next = next
        self.min_data = min_data
