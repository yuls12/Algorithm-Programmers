def solution(today, terms, privacies):
    answer = []
    term = {}
    today = list(map(int, today.split('.')))
    todays = today[0] * 12 * 28 + today[1] * 28 + today[2]
    
    for t in terms:
        term[t[0]] = int(t[2:]) * 28
    
    for i, p in enumerate(privacies):
        y, m, d = p.split('.')
        d, t = d.split()
        p = int(y) * 12 * 28 + int(m) * 28 + int(d)
        if p + term[t] <= todays:
            answer.append(i+1)
    return answer