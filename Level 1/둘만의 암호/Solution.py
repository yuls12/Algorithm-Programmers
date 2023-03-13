def solution(s, skip, index):
    answer = ""
    
    alpha = "abcdefghijklmnopqrstuvwxyz" 
    
    for skip_word in skip: 
        if skip_word in alpha:
            alpha = alpha.replace(skip_word, "") 
    
    for i in s:
        change = alpha[(alpha.index(i) + index) % len(alpha)]
        answer += change
    
    return answer