def solution(s):
    s = list(map(int, s.split()))
    max_s = str(max(s))
    min_s = str(min(s))
    answer = [min_s, max_s]
    answer = ' '.join(answer)
    return answer