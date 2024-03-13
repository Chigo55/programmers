def solution(array):
    from collections import Counter

    cnt = dict(Counter(array))
    cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
    print(cnt)

    if len(cnt) < 2: 
        return cnt[0][0]
    elif cnt[0][1] == cnt[1][1]: 
        return -1
    else: 
        return cnt[0][0]