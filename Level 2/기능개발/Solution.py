import math as m


def solution(progresses, speeds):
    publish = []
    day = [m.ceil((100 - x) / y) for x, y in zip(progresses, speeds)]

    while len(day) > 0:
        cnt = 1
        check = day.pop(0)
        day_check = day.copy()

        for i in range(len(day)):
            if check >= day[i]:
                cnt += 1
                day_check.pop(0)
            else:
                break
        publish.append(cnt)

        day = day_check.copy()

    return publish
