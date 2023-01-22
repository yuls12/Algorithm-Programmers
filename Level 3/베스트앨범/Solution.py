def solution(genres, plays):
    answer = []
    g_dic = {}
    play_dic = {}
    for i in range(len(genres)):
        g_dic[genres[i]] = g_dic.get(genres[i],0) + plays[i]
        play_dic[genres[i]] = play_dic.get(genres[i], []) + [(plays[i], i)]
    g_sorted = sorted(g_dic.items(), key = lambda x: x[1], reverse=True)
    
    for (g, p) in g_sorted:
        play_dic[g] = sorted(play_dic[g], key=lambda x : (-x[0] , x[1]))
        answer += [idx for (p, idx) in play_dic[g]][:2]
    
    return answer