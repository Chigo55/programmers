def solution(A,B):
    answer = 0
    
    A.sort()
    B.sort(reverse=True)
    while A:
        a, b = A.pop(0), B.pop(0)
        answer = answer + (a * b)
    
    return answer