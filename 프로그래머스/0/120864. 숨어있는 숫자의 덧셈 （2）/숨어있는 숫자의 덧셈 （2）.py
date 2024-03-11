def solution(my_string):
    import re
    words = [word for word in re.sub(r'[a-zA-Z]', ' ', my_string).split()]
    print(words)
    answer = sum(map(int, words))
    return answer