def solution(array):
    dic = {num:idx for idx, num in enumerate(array)}
    return [max(dic.keys()), dic[max(dic.keys())]]