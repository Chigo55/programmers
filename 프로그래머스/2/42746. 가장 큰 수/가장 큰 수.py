def solution(numbers):
    answer = str(int(''.join(sorted(list(map(str, numbers)), key= lambda x: x*3, reverse=True))))
    return answer