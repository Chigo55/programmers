def solution(clothes):
    ans = 1
    dic = dict()
    
    for name, kind in clothes:
        if kind in dic.keys():
            dic[kind] += [name]
        else:
            dic[kind] = [name]
    
    for val in dic.values():
        ans *= len(val) + 1


    return ans - 1

# from collections import Counter
# from functools import reduce

# def solution(clothes):
#     counter = Counter([type for clothe, type in clothes])
#     ans = reduce(lambda acc, cur: acc*(cur+1), counter.values(), 1) - 1
#     return ans