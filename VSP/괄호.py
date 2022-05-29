def isValid(input):
    kind = {'(': 0, '[': 0, '{': 0}
    for i in input:
        if i in kind:
            kind[i] += 1
        else:
            if i == ')':
                if kind['('] == 0:
                    return False
                kind['('] -= 1
            elif i == ']':
                if kind['['] == 0:
                    return False
                kind['['] -= 1
            elif i == '}':
                if kind['{'] == 0:
                    return False
                kind['{'] -= 1
    if sum(kind.values()) > 0:
        return False
    return True


print("input: ()")
print("output:",isValid("()"))  # True
print("input: ()[]{}")
print("output: ",isValid("()[]{}"))  # True
print("input: (]")
print("output: ",isValid("(]"))  # False

print(isValid("((()))"))  # True
print(isValid("((())"))  # False

print(isValid("([)]"))  # True
