def isValid(s):
    opener = ['(', '[', '{']
    stack = []

    for i in range(len(s)):
        if s[i] in opener:
            stack.append(s[i])
        else:
            if s[i] == ')' and len(stack) != 0 and stack[-1] == '(':
                stack.pop(-1)
            elif s[i] == ']' and len(stack) != 0 and stack[-1] == '[':
                stack.pop(-1)
            elif s[i] == '}' and len(stack) != 0 and stack[-1] == '{':
                stack.pop(-1)
            else:
                return False

    return len(stack) == 0


print(isValid("([}}])"))
