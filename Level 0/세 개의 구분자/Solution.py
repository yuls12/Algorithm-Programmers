import re

def solution(myStr):
    answer = []
    for s in re.split('[a-c]', myStr):
        if len(s) > 0 :
            answer.append(s)
    if len(answer) > 0 :
        return answer
    else:
        return ['EMPTY']