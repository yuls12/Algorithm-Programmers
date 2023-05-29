def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == '(':
            stack.append('(')
        elif stack:
            stack.pop()
        else:
            return False
    if len(stack) == 0:
        return True
    else:
        return False
