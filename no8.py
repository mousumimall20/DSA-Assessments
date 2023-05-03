def reverse_string_using_stack(s):
    stack = []
    # push all characters onto the stack
    for c in s:
        stack.append(c)

    # pop characters off the stack to get the reversed string
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()

    return reversed_string
