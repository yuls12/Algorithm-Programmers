from collections import deque

def solution(people, limit):
    cnt = 0
    people.sort()

    # 보트는 2명씩만 탈 수 있고 무게 제한이 있음
    q = deque(people)
    while q:
        if len(q) >= 2:
            if q[0] + q[-1] <= limit:
                q.pop()
                q.popleft()
                cnt += 1
            elif q[0] + q[-1] > limit:
                q.pop()
                cnt += 1
        else:
            if q[0] <= limit:
                q.pop()
                cnt += 1
    return cnt