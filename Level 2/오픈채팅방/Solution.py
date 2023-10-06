def solution(record):
    record = [i.split(' ') for i in record]
    rec = sorted(record.copy(), key=lambda x: x[1])
    id_name = {}
    for i in rec:
        if i[0] == 'Enter' or i[0] =='Change':
            id_name[i[1]] = i[2]
    result = []
    for i in record:
        if i[0] == 'Enter':
            result.append(f"{id_name[i[1]]}님이 들어왔습니다.")
        elif i[0] == 'Leave':
            result.append(f"{id_name[i[1]]}님이 나갔습니다.")
    return result