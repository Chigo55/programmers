def solution(s):
    from collections import deque    
    stack = deque()
    
    if (s[0] != '(') or (len(s)%2 != 0):
        return False
    
    for i in s:
        if i == '(':
            stack.append(i)
        elif stack and i == ')':
            stack.pop()
            
    if stack:
        return False
        
    return True