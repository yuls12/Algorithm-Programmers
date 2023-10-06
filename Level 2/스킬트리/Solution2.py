import re
def solution(skill, skill_trees):
    skill_hap = [skill[:i+1] for i in range(len(skill)) ]
    tree = [re.sub(f'[^{skill}]', '', i) for i in skill_trees]
    cnt = 0
    for i in tree:
        if i in skill_hap or i == '':
            cnt += 1 
    return cnt