from itertools import permutations

def solution(babbling):
    answer = 0
    word = ["aya","ye","woo","ma"]
    new_word = []
    
    for i in range(1, len(speek)+1):
        for k in permutations(word, i):
            new_word.append(''.join(k))

    for i in babbling:
        if i in new_word:
            answer += 1

    return answer