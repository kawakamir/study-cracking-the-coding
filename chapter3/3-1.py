from chapter3.stack import Stack, StackNode


def create_stack(nums):
    separate_num = 3

    stacks = [Stack for _ in range(separate_num)]
    for i, num in enumerate(nums):
        stacks[i % separate_num].push(num)

    return stacks
