def solution(s):
    answer = s.split(' ')
    answer = [words.capitalize() for words in answer]
    answer = ' '.join(answer)
    return answer