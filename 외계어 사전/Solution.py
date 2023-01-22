from itertools import permutations as p

def solution(spell, dic):
    word = [''.join(i) for i in list(p(spell, len(spell)))]
    if len(set(dic) & set(word)) == 0:
        return 2
    else :
        return 1