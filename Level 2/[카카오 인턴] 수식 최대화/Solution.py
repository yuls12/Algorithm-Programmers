from itertools import permutations


def solution(expression):
    operators = ["*", "+", "-"]
    answer = []
    for oper in permutations(operators, 3):
        a = oper[0]
        b = oper[1]
        tmp_list = []
        for i in expression.split(a):
            tmp = [f"({j})" for j in i.split(b)]
            tmp_list.append(f"({b.join(tmp)})")
            # print(tmp_list)
        answer.append(abs(eval(a.join(tmp_list))))
        # print(answer)
        
    return max(answer)