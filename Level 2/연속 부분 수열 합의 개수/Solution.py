def solution(elements):
    r = 1
    answer = []
    while r <= len(elements):
        elem = elements + elements[0:r]
        for i in range(0,len(elem)-r):
            answer.append(sum(elem[i:i+r]))
        r += 1
        print(elem, answer)
    return len(set(answer))