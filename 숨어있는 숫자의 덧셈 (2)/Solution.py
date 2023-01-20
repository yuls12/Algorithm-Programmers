import re
def solution(my_string):
    answer = re.findall(r'\d+', my_string)
    result = [int(i) for i in answer]
    return sum(result)