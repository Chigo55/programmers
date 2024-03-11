def solution(s):
    ans = []
    dic = {}
    for idx, string in enumerate(s):
        if string not in dic:
            ans.append(-1)
            dic[string] = idx
        else:
            ans.append(idx - dic[string])
            dic[string] = idx
    
    return ans