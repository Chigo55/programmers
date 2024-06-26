def solution(survey, choices):
    ans = ''
    dic = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}

    for s, c in zip(survey, choices):
        if c > 4 : dic[s[1]] += c-4
        elif c < 4 : dic[s[0]] += 4-c

    lst = list(dic.items())

    for i in range(0, 8, 2):
        if lst[i][1] < lst[i+1][1]: ans += lst[i+1][0]
        else: ans += lst[i][0]
    return ans