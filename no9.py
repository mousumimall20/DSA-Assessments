def evaluate_postfix_expression(postfix):
    stack = []
    # iterate over the postfix expression
    for element in postfix:
        # if the element is an operand, push it onto the stack
        if element.isdigit():
            stack.append(int(element))
        else:
            # if the element is an operator, pop the top two elements from the stack
            operand2 = stack.pop()
            operand1 = stack.pop()

            # perform the operation and push the result back onto the stack
            if element == '+':
                result = operand1 + operand2
            elif element == '-':
                result = operand1 - operand2
            elif element == '*':
                result = operand1 * operand2
            elif element == '/':
                result = operand1 / operand2
            else:
                raise ValueError("Invalid operator: " + element)

            stack.append(result)

    # the final result will be the only element left on the stack
    return stack.pop()
