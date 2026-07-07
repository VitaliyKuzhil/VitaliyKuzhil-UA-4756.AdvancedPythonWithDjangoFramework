
operations = {
    '*': 2,
    '/': 2,
    '%': 2,
    '+': 1,
    '-': 1
}


def toPostFixExpression(e):
    result, stack = [], []

    for i in e:
        if i.isdigit():
            result.append(i)
        else:
            if i == '(':
                stack.append(i)
            elif i == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()
            else:
                while stack and stack[-1] != '(' and operations[stack[-1]] >= operations[i]:
                    result.append(stack.pop())
                stack.append(i)
    
    while stack:
        result.append(stack.pop())

    return result



# expression = ['2', '+', '3']

expression = ['20','+', '3', '*', '(', '5', '*', '4', ')']


print(toPostFixExpression(expression))