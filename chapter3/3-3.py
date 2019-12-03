class EmptyStackException(Exception):
    pass


class SetOfStacks(object):
    def __init__(self, limit):
        self.limit = limit
        self.stacks = [self.__create_stack()]
        self.nums = [0]
        self.pop_at_indexes = []

    def __create_stack(self):
        return Stack()

    def __is_exists_index(self, i):
        try:
            self.stacks[i]
        except IndexError:
            return False
        return True

    def push(self, data):
        if self.nums[-1] == self.limit:
            target_stack = self.__create_stack()
            self.stacks.append(target_stack)
        else:
            target_stack = self.stacks[-1]
        target_stack.push(data)

    def pop(self):
        while True:
            try:
                self.stacks[-1].pop()
                break
            except EmptyStackException:
                self.stacks.pop()
                if not self.stacks:
                    raise EmptyStackException

    def popAt(self, i):
        try:
            self.stacks[i].pop()
        except EmptyStackException:
            self.stacks.pop(i)
            raise EmptyStackException


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
