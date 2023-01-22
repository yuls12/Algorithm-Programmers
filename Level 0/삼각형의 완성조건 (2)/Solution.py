def solution(sides):
    sides.sort()
    a, b = sides[0], sides[1]
    x = len(range(b - (a - 1), b + 1))
    y = len(range(b + 1, a + b))
    return x + y