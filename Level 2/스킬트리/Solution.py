def solution(skill, skill_trees):
    result = 0
    for skills in skill_trees:
        match = []
        for s in skills:
            if s in skill:
                match.append(s)
        for i in range(len(match)):
            if match[i] != skill[i]:
                break
        else :
            result += 1
    return result