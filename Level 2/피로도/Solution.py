from itertools import permutations

def clear_dungeoun(k, dungeons):
    result = 0
    for dungeon in dungeons:
        need, consum = dungeon
        if k < need:
            return result
        k -= consum
        result += 1
    return result


def solution(k, dungeons):
    case = permutations(dungeons, len(dungeons))
    answers = []
    for s in case:
        answers.append(clear_dungeoun(k, s))

    return max(answers)