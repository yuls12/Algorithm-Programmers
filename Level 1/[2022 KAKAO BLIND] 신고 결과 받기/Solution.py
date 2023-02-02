from collections import defaultdict


def solution(id_list, report, k):
    answer = list()
    count = defaultdict(int)   # 몇번 신고했는지
    user = defaultdict(set)  # 신고 리스트
    # 누가 누구를 신고했는지, 산고당한 횟수 세기
    for r in report:
        a, b = r.split()  # 누가 누구를 신고했는지 나누기
        if b not in user[a]:   # 같은 사람이 1번 이상 신고 x
            user[a].add(b)
            count[b] += 1  # 신고당한 수
            
    # 자신이 신고한 사람이 k번 이상이면 처리된 횟수 + 1
    for id in id_list:
        result = 0
        for u in user[id]:
            if count[u] >= k:
                result += 1
        answer.append(result)
    return answer