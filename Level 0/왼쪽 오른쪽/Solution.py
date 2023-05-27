def solution(str_list):
    if 'r' in str_list and 'l' in str_list:
        left, right = str_list.index('l'), str_list.index('r')
        if left < right:
            return str_list[:left]
        else:
            return str_list[right+1:]
    elif 'r' in str_list:
        right = str_list.index('r')
        return str_list[right+1:]
    elif 'l' in str_list:
        left = str_list.index('l')
        return str_list[:left]
        
    else:
        return []