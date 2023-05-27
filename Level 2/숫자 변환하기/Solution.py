def solution(x, y, n):
    answer = 0
    s = set()
    s.add(x)

    while s:
        if y in s:
            return answer
        else:
            x = set()
            for i in s:
                if i+n <= y:
                    x.add(i+n)
                if i*2 <= y:
                    x.add(i*2)
                if i*3 <= y:
                    x.add(i*3)
            s = x
            answer += 1

    return -1
