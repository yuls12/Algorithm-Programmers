def solution(N, stages):
    answer = {}
    people = len(stages)
    
    for stage in range(1, N+1):
        if people != 0:
            cnt = stages.count(stage)
            answer[stage] = cnt/people
            people -= cnt
        else :
            answer[stage] = 0
    
    return sorted(answer, key=lambda x : answer[x], reverse=True )