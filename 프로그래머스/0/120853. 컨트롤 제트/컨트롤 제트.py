def solution(s):
    stack = []
    s = s.split()

    for num in s:
        if num != 'Z':
            stack.append(num)
        elif num == 'Z':
            stack.pop()
            
    answer = sum(list(map(int, stack)))
    return answer