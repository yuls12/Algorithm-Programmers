def solution(elements):
    answer = 0
    l = set()

    n = len(elements)

    add = [0 for i in range(n)]

    for i in range(n):
        add = [add[j] + elements[(i+j)%n] for j in range(n)]

        for a in add:
            l.add(a)

    return len(l)