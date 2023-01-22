from itertools import combinations as c

def solution(number):
    return [sum(i) for i in list(c(number,3))].count(0)