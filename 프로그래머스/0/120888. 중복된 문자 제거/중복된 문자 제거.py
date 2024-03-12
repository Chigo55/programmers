def solution(my_string):
    answer = ''
    dic = {string:idx for idx, string in enumerate(my_string)}
    answer = ''.join(dic.keys())
    return answer