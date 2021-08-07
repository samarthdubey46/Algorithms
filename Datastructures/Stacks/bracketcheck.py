from Stacks.listStack import Stack


def getBracketValid(string: str):
    b = ['[', '{', '(']
    r = [']', '}', ')']
    stack = Stack()
    isValid = True
    for j,i in enumerate(string):
        if i in b:
            stack.push(i)
        else:
            if stack.isEmpty():
                isValid = False
                break
            else:
                if stack.peek() != b[r.index(i)]:
                    isValid = False
                    break
                else:
                    stack.pop()
    return isValid and stack.size() == 0


print(getBracketValid('[{()}]'))
