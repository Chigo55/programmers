def solution(s):
    l = 0 
    same = 0
    diff = 0 
    answer = []
    for r in range(len(s)):
        if s[l] == s[r]:
            same += 1
        else:
            diff += 1
            
        if same == diff:
            answer.append(s[l:r+1])
            l = r+1
        else:
            if r == len(s)-1:
                    answer.append(s[r])
                    
    return len(answer)